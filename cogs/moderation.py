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

class moderation(commands.Cog):

    def __init__(self, client):
        self.client = client




    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member : nextcord.Member, *, reason=None):
        await member.kick(reason=reason)


    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member : nextcord.Member, *, reason=None):
        await member.ban(reason=reason)


    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=5):
        await ctx.channel.purge(limit=amount)


def setup(client):
    client.add_cog(moderation(client))
