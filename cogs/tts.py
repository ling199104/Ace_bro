from discord.ext import commands
from xml.etree import ElementTree
import discord, os, requests, time, re, random
from azure.cognitiveservices.language.textanalytics import TextAnalyticsClient
from msrest.authentication import CognitiveServicesCredentials

tts_subscription_key = '847c5564b72843bb93dc8da4ae3c3154'
text_analytics_subscription_key = '253b66fe212241c080356c2819512b08'

class TTSMessage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.tts_subscription_key = tts_subscription_key

    @commands.Cog.listener()
    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author == self.bot.user:
            return

        # Note: if there are too many messages at the same time, some messages will be missed.
        r_content = re.sub(r'\<\S+\>', '', message.content) # delete mentioned user_id
        r_content = re.sub(r'@\S+\s', '', r_content)
        r_content = re.sub(r'^https?:\/\/.*[\r\n]*', '', r_content, flags=re.MULTILINE)
        if len(r_content) <50: # if a sentence is too long, then ignore it.
            guild = message.guild
            if guild.me.voice != None: # if bot is in any voice channel
                voice_client: discord.VoiceClient = discord.utils.get(self.bot.voice_clients, guild=guild)
                if len(guild.me.voice.channel.members) > 1: # another or the other user in voice channel
                    if not voice_client.is_playing():
                        if not message.content.startswith('!'):
                            app = TextToSpeech(tts_subscription_key, message.author.display_name, r_content) # generate .mp3 file
                            app.get_token()
                            app.save_audio()
                            audio_source = discord.FFmpegPCMAudio('temp.mp3')
                            if guild.me.voice != None:
                                try:
                                    await voice_client.play(audio_source, after=None)
                                except:
                                    pass
                elif len(guild.me.voice.channel.members) == 1:
                    await voice_client.disconnect()

    @commands.command(name='來')
    async def join_vc(self, ctx):
        guild = ctx.guild
        if guild.me.voice != None: # if bot is in any voice channel
            voice_client: discord.VoiceClient = discord.utils.get(self.bot.voice_clients, guild=guild)
            await voice_client.disconnect()
            if ctx.message.author.voice != None: # message's author is in a voice channel
                channel = ctx.message.author.voice.channel
                await channel.connect()
            else:
                channel = ctx.message.channel
                await channel.send('貴使用者並不在任何語音頻道內，請不要講幹話。')
        else: # bot is not in any voice channel
            if ctx.message.author.voice != None: # message's author is in a voice channel
                channel = ctx.message.author.voice.channel
                await channel.connect()
            else:
                channel = ctx.message.channel
                await channel.send('貴使用者並不在任何語音頻道內，請不要講幹話。')

    @commands.command(name='滾')
    async def leave_vc(self, ctx):
        for x in self.bot.voice_clients:
            if(x.guild == ctx.message.author.guild):
                return await x.disconnect()
        return await ctx.message.channel.say('鍋P4窩')

    @commands.command(name='唱', aliases=['播', '播放', 'play', 'sing', 's', \
        '停', '停止', '停停停', '別', '鬧', '別鬧', 'queue', 'que', 'stop'])
    async def play(self, ctx, song_name=None):
        guild = ctx.guild
        voice_client: discord.VoiceClient = discord.utils.get(self.bot.voice_clients, guild=guild)
        if guild.me.voice != None: # if bot is in any voice channel
            if ctx.message.author.voice != None: # message's author is in a voice channel
                if song_name!=None:
                    try:
                        audio_source = discord.FFmpegPCMAudio('./data/music/{}.mp3'.format(song_name))
                        if not voice_client.is_playing():
                            await voice_client.play(audio_source, after=None)
                        else:
                            await voice_client.stop()
                            await voice_client.play(audio_source, after=None)
                    except:
                        pass
                else:
                    try:
                        await voice_client.stop()
                    except:
                        pass
            else:
                await ctx.message.channel.send('你給我進來')
        else:
            await ctx.message.channel.send('歹勢 拎北牟營')

    @commands.command(name='歌單', aliases=['playlist', 'songlist', 'listsongs'])
    async def playlist(self, ctx):
        channel = ctx.message.channel
        song_list = []
        for file in os.listdir("./data/music/"):
            if file.endswith(".mp3"):
                song_list.append(os.path.splitext(file)[0])
        try:
            song_list.remove('temp')
        except:
            pass
        await channel.send(', '.join(song_list))

def setup(bot):
    bot.add_cog(TTSMessage(bot))

class TextToSpeech(object):
    def __init__(self, tts_subscription_key, tts_author, tts_text):
        self.tts_subscription_key = tts_subscription_key
        self.text_key = text_analytics_subscription_key
        self.tts = tts_text
        self.author = tts_author
        self.access_token = None
        
    def get_token(self):
        fetch_token_url = "https://eastasia.api.cognitive.microsoft.com/sts/v1.0/issueToken"
        headers = {
            'Ocp-Apim-Subscription-Key': self.tts_subscription_key
        }
        response = requests.post(fetch_token_url, headers=headers)
        self.access_token = str(response.text)

    def save_audio(self):
        base_url = 'https://eastasia.tts.speech.microsoft.com/'
        path = 'cognitiveservices/v1'
        constructed_url = base_url + path
        headers = {
            'Authorization': 'Bearer ' + self.access_token,
            'Content-Type': 'application/ssml+xml',
            'X-Microsoft-OutputFormat': 'riff-24khz-16bit-mono-pcm',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
        }
        xml_body = ElementTree.Element('speak', version='1.0')
        xml_body.set('{http://www.w3.org/XML/1998/namespace}lang', 'zh-Hant')
        voice = ElementTree.SubElement(xml_body, 'voice')
        voice.set('{http://www.w3.org/XML/1998/namespace}lang', 'zh-Hant')
        ld = Lang_Detection(self.text_key, self.tts)
        result = ld.language_detection()
        if result != None:
            voice.set('name', result)
            voice.text = '{}さんは、{}と言った。'.format(self.author, self.tts)
        else:
            accent_list = [
                "Microsoft Server Speech Text to Speech Voice (zh-TW, Zhiwei, Apollo)",\
                "Microsoft Server Speech Text to Speech Voice (zh-TW, HanHanRUS)",\
                "Microsoft Server Speech Text to Speech Voice (zh-TW, Yating, Apollo)",\
                "Microsoft Server Speech Text to Speech Voice (zh-CN, Kangkang, Apollo)",\
                "Microsoft Server Speech Text to Speech Voice (zh-CN, Yaoyao, Apollo)",\
                "Microsoft Server Speech Text to Speech Voice (zh-CN, HuihuiRUS)"]
            random_accent = random.choice(accent_list)
            voice.set('name', random_accent)
            voice.text = '{}說了，{}'.format(self.author, self.tts)
        
        body = ElementTree.tostring(xml_body)

        response = requests.post(constructed_url, headers=headers, data=body)
        if response.status_code == 200:
            with open('temp.mp3', 'wb') as audio:
                audio.write(response.content)
                print("\nStatus code: " + str(response.status_code))
        else:
            print("\nStatus code: " + str(response.status_code) + "\nSomething went wrong. Check your subscription key and headers.\n")

class Lang_Detection(object):
    def __init__(self, text_key, text):
        self.key = text_key
        self.text = text
        self.endpoint = 'https://eastasia.api.cognitive.microsoft.com'

    def authenticateClient(self):
        credentials = CognitiveServicesCredentials(self.key)
        text_analytics_client = TextAnalyticsClient(
            endpoint=self.endpoint, credentials=credentials)
        return text_analytics_client
        
    def language_detection(self):
        text = self.text
        client = self.authenticateClient()

        try:
            documents = [
                {'id': '1', 'text': text}
            ]
            response = client.detect_language(documents=documents)

            for document in response.documents:
                print("Language: ", document.detected_languages[0].name) #document.detected_languages[0].iso6391_name
                if document.detected_languages[0].name == 'Japanese':
                    return "Microsoft Server Speech Text to Speech Voice (ja-JP, Ayumi, Apollo)"
                else:
                    return None

        except Exception as err:
            print("Encountered exception. {}".format(err))
        


if __name__ == "__main__":
    tts_text = '你今天過得怎麼樣？'
    tts_author = '路西法'
    app = TextToSpeech(tts_subscription_key, tts_author, tts_text)
    app.get_token()
    app.save_audio()
