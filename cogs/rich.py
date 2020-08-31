from discord.ext import commands
import discord
import requests
import os, random
import re
import time
from bs4 import BeautifulSoup as bs
class RichMessage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        channel = message.channel
        # we do not want the bot to reply to itself
        if message.author == self.bot.user:
            return

        rabbit_list = os.listdir("./data/rabbit/")
        if message.content.startswith(''):
            filename_list = [x for x in rabbit_list if os.path.splitext(x)[0] == message.content]
            if filename_list:
                await channel.send(content='', file=discord.File(fp='./data/rabbit/{}'.format(filename_list[0])))

        north_list = os.listdir("./data/Dutch_Harbor/")
        if message.content.startswith(''):
            filename_list = [x for x in north_list if os.path.splitext(x)[0] == message.content]
            if filename_list:
                await channel.send(content='', file=discord.File(fp='./data/Dutch_Harbor/{}'.format(filename_list[0])))
def setup(bot):
    bot.add_cog(RichMessage(bot))