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



TOKEN = 'ODgwNTE5MjU3MTA3MDg3MzYy.YSfddg.dl-439xq86Fdlj14XUHM0H3p5ZM'

client = commands.Bot(command_prefix = '.')





@client.event
async def on_ready():
    await client.change_presence(status=nextcord.Status.online, activity=nextcord.Game('Winning bot contest'))
    print('Bot is ready.')
    garf.start()

    
	


num = 4
@tasks.loop(seconds = 10 )
async def garf():
    global num
    channel = client.get_channel(873789547811602503)
    await channel.send(file=nextcord.File(fr'C:\Users\dwatn\OneDrive\Desktop\garfffi\Breadbot\{num}.png'))
    num += 1



@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)} ms')	
	
	
	
@client.command(aliases=['8ball', 'test'])
async def _8ball(ctx, *, question):
	responses = ['yes',
				'no',
				'maybe',
				'ok but like idc']		
	
	await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')






@client.command()
async def clear(ctx, amount=5):
    if (ctx.message.author.permissions_in(ctx.message.channel).manage_messages):
        await ctx.channel.purge(limit=amount)

@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send('Sorry you are not allowed to use this command.')






@client.command()
async def funfact(ctx):

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
	'The sun weighs 2,000 million million million million tons.',



	]
	await ctx.send(random.choice(fax))

@client.command()
async def kiss(ctx):
    await ctx.message.add_reaction("💋") 



@client.command()
async def cat(ctx):
    r = requests.get("https://api.thecatapi.com/v1/images/search").json()

    cat_em = nextcord.Embed()
    cat_em.set_image(url=f'{r[0]["url"]}')

    await ctx.send(embed=cat_em)

@client.command()
async def positive(ctx):
    await ctx.message.add_reaction("✅") 
    await ctx.message.add_reaction("⛔")
    
    # Makes a function to verify that the reaction is from the author and is the thumbs up emote.
    def check(reaction, user):
        return user == ctx.message.author and str(reaction.emoji) == '✅'
    try:
        # Makes the bot wait for the reaction with the 60 second timeout
        reaction, user = await client.wait_for('reaction_add', timeout=10.0, check=check)
    except asyncio.TimeoutError:
        # If it times out, do this.
        await ctx.send("You are negative :(")
    else:
        # If the check succeeds, do this.
        await ctx.send("You are positive :D")





@client.command()
async def wisdom(ctx):
 with open('./resources/file.txt', 'r', encoding="utf8") as file:
      await ctx.send(random.choice(file.readlines()))

@client.command()
async def nerd(ctx):

    await ctx.send("@Anthony2be#1900 is nerd")      



client.run(TOKEN)
