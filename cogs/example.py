import discord
from discord.ext import commands

class Example(commands.Cog):

    def __init__(self, client):
        self.client = client



    #ONLINE
    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot Example Ready')

    ##CODE
    @client.event
    async def on_message(message):
        



#end
def setup(client):
    client.add_cog(Example(client))
