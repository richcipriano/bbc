import discord
import json
import os
from discord.ext import commands

client = commands.Bot(command_prefix = '$')


##COGS
@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


client.run('NzQ2NDc3MzQxMTM1MzM5NjYx.X0A5Mw.LGdS9IAV9WCYlf7XgwFYoQ7HWkQ')
