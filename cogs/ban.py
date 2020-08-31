from discord.ext import commands
import discord
import os, time
import re
class CountReaction(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        poop = u"\U0001F4A9"
        if reaction.emoji != poop:
            pass
        else:
            await self

    async def timer(self, reaction): #triggered 1 time
        msg = reaction.message
        def check_count_reaction(desired_count, reaction): #checks the number of poop reactions
            if reaction.count >= desired_count:
                return True
        timeout = time.time() + 60
        while True:
            if time.time() > timeout:
                break
            if check_count_reaction(3, reaction): #triggered 3 time
                await msg.delete()
                #await msg.edit(content="||{}||".format(msg))
                break
            time.sleep(1)
        pass

        

def setup(bot):
    bot.add_cog(CountReaction(bot))