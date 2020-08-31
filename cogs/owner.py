from discord.ext import commands
import checks
import asyncio
class OwnerCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Hidden means it won't show up on the default help.
    # clearall can delete data within two weeks, up to 100 data at a time
    @commands.command(name='clearall', hidden=True)
    @checks.is_owner()
    async def clear_all_messages(self, ctx, number=100):

        number = int(number)
        messages = []
        async for message in ctx.channel.history(limit=number):
            messages.append(message)
        await ctx.channel.delete_messages(messages)

    # clear can delete a piece of data at a time
    @commands.command(name='clear', hidden=True)
    @checks.is_owner()
    async def clear_lines_message(self, ctx, number):

        number = int(number)
        counter = 0
        messages = []
        async for x in ctx.channel.history(limit=number):
            if counter < number:
                messages.append(x)
                await ctx.channel.delete_messages(messages)
                messages = []
                counter += 1
                await asyncio.sleep(1.2)

    @commands.command(name='load', hidden=True)
    @checks.is_owner()
    async def load_cog(self, ctx, *, cog: str):
        """Command which Loads a Module.
        Remember to use dot path. e.g: cogs.owner"""

        try:
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')

    @commands.command(name='unload', hidden=True)
    @checks.is_owner()
    async def unload_cog(self, ctx, *, cog: str):
        """Command which Unloads a Module.
        Remember to use dot path. e.g: cogs.owner"""

        try:
            self.bot.unload_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')

    @commands.command(name='reload', hidden=True)
    @checks.is_owner()
    async def reload_cog(self, ctx, *, cog: str):
        """Command which Reloads a Module.
        Remember to use dot path. e.g: cogs.owner"""

        try:
            self.bot.unload_extension(cog)
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')


def setup(bot):
    bot.add_cog(OwnerCog(bot))