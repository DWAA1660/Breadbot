from nextcord.ext import tasks
from asyncio.tasks import wait_for
from sys import prefix
import nextcord
from nextcord import *
from nextcord import channel
from nextcord import reaction
from nextcord import message
from nextcord import emoji
from nextcord import guild
from nextcord.ext import commands
import random
import requests
import asyncio
import datetime
import time

class Example(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is ready')
        game = nextcord.Game("DWAA#1660 makes bots https://discord.gg/KqnUku9XA2")
        await self.client.change_presence(status=nextcord.Status.idle, activity=game)
       

    @commands.command()
    async def ping(self, ctx):
        await ctx.send('Pong!')


def setup(client):
    client.add_cog(Example(client))