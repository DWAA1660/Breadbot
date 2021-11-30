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
from PIL import Image, ImageDraw
import math

class Mesh(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def makemesh(self, ctx):
      file = open("saving/mesh.txt", "r")
      filedata = file.read()
      filedata[str(ctx.message.author)] = []
      await ctx.send("Mesh save wiped")

    @commands.command()
    async def meshcube(self, ctx, x1, y1, z1, x2, y2, z2):
      #Rotation Point Function
      def rotate(origin, point, angle):
        ox, oy = origin
        px, py = point
        qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
        qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
        return qx, qy

      #Convert Coords Function
      def coords_convert(x, y):
        x = x + 250
        y = 0 - y
        y = y + 250
        return (x, y)

      #Draw Line Function
      def line3d(x1, y1, z1, x2, y2, z2):
        x1z1 = rotate((0, 0), (x1, z1), angle)
        x2z2 = rotate((0, 0), (x2, z2), angle)
        x1 = x1z1[0]
        z1 = x1z1[1]
        x2 = x2z2[0]
        z2 = x2z2[1]

        y1 -= 250
        y2 -= 250

        z1 -= 500
        z2 -= 500

        x1 = x1 * (focal / z1)
        y1 = y1 * (focal / z1)

        x2 = x2 * (focal / z2)
        y2 = y2 * (focal / z2)

        a = coords_convert(x1, y1)
        b = coords_convert(x2, y2)

        draw.line((a[0], a[1], b[0], b[1]), fill=(0, 0, 0, 255), width=3)

      #Cube Render Function
      def render_cube(meshpoints):
        line3d(meshpoints[0][0], meshpoints[0][1], meshpoints[0][2], meshpoints[1][0], meshpoints[0][1], meshpoints[0][2])
        line3d(meshpoints[1][0], meshpoints[0][1], meshpoints[0][2], meshpoints[1][0], meshpoints[0][1], meshpoints[1][2])
        line3d(meshpoints[1][0], meshpoints[0][1], meshpoints[1][2], meshpoints[0][0], meshpoints[0][1], meshpoints[1][2])
        line3d(meshpoints[0][0], meshpoints[0][1], meshpoints[1][2], meshpoints[0][0], meshpoints[0][1], meshpoints[0][2])

        line3d(meshpoints[0][0], meshpoints[1][1], meshpoints[0][2], meshpoints[1][0], meshpoints[1][1], meshpoints[0][2])
        line3d(meshpoints[1][0], meshpoints[1][1], meshpoints[0][2], meshpoints[1][0], meshpoints[1][1], meshpoints[1][2])
        line3d(meshpoints[1][0], meshpoints[1][1], meshpoints[1][2], meshpoints[0][0], meshpoints[1][1], meshpoints[1][2])
        line3d(meshpoints[0][0], meshpoints[1][1], meshpoints[1][2], meshpoints[0][0], meshpoints[1][1], meshpoints[0][2])

        line3d(meshpoints[0][0], meshpoints[0][1], meshpoints[0][2], meshpoints[0][0], meshpoints[1][1], meshpoints[0][2])
        line3d(meshpoints[1][0], meshpoints[0][1], meshpoints[0][2], meshpoints[1][0], meshpoints[1][1], meshpoints[0][2])
        line3d(meshpoints[1][0], meshpoints[0][1], meshpoints[1][2], meshpoints[1][0], meshpoints[1][1], meshpoints[1][2])
        line3d(meshpoints[0][0], meshpoints[0][1], meshpoints[1][2], meshpoints[0][0], meshpoints[1][1], meshpoints[1][2])
      
      #Code
      x1 = int(x1)
      x2 = int(x2)
      y1 = int(y1)
      y2 = int(y2)
      z1 = int(z1)
      z2 = int(z2)

      meshpoints = [(x1, y1, z1), (x2, y2, z2)]
      
      angle = 0
      focal = -200
      width = 500
      height = 500

      images = []

      img = Image.new(mode = "RGBA", size = (width, height), color=(255, 255, 255, 255))
      draw = ImageDraw.Draw(img)

      await ctx.send("Generating Mesh")

      for x in range(0, 360):
        img = Image.new(mode = "RGBA", size = (width, height), color=(255, 255, 255, 255))
        draw = ImageDraw.Draw(img)
        render_cube(meshpoints)
        angle += 0.1
        images.append(img)

      await ctx.send("Compiling Response")

      img.save('resources/gif/mesh_gif.gif', save_all=True, append_images=images, optimize=False, duration=50)
      await ctx.send(file=nextcord.File('resources/gif/mesh_gif.gif'))



def setup(client): 
    client.add_cog(Mesh(client))
