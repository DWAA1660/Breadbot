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

class games(commands.Cog):

    def __init__(self, client):
        self.client = client


    
    @commands.command()
    async def kill(self, ctx, *, person):
     deaths = ['blended by fan',
                    'chopped into soup',
                    'thrown off a cliff',
                    'roasted in space',
                    'your mom\'ed to oblivion']		
	
     await ctx.send(f'  {person} was {random.choice(deaths)}')


    @commands.command()
    async def funfact(self, ctx):

        fax = ['American flags left on the moon will eventually get bleached white by the sun.',
	'While they are hibernating, bears do not urinate. Their bodies convert waste into protein.',
	'White-faced capuchin monkeys greet each other by sticking their fingers up each others’ noses.',
	'Gummy bears were originally called dancing bears.',
	'New Zealand has more cats per person than any other country in the world.',
	'The hagfish is the only animal that has a skull but no spine.',
	'People weigh less if they stand at the equator than if they stand at the North or South poles.',
	'At their closest points, the U.S and the Soviet Union are over 2 miles (3km) apart.',
	'The yo-yo was originally a weapon used in the Philippine jungle.',
	'Victor Hugo’s novel Les Miserable contains a sentence that is 823 words long.',
	'Alexander the Great was the first person to be pictured on a coin.',
	'FDR’s portrait was on the dime because of his association with the March of Dimes charity.',
	'The sun weighs 2,000 million million million million tons.',] 
        await ctx.send(f'{random.choice(fax)}')


    @commands.command()
    async def qq(self, ctx, *, person):
     responsessize = ['8==>',
				'8===>',
				'8====>',
				'8=====>',
                '8======>',
                '8=======>',
                '8========>',
                '8=========>',
                '8==========>',
                '*nothing*']		
	
     await ctx.send(f'  {person}\'s qq size is: {random.choice(responsessize)}')    


    @commands.command()
    async def kiss(self, ctx):
        await ctx.message.add_reaction("💋")

    @commands.command()
    async def soup(self, ctx):
        await ctx.send('SOUP')


def setup(client):
    client.add_cog(games(client))
