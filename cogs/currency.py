import discord
import json
import os
from discord.ext import commands

class Example(commands.Cog):

    def __init__(self, client):
        self.client = client


    #ONLINE
    @commands.Cog.listener
    async def on_ready(self):
        print('Bot Currency is ready')

        ...

   

def setup(client):
    client.add_cog(Example(client))
