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
import os


TOKEN = 'ODgwNTE5MjU3MTA3MDg3MzYy.YSfddg.7uqPUGT_d6vb9DOXhEmId69jB7Q'

client = commands.Bot(command_prefix = '.')


client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


client.run(TOKEN)
