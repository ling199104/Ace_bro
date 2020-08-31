from discord.ext import commands
import discord
import re

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

ctbot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(ctbot)
trainer.train("./data/learning_corpus/")
ctbot.read_only = True #if True, bot will NOT learning after training
"""
import process_model as pm #import emotion recognition model
def response_text(text):
    processed_text = pm.response(text)
    return processed_text
"""

class ChatMentioned(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        channel = message.channel
        if message.author == self.bot.user:
            return

        if self.bot.user.mentioned_in(message):
            message_content = re.sub(r'\S@\S+','',message.content)
            await channel.send(get_res(message_content))
        #await self.bot.process_commands(message)

def setup(bot):
    bot.add_cog(ChatMentioned(bot))

def get_res(userText):
    #processed_text = response_text(userText) #get text emotion prediction
    return (str(ctbot.get_response(str(userText))))
    #return (str(ctbot.get_response(userText)) + '(' + processed_text + ')')

