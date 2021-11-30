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

ts = 0
tm = 0
th = 0
td = 0

servers = []

@tasks.loop(seconds=2.0)
async def uptimeCounter():
  global ts, tm, th, td
  timee = open("saving/time.txt", "r")
  timee = eval(timee.read())
  ts = timee[0]
  tm = timee[1]
  th = timee[2]
  td = timee[3]
  ts += 2
  if ts == 60:
    ts = 0
    tm += 1
    if tm == 60:
      tm = 0
      th += 1
      if th == 24:
        th = 0
        td +=1
  times = [ts, tm, th, td]
  timee = open("saving/time.txt", "w")
  timee.write(str(times))
  timee.close()

  
  
uptimeCounter.start()











class Stats(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def stats(self, ctx):
      global ts, tm, th, td
      embed = nextcord.Embed(title="My Time online")
      embed.add_field(name="Days:", value=td, inline=True)
      embed.add_field(name="Hours:", value=th, inline=True)
      embed.add_field(name="Minutes:", value=tm, inline=True)
      embed.add_field(name="Seconds:", value=ts, inline=True)
      await ctx.send(embed=embed)

    @commands.Cog.listener()
    async def on_message(self, message):
      guild = message.guild.name
      servers = open("saving/servers.txt", "r")
      servers = eval(servers.read())
      if not guild in servers:
        servers.append(guild)
        serverss = open("saving/servers.txt", "w")
        serverss.write(str(servers))
        serverss.close()

    @commands.command()
    async def servers(self, ctx):
      zervers = open("saving/servers.txt", "r")
      zervers = eval(zervers.read())
      des = "**"
      for x in zervers:
        des = des + x + "\n"
      des = des + "**"
      embed = nextcord.Embed(title="My Servers", description=des)
      await ctx.send(embed=embed)

   

def setup(client):
    client.add_cog(Stats(client))















