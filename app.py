import discord
from discord.ext import commands
import asyncio
import random, os, sys, traceback
import checks

if 'ACE_BRO_KEY' in os.environ:
    TOKEN = os.environ['ACE_BRO_KEY']

else:
    print('Environment variable for ACE_BRO_KEY is not set.')
    exit()

description = '''
    📣大家好、打給賀、胎嘎後，我是本群組圈養的bot，請多指教
    '''

initial_extensions = ['cogs.owner', 'cogs.ban', 'cogs.mention', 'cogs.rich', 'cogs.tts']

bot = commands.Bot(command_prefix='!', description=description)

# Here we load our extensions(cogs) listed above in [initial_extensions].
if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Failed to load extension {extension}.', file=sys.stderr)
            traceback.print_exc()

@bot.event
async def on_ready():
    """https://discordpy.readthedocs.io/en/latest/api.html?highlight=on_ready#discord.on_ready"""

    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')

    # Changes our bots Playing Status. type=1(streaming) for a standard game you could remove type and url.
    game = discord.Game("Anno 1800")
    await bot.change_presence(status=discord.Status.idle, activity=game)
    print(f'Successfully logged in and booted...!')

bot.run(TOKEN, bot=True, reconnect=True)