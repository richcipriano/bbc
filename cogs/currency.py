import discord
import json
import os
from discord.ext import commands

client = commands.Bot

class Example(commands.Cog):

    def __init__(self, client):
        self.client = client


    #ONLINE
    @commands.Cog.listener
    async def on_ready(self):
        print('Bot Currency is ready')

        ...

    @client.event
    async def on_message(self, member):
        with open('users.json', 'r') as f:
            users = json.load(f)

        await update_data(users, member)

        with open('users.json', 'w') as f:
            json.dump(users, f)

        ...

    @client.event
    async def on_member_join(self, member):
        with open('users.json', 'r') as f:
            users = json.load(f)

        await update_data(users, message.author)
        await add_experience(users, message.author, 5)
        await level_up(users, message.author, message.channel)

        with open('user.json', 'w') as f:
            json.dump(users, f)

    async def update_data(self, users, user):
        if not user.id in users:
            users[user.id] = {}
            users[user.id]['experience'] = 0
            users[user.id]['level'] = 1

    async def add_experience(self, users, user, exp):
        users[user.id]['experience'] = experience

    async def level_up(self, users, user, channel):
        experience = users[user.id]['experience']
        lvl_start = users[user.id]['level']
        lvl_end = int(experience ** (1/4))

        if lvl_start < lvl_end:
            await client.send.message(channel, '{} lucrou ${}'.format(user.mention, lvl_end))
        ...

def setup(client):
    client.add_cog(Example(client))
