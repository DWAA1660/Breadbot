
import nextcord

from nextcord.ext import commands
import random
import requests
import asyncio
import datetime
import time

class Example(commands.Cog):

    def __init__(self, client):
        self.client = client


    
  #cool help command

    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is ready')
        game1 = nextcord.Game("DWAA#1660 makes bots https://discord.gg/KqnUku9XA2")
        game2 = nextcord.Game("hi")
        await self.client.change_presence(status=nextcord.Status.online, activity=game1)
        
        await self.client.change_presence(status=nextcord.Status.online, activity=game1)
          

    @commands.command()
    async def ping(self, ctx):
        await ctx.send('Pong!')



def setup(client):
    client.add_cog(Example(client))
