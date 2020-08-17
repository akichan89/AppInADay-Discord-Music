  
import discord
import os
from discord.ext import commands

bot = commands.Bot(command_prefix=os.getenv('PREFIX'))

@bot.event
async def on_ready():
  print(f'{bot.user} has logged in.')
  bot.load_extension('cogs.music')

bot.run('NzQ0OTY1NjE2NDgxMzM3Mzk0.Xzq5Sw.E0hlh06dvxRlZfNChL_yRFsBV1k')