
from sys import prefix
import nextcord

from nextcord.ext import commands
import random
import requests
import asyncio
import datetime
import time
import os

client = commands.Bot(command_prefix = '.')





class Confirm(nextcord.ui.View):
  def __init__(self):
    super().__init__()
    self.value = None
  
 









client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


client.run(os.getenv("TOKEN")) # EDIT: Moved to secrets.
#this uses replits env format you can also use client.run('tokenhere')
