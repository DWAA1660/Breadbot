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
import requests
import asyncio
import datetime
import time
import requests
import json
import io
from PIL import Image, ImageFilter, ImageOps, ImageDraw
import numpy as np
import secrets

#got it working :D

class image(commands.Cog):
    def __init__(self, client):
        self.client = client
#this is much code wow
#ik lol
    @commands.command()
    async def helpimage(self, ctx):
      embed = nextcord.Embed(title='Image Help', description="The Image commands are commands for manipulating images though discord.", color=0x4287f5)
      embed.add_field(name="**Blur**", value="A command that blurs the attached image.\nSyntax: .blur blur_power")
      embed.add_field(name="**Grayscale**", value="Turns the attached image black and white.\nSyntax: .grayscale")
      embed.add_field(name="**Resize**", value="Resizes the attached image. You can specify the pixel size like:\n.resize 100 100\nOr change the size based on the original size:\n.resize x2 /2")
      embed.add_field(name="**Crop**", value="Crops the attached image. There are 3 ways to crop:\n.crop circle\n.crop square\n.crop oval")
      embed.add_field(name="**Tint**", value="Modifies the rgb of every pixel in the attached image (Tints it).\nSyntax: .tint r g b\nThe r, g, and b are the values you want to increase / decrease all the pixels RGB values by.")
      embed.add_field(name="**Pixelate**", value="Pixelates the attached image.\n Syntax: .pixelate size\nSize is the amount of pixels long and wide you want to image to be.")
      await ctx.send(embed=embed)

    @commands.command(brief="blurs the attached image. Syntax: .blur blur_power")
    async def blur(self, ctx, blur):
      if int(blur) > 100:
        blur = 100
      in_image = ctx.message.attachments
      image = Image.open(requests.get(in_image[0], stream=True, timeout=60).raw)
      out_image = image.filter(ImageFilter.GaussianBlur(radius=int(blur)))
      out_image.save('resources/blur_image.png', quality=95)
      await ctx.send(file=nextcord.File('resources/blur_image.png'))

    @commands.command(brief="grayscales the attached image. Syntax: .grayscale")
    async def grayscale(self, ctx):
      in_image = ctx.message.attachments
      image = Image.open(requests.get(in_image[0], stream=True, timeout=60).raw)
      out_image = ImageOps.grayscale(image)
      out_image.save('resources/grayscale_image.png', quality=95)
      await ctx.send(file=nextcord.File('resources/grayscale_image.png'))

    @commands.command(brief="resize an image")
    async def resize(self, ctx, x, y):
      in_image = ctx.message.attachments
      image = Image.open(requests.get(in_image[0], stream=True, timeout=60).raw)
      if x[0].isnumeric() and y[0].isnumeric():
        out_image = image.resize((int(x), int(y)), Image.LANCZOS)
      elif x[0] == "x" and y[0] == "x":
        out_image = image.resize((round(image.width*float(x[1:])), round(image.height*float(y[1:]))), Image.LANCZOS)
      elif x[0] == "/" and y[0] == "x":
        out_image = image.resize((round(image.width/float(x[1:])), round(image.height*float(y[1:]))), Image.LANCZOS)
      elif x[0] == "x" and y[0] == "/":
        out_image = image.resize((round(image.width*float(x[1:])), round(image.height/float(y[1:]))), Image.LANCZOS)
      elif x[0] == "/" and y[0] == "/":
        out_image = image.resize((round(image.width/float(x[1:])), round(image.height/float(y[1:]))), Image.LANCZOS)
      out_image.save('resources/resize_image.png', quality=95)
      await ctx.send(file=nextcord.File('resources/resize_image.png'))

    @commands.command()
    async def crop(self, ctx, ctype):
      in_image = ctx.message.attachments
      if ctype == "oval":
        in_image = ctx.message.attachments
        img  = Image.open(requests.get(in_image[0], stream=True, timeout=60).raw)
        npImage=np.array(img)
        h,w=img.size
        alpha = Image.new('L', img.size,0)
        draw = ImageDraw.Draw(alpha)
        draw.pieslice([0,0,h,w],0,360,fill=255)
        npAlpha=np.array(alpha)
        npImage=np.dstack((npImage,npAlpha))
        Image.fromarray(npImage).save('resources/crop_image.png')
      elif ctype == "circle":
        img  = Image.open(requests.get(in_image[0], stream=True, timeout=60).raw)
        #crop square
        img_width, img_height = img.size
        img = img.crop(((img_width - min(img.size)) // 2,
          (img_height - min(img.size)) // 2,
          (img_width + min(img.size)) // 2,
          (img_height + min(img.size)) // 2))
        #crop from square to circle
        npImage=np.array(img)
        h,w=img.size
        alpha = Image.new('L', img.size,0)
        draw = ImageDraw.Draw(alpha)
        draw.pieslice([0,0,h,w],0,360,fill=255)
        npAlpha=np.array(alpha)
        npImage=np.dstack((npImage,npAlpha))
        Image.fromarray(npImage).save('resources/crop_image.png')
      elif ctype == "square":
        img  = Image.open(requests.get(in_image[0], stream=True, timeout=60).raw)
        #crop square
        img_width, img_height = img.size
        img = img.crop(((img_width - min(img.size)) // 2,
          (img_height - min(img.size)) // 2,
          (img_width + min(img.size)) // 2,
          (img_height + min(img.size)) // 2))
        img.save('resources/crop_image.png', quality=95)
      await ctx.send(file=nextcord.File('resources/crop_image.png'))

    @commands.command()
    async def tint(self, ctx, r, g, b):
      in_image = ctx.message.attachments
      im  = Image.open(requests.get(in_image[0], stream=True, timeout=60).raw)
      pixels = list(im.getdata())
      width, height = im.size
      pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]
      increase = (int(r), int(g), int(b))
      pixlist = []
      for x in range(0, len(pixels)):
        for y in range(0, len(pixels[x])):
          pixlist = list(pixels[x][y])
          pixlist[0] += increase[0]
          pixlist[1] += increase[1]
          pixlist[2] += increase[2]
          if pixlist[0] > 255:
            pixlist[0] = 255
          elif pixlist[0] < 0:
            pixlist[0] = 0
          if pixlist[1] > 255:
            pixlist[1] = 255
          elif pixlist[1] < 0:
            pixlist[1] = 0
          if pixlist[2] > 255:
            pixlist[2] = 255
          elif pixlist[2] < 0:
            pixlist[2] = 0
          pixels[x][y] = (pixlist[0], pixlist[1], pixlist[2])
      data = np.array(pixels, dtype=np.uint8)
      new_image = Image.fromarray(data)
      new_image.save('resources/tint_image.png', quality=95)
      await ctx.send(file=nextcord.File('resources/tint_image.png'))

    @commands.command()
    async def pixelate(self, ctx, pixelate_size):
      pixelate_size = int(pixelate_size)
      in_image = ctx.message.attachments
      img = Image.open(requests.get(in_image[0], stream=True, timeout=60).raw)
      if pixelate_size > img.size[0]*2:
        pixelate_size = img.size[0]*2
      imgSmall = img.resize((pixelate_size,pixelate_size),resample=Image.BILINEAR)
      result = imgSmall.resize(img.size,Image.NEAREST)
      result.save('resources/pixilate_image.png')
      await ctx.send(file=nextcord.File('resources/pixilate_image.png'))

    @commands.command()
    async def distort(self, ctx, power):
      in_image = ctx.message.attachments
      image = Image.open(requests.get(in_image[0], stream=True, timeout=60).raw)

      power = abs(int(power))

      pixels = list(image.getdata())
      width, height = image.size
      pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]

      for x in range(0, len(pixels)):
        for y in range(0, len(pixels[x])):
          swap_x = secrets.SystemRandom().randint(0, power)
          swap_y = secrets.SystemRandom().randint(0, power)

          pixel_save = pixels[x][y]
          pixels[x][y] = pixels[swap_x][swap_y]
          pixels[swap_x][swap_y] = pixel_save

      data = np.array(pixels, dtype=np.uint8)
      new_image = Image.fromarray(data)
      new_image.save('resources/distort_image.png', quality=95)
      await ctx.send(file=nextcord.File('resources/distort_image.png'))



def setup(client):
    client.add_cog(image(client))

