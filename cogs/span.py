from discord.ext import commands
from bs4 import BeautifulSoup as bs
import discord
import requests
import os, random, re, time

class SpanMessage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_reaction_remove(self, reaction, user):
        channel = reaction.message.channel
        await channel.send('{} 不小心按錯了，默默的從 {} 收回了一個 {} ...好害羞...'\
        .format(user.name, reaction.message.content, reaction.emoji))

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        channel = reaction.message.channel
        await channel.send('{} 獲得了一個來自於 {} 的 {}，才...才不開心呢！'\
        .format(reaction.message.author.name, user.name, reaction.emoji))

    @commands.Cog.listener()
    async def on_message(self, message):
        channel = message.channel
        # we do not want the bot to reply to itself
        if message.author == self.bot.user:
            return
        if message.author.id == 149471797547368449:
            if len(message.content)>80:
                y_list = ['我的心中，沒有一絲一毫的喜悅','我的內心，沒有一絲一毫的喜悅','不要再搞這些了','wonderful',\
                '對不起啦','這是不可能的','一絲一毫的喜悅都沒有','我感覺到無比沉重的壓力','我非常討厭你知道嗎',\
                '所以內心是很寂寞','絕對不會懈怠','我想標準都該一致','還是做你自己吧','我覺得還是需要一些天份',\
                '永不改變，永不放棄','誰影響誰的','誰影響誰大不一定','我們完全沒問題','其實很寂寞','不只啦不只',\
                '其實我覺得是這樣啦，有時候以前...以前沒有仔細想，現在開始很認真想了啦','說謊成性啦','跟著月亮走，好不好',\
                '你知道我對這種題目都嗤之以鼻你知道嗎']
                await channel.send(random.choice(y_list))
        if message.content.startswith('daisuke'):
            await channel.send('らい☆なう')
            await channel.send('https://youtu.be/XUV863a1Lok?t=91')
            time.sleep(3)
            await channel.send('Daisuke☆')
        if message.content.startswith('嘔'):
            await channel.send('<a:disgusting_r:600695954034917387><a:disgusting_r:600695954034917387><a:disgusting_r:600695954034917387><a:disgusting_r:600695954034917387><a:disgusting_r:600695954034917387>')
        if '人類' in message.content:
            await channel.send(message.content)
        if message.content.startswith('そんな装備で大丈夫か'):
            time.sleep(2)
            await channel.send('大丈夫だ、問題ない')
        if '意思' in message.content:
            await channel.send(message.content)
        if '貧窮' in message.content:
            await channel.send(message.content)
        if 'ん？' in message.content:
            time.sleep(2)
            await channel.send('流れ変わったな')
        if 'まだ弱い' in message.content:
            time.sleep(2)
            await channel.send('強くなりそう')
        if 'やったぜ' in message.content:
            time.sleep(1)
            await channel.send('<a:the_king:532257579280367636>')
        if 'ザ・ワールド' in message.content:
            time.sleep(1)
            await channel.send('ザ・ワールドッ!!!ブゥォオオン！チッチッチッチッチッチッチ...!!!ウィーーン...!カチッ!')
            time.sleep(1)
            await channel.send('<a:dio_left:573373905595531277><a:dio_right:573373972964573186>')
        if '是什麼蒙蔽了我的雙眼' in message.content:
            await channel.send('<:titblind:622964808681127957>')
        if u"\U0001F914" in message.content: #thinking
            rd_thinking = ['<:the_thinker:532467511984128000>','<:fox_thinking:532467484322824192>',\
            '<:ttttt_thinking:532467415066345493>','<:tai_thinking:532467386985742337>',\
            '<:suicide_thinking:532467352504238080>','<:v_thinking:532467290084474880>',\
            '<:tttttthinking:532467249643257866>','<:yelo1:532241454932688906>',\
            '<:ussr_thinking:532460309185691671>','<:thththinking:532460899135389697>',\
            '<:big_hand_thinking:532461326379778072>','<:eggplant_thinking:532460679391870976>',\
            '<:finger_thinking:532461900328599552>','<:hand_thinking:532461608627339264>',\
            '<:mad_thinking:532461930166878208>']
            await channel.send(random.choice(rd_thinking))
        if message.content.startswith('xvmsnipe'):
            usrmsg = [await channel.fetch_message(message.id)]
            playerID = message.content[8:]
            wn8 = wn8_parser(playerID)
            text = '{0.author.mention} '.format(message) + playerID + '的wn8是：' + wn8
            await channel.send(text)
            if int(wn8)>=2180:
                response1 = '由於數值過高，已被敵方自走砲鎖定！'
                await channel.send(response1)
                time.sleep(1)
                response2 = 'сука блять!'
                await channel.send(response2)
                time.sleep(2)
                await channel.delete_messages(usrmsg)
                time.sleep(1)
                response3 = '我們重創目標！目標坦克%s已被摧毀！' % playerID
                await channel.send(response3)
            elif 2180>int(wn8)>900:
                response1 = '數值正確。敵方自走砲瞄準中...'
                await channel.send(response1)
                time.sleep(1)
                response2 = 'Click！'
                await channel.send(response2)
                time.sleep(2)
                rd = random.randint(0,1)
                if rd == 0:
                    response3 = '我們未能穿透%s的裝甲！' % playerID
                    await channel.send(response3)
                else:
                    await channel.delete_messages(usrmsg)
                    time.sleep(1)
                    response3 = '裝甲被擊穿！目標坦克%s已被摧毀！' % playerID
                    await channel.send(response3)
            else:
                response1 = '數值一般。敵方自走砲瞄準中...'
                await channel.send(response1)
                time.sleep(1)
                response2 = 'Click！'
                await channel.send(response2)
                time.sleep(2)
                response3 = '跳彈！'
                await channel.send(response3)
        if message.content.startswith('thinking'):
            gif_url = ['https://media.giphy.com/media/XZym5wHFZcnE74CgI8/giphy.gif',\
            'https://media.giphy.com/media/ZBVuIFSO8gLtJDIueV/giphy.gif','https://media.giphy.com/media/U5E4RRFweWC1C40yLD/giphy.gif',\
            'https://media.giphy.com/media/chiFmYZYPS3I84vbqe/giphy.gif','https://media.giphy.com/media/hX0ZRI1la4r3RF8bEA/giphy.gif',\
            'https://media.giphy.com/media/f8ymLuhwl4ABQ6iWwx/giphy.gif','https://media.giphy.com/media/W2RNCHSwUD19EEmsNg/giphy.gif',\
            'https://media.giphy.com/media/UTv6jh5VB5hvWGN1hx/giphy.gif','https://media.giphy.com/media/hS8jNcNVtEgTQnJoQV/giphy.gif',\
            'https://media.giphy.com/media/L05YuWluzAvwYDLlik/giphy.gif','https://media.giphy.com/media/eNYUCygZqaVdMpz8VB/giphy.gif',\
            'https://media.giphy.com/media/hS3BFfwBZBWzTR2HUh/giphy.gif','https://media.giphy.com/media/RghQMjgQes2tLNuVFc/giphy.gif',\
            'https://media.giphy.com/media/lQI4Ff8wv8S7vSPax5/giphy.gif','https://media.giphy.com/media/loiwqjRmuILt5HqOuT/giphy.gif',\
            'https://media.giphy.com/media/Lmg8kI6HrggWPKvWcK/giphy.gif','https://media.giphy.com/media/W4QD46bjXSpAOLYkJl/giphy.gif',\
            'https://media.giphy.com/media/iH70t5t20My5BhDTKc/giphy.gif','https://media.giphy.com/media/dXEjHPLE0nMQu4WyNE/giphy.gif',\
            'https://media.giphy.com/media/IzXDE6DWJA1RleeOKI/giphy.gif','https://media.giphy.com/media/jR03mFmaw9zNZvEyA3/giphy.gif',\
            'https://media.giphy.com/media/JPZeMuZy5pK8n5tg9Q/giphy.gif','https://media.giphy.com/media/Kbw498sbl56kePnpH3/giphy.gif',\
            'https://media.giphy.com/media/f6yclZBlpzfhmvo0vY/giphy.gif','https://media.giphy.com/media/hVn6Ndy1sp1IgYPKRc/giphy.gif',\
            'https://media.giphy.com/media/fSMyLT4bbxvfitR7Ru/giphy.gif','https://media.giphy.com/media/QrcjUXCXmzMOBU1CmT/giphy.gif',\
            'https://media.giphy.com/media/JsPJNC1QTaTqIISRCG/giphy.gif','https://media.giphy.com/media/dXchDujTkFMW120TIO/giphy.gif',\
            'https://media.giphy.com/media/cPkndpQvWzjh5fNcww/giphy.gif']
            embed = discord.Embed(title='',
                              description='',
                              colour=0x000000)
            embed.set_image(url=random.choice(gif_url))
            await channel.send(content='', embed=embed)

        if message.content.startswith('爽'):
            embed = discord.Embed(title='',
                              description='',
                              colour=0x000000)
            embed.set_image(url='https://media.giphy.com/media/LqfKpZ4O5JbqfJRnVv/giphy.gif')
            await channel.send(content='', embed=embed)
        if message.content.startswith('三玖'):
            embed = discord.Embed(title='',
                              description='',
                              colour=0x000000)
            embed.set_image(url='https://media.giphy.com/media/fvf6uF7Kxb3cN2I5WF/giphy.gif')
            await channel.send(content='', embed=embed)
        if message.content.startswith('來來來'):
            embed = discord.Embed(title='',
                              description='',
                              colour=0x000000)
            embed.set_image(url='https://media.giphy.com/media/fvYPPWsq2I3oVbATjR/giphy.gif')
            await channel.send(content='', embed=embed)
        if message.content.startswith('射爆'):
            embed = discord.Embed(title='',
                              description='',
                              colour=0x000000)
            embed.set_image(url='https://media.giphy.com/media/QUWhPxfmDMyjz5YXkN/giphy.gif')
            await channel.send(content='', embed=embed)
        if message.content.startswith('壞壞'):
            embed = discord.Embed(title='',
                              description='',
                              colour=0x000000)
            embed.set_image(url='https://media.giphy.com/media/Q5dcrcsR2IHabZ94zb/giphy.gif')
            await channel.send(content='', embed=embed)
        if ('不喜歡' in message.content) or ('不舒服' in message.content):
            embed = discord.Embed(title='',
                              description='',
                              colour=0x886600)
            embed.set_image(url='https://media.giphy.com/media/ihjhCrgLtzCEBdgcUT/giphy.gif')
            await channel.send(content='', embed=embed)

        if '噁心' in message.content:
            embed = discord.Embed(title='',
                              description='',
                              colour=0x000000)
            embed.set_image(url='https://media.giphy.com/media/VEyTGZtafWRXAM9QYh/giphy.gif')
            await channel.send(content='', embed=embed)

        if ('想一' in message.content) or ('想想' in message.content) or ('思考' in message.content):
            filename = random.choice(os.listdir("./data/thinking/"))
            await channel.send(content='', file=discord.File(fp='./data/thinking/{}'.format(filename)))

        if '真香' in message.content:
            embed = discord.Embed(title='',
                              description='',
                              colour=0x000000)
            rd_sg = ['https://media.giphy.com/media/lsAcmXibgPr4IfcxXC/giphy.gif',\
            'https://media.giphy.com/media/gdTsxdUHoBPIcra7iO/giphy.gif']
            embed.set_image(url=random.choice(rd_sg))
            await channel.send(content='', embed=embed)

        if ('蒸蚌' in message.content) or ('真棒' in message.content):
            embed = discord.Embed(title='',
                              description='',
                              colour=0x000000)
            embed.set_image(url='https://media.giphy.com/media/UQJu3WNRPUVk5OrXsN/giphy.gif')
            await channel.send(content='', embed=embed)

        if '佛' in message.content:
            embed = discord.Embed(title='',
                              description='',
                              colour=0x000000)
            embed.set_image(url='https://media.giphy.com/media/KzneAXxdL39EUDlWZ5/giphy.gif')
            await channel.send(content='', embed=embed)

        if ('巨人' in message.content) or ('牆外' in message.content):
            embed = discord.Embed(title='',
                              description='',
                              colour=0xBB5500)
            embed.set_image(url='https://media.giphy.com/media/fUpmmmKmhJPRn092KS/giphy.gif')
            await channel.send(content='', embed=embed)

        if '豹炸' in message.content:
            embed = discord.Embed(title='',
                              description='',
                              colour=0xFFFFFF)
            embed.set_image(url='https://media.giphy.com/media/kcCix99Fq2YZSZEmHZ/giphy.gif')
            await channel.send(content='(∩ ◕_◕ )⊃━☆ Explosion！！', embed=embed)

        if ('大薯' in message.content) or ('M記' in message.content):
            embed = discord.Embed(title='',
                              description='',
                              colour=0x000000)
            embed.set_image(url='https://media.giphy.com/media/Jqzc8uasABrAlHmKjU/giphy.gif')
            await channel.send(content='牡丹樓薯條真係好味!', embed=embed)

        if '食屎' in message.content:
            embed = discord.Embed(title='',
                              description='',
                              colour=0x007799)
            embed.set_image(url='https://media.giphy.com/media/jtKRojw9cLJ5uYQ7AC/giphy.gif')
            await channel.send(content='吔屎啦你!', embed=embed)

        if 'FBI' in message.content:
            embed = discord.Embed(title='',
                              description='',
                              colour=0x000000)
            embed.set_image(url='https://media.giphy.com/media/QXDWs28HekoVAc7JMM/giphy.gif')
            await channel.send(content='上車!', embed=embed)

        if ('維尼' in message.content) or ('習近平' in message.content):
            embed = discord.Embed(title='',
                              description='',
                              colour=0x000000)
            embed.set_image(url='https://media.giphy.com/media/h467vErPErZ0i5HbnQ/giphy.gif')
            await channel.send(content='**呢 嘛 叭 唭**', embed=embed)

        if '我全都要' in message.content:
            embed = discord.Embed(title='',
                              description='',
                              colour=0x000000)
            embed.set_image(url='https://media.giphy.com/media/chVOqKDQCmKYV5dSu9/giphy.gif')
            await channel.send(content='一個也不能少！', embed=embed)

        if '危險' in message.content:
            embed = discord.Embed(title='',
                              description='',
                              colour=0x000000)
            embed.set_image(url='https://media.giphy.com/media/TgsLyaSezPYmJouaju/giphy.gif')
            await channel.send(content='', embed=embed)

        if '歹勢' in message.content:
            embed = discord.Embed(title='',
                              description='',
                              colour=0x000000)
            embed.set_image(url='https://media.giphy.com/media/WRFfXu6xIUfMfdLq3C/giphy.gif')
            await channel.send(content='', embed=embed)

        if '都發財' in message.content:
            embed = discord.Embed(title='',
                              description='',
                              colour=0x000000)
            embed.set_image(url='https://media.giphy.com/media/MCGFrh9s8Zdi0By0NH/giphy.gif')
            await channel.send(content='', embed=embed)

        if '興奮' in message.content:
            embed = discord.Embed(title='',
                              description='',
                              colour=0xFF0000)
            embed.set_image(url='https://media.giphy.com/media/wrBkgZYJA1xLoDPtSW/giphy.gif')
            """
            embed.set_author(name='MysterialPy',
                            url='https://gist.github.com/MysterialPy/public',
                            icon_url='http://i.imgur.com/ko5A30P.png')


            embed.add_field(name='Embed Visualizer', value='[Click Here!](https://leovoel.github.io/embed-visualizer/)')
            embed.add_field(name='Command Invoker', value=ctx.author.mention)
            embed.set_footer(text='Made in Python with discord.py@rewrite', icon_url='http://i.imgur.com/ko5A30P.png')
            """
            await channel.send(content='很興奮!你知道嗎!', embed=embed)



def wn8_parser(playerID):
	r = requests.get('http://www.wotinfo.net/en/efficiency?server=SEA&playername=%s' % (playerID))
	soup = bs(r.text, 'html.parser')
	content = soup.find("var", string="WN8").find_next_siblings('div', class_='text')
	regex = re.compile(r'(\d.\d+)') #篩字串
	match = regex.search(str(content))
	submatch = re.sub(r'\D','',match.group(1)) #篩數字
	return submatch

def setup(bot):
    bot.add_cog(SpanMessage(bot))