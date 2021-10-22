from os import write
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

class files(commands.Cog):

    def __init__(self, client):
        self.client = client


    

    @commands.command(name="qotdwrite", brief="Adds a qotd to que")
    async def qotdwrite(self, context: commands.Context, *, message):
        with open('qotds.txt', 'a') as f:
            f.write(message + '\n')



    @commands.command(name="sg", brief="Suggests a feature to be added to bot")
    async def sg(self, context: commands.Context, *, message):
        with open('suggestions.txt', 'a') as f:
            f.write(message + '\n')
        await context.send('Suggestion has been recorded, Thank You!')
        print('hi')




        
        
    
    
    
    @commands.command(name="qotd", brief="Posts qotd in channel you write this command in")
    async def qotdread(self, ctx):
        with open('qotdnumber.txt', 'r+') as f:
            readvariable = int(f.readline())
        
        file = open('qotds.txt')
        all_lines = file.readlines()
        oknow = (all_lines[readvariable])
        await ctx.send(oknow)
        readvariable += 1

        str(readvariable)
        with open('qotdnumber.txt', 'r+') as f:
            f.write(str(readvariable))       
      
            
         
    @commands.command(name="qotdall", brief="Posts all qotds in channel you write this command in")
    async def qotdreadall(self, ctx):
        with open('qotdnumber.txt', 'r+') as f:
            readvariable = int(f.readline())
        
        file = open('qotds.txt')
        all_lines = file.readlines()
        await ctx.send(all_lines)
        


#@tasks.loop(seconds = 10 )
#async def garf():
 #   global num
  #  channel = client.get_channel(873789547811602503)
  #  await channel.send(file=discord.File(f'{num}.png'))
  #  await channel.send(file=nextcord.File(fr'C:\Users\dwatn\OneDrive\Desktop\garfffi\Breadbot\{num}.png'))
 #   num += 1


def setup(client):
    client.add_cog(files(client))
