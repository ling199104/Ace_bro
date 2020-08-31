from discord.ext import commands

def is_owner():
    def predicate(ctx):
        return ctx.message.author.id == 149471723576623105
    return commands.check(predicate)