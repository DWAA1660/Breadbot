from nextcord.ext import tasks
from asyncio.tasks import wait_for
from sys import prefix
import nextcord

from nextcord.ext import commands
import requests
import asyncio
import datetime
import time
from googlesearch import search
import requests
import json
from PIL import Image, ImageFilter
import urllib
from dadjokes import Dadjoke
from better_profanity import profanity
import secrets

#got it working :D

class games(commands.Cog):

    def __init__(self, client):
        self.client = client


    
    @commands.command(brief="do the die to someone ex .kill @member")
    async def kill(self, ctx, *, person):
      deaths = ['blended by fan',
                            'chopped into soup',
                        'thrown off a cliff',
                        'roasted in space',
                        'your mom\'ed to oblivion',
                        'removed from existance',
                        'exploded',
                        'killed by a spoon',
                        'ejected from the ship',
                        'swallowed by a black hole']	
      insults = [
        'I love my job >:)',
        'Get ded newb',
        'Time to die :)',
        'I kill all things with a smile',
        'Murder is ||fun||',
        'I\'m the Imposter. But you won\'t live long enough to tell anyone.',
        'Has been impostered',
      ]	
        
      dies = (f'{secrets.SystemRandom().choice(deaths)}')
      embed=nextcord.Embed(title=insults[secrets.SystemRandom().randint(0, len(insults)-1)], description=person + ' was ' + dies)
      await ctx.send(embed=embed)


    @commands.command(name="future", brief="aka 8ball ex. 'future' question")
    async def eightball(self, ctx, *, question):
        answers = ['yes',
          'Absolutly!',
          'depends on you',
          'nahh',
          'go for it',
          'not my problem',
        ]
        ans = (f'{secrets.SystemRandom().choice(answers)}')
        embed=nextcord.Embed(title=question, description=ans)
        await ctx.send(embed=embed)


    @commands.command(brief="states random funfact")
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
	      'The sun weighs 2,000 million million million million tons.'] 

      faxbutactual = (f'{secrets.SystemRandom().choice(fax)}')
      embed=nextcord.Embed(title="FunFact is:", description=faxbutactual)
      await ctx.send(embed=embed)
      
    @commands.command(brief='<3')
    async def kiss(self, ctx):
        await ctx.message.add_reaction("💋")

    @commands.command(brief="SOUP")
    async def soup(self, ctx):
       await ctx.send("SOUP")

    

    @commands.command(brief="slap someone with fish ex. .slap @member")

    async def slap(self, ctx):
      await ctx.send('https://tenor.com/view/fish-slap-w2s-slap-funny-sidemen-gif-20599048')


  

    @commands.command(brief="wikepedia stuff")
    async def wiki(self, ctx, *, search):
       memeApi = urllib.request.urlopen(f"https://en.wikipedia.org/w/api.php?action=query&origin=*&format=json&generator=search&gsrnamespace=0&gsrlimit=5&gsrsearch='{search}'")

       ctx.send(memeApi)





    
   

    @commands.command(brief='google somthing ex. .google number_of_results query')
    async def google(self, ctx, amount, *, query):
      embed = nextcord.Embed(title="Google Results For: "+query, url="https://google.com", description=" ", color=0x4d7cff)
      amount = int(amount)
      if amount > 10:
        amount = 10
      for i in search(query, tld="co.in", num=amount, stop=amount, pause=2):
        embed.add_field(name=query, value=i, inline=True)
      await ctx.send(embed=embed)





    @commands.command(brief="shows somone qq size ex. .qq @member")
    async def qq(self, ctx, *, person):
      responsessize = [
                '8==>',
                '8===>',
                '8->',
                '8=========>',
                '8==========>',
                '*nothing*'
            ]		    


      res = (f'{secrets.SystemRandom().choice(responsessize)}')
      embed=nextcord.Embed(title="qq size is:", description=person +  ' qq size is ' + res)
      await ctx.send(embed=embed)

    @commands.command(brief='Send random memes')
    async def meme(self, ctx):
      memeApi = urllib.request.urlopen('https://meme-api.herokuapp.com/gimme')
      memeData = json.load(memeApi)
      memeUrl = memeData['url']
      memeName = memeData['title']
      memePoster = memeData['author']

      embed=nextcord.Embed(title=memeName, color=0x4287f5)
      embed.set_image(url=memeUrl)
      embed.set_footer(text=f"Meme By: " + memePoster)
      await ctx.send(embed=embed)

    @commands.command()
    async def dadjoke(self, ctx):
      dadjoke = Dadjoke()
      dj = dadjoke.joke
      dj = profanity.censor(dj)
      await ctx.send(dj)
    
    @commands.command()
    async def complete(self, ctx, rlen, creativity, *, message):
      await ctx.send("Gathering Data")
      context = message
      max_length = abs(int(rlen))
      tempature = int(creativity) / 10
      top_probability = 0.9
      output = ""

      if rlen == 0: rlen = 1

      while round(len(output)/4) < max_length:
        context = context + output

        ml = max_length - round(len(output)/4)

        payload = {
          "context": context,
          "token_max_length": ml,
          "temperature": tempature,
          "top_p": 0.9,
        }

        response = requests.post("http://api.vicgalle.net:5000/generate", params=payload, timeout=60).json(timeout=60)

        temp = response['text']
        tempstring = ""

        for x in range(len(response['text']), 0):
          temp.split(x+40)
          temp = list(dict.fromkeys(temp))

          tempstring = ""
          for y in temp:
            tempstring = tempstring + y
          temp = tempstring

        output = temp

      await ctx.send("Processing response")

      censored = profanity.censor(output)
      output = ""

      for x in censored:
        output = output + x + " "

      output.split(2000)

      for x in output:
        await ctx.send(x)

      


    
    
    
    @commands.command(brief="blur gif")
    async def blurgif(self, ctx, frames, blur_per_frame):
      image = ctx.message.attachments
      image = Image.open(requests.get(image[0], stream=True, timeout=60).raw)
      gif = []
      for x in range(0, int(frames)):
        gif.append(image.filter(ImageFilter.GaussianBlur(radius=int(x)*int(blur_per_frame))))
      image.save('resources/blur_gif.gif', save_all=True, append_images=gif, quality=95)
      await ctx.send(file=nextcord.File('resources/blur_gif.gif'))

def setup(client):
    client.add_cog(games(client))

# this is so long for how little it is lol
#i knoww

