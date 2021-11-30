
import nextcord

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
    async def kick(self, ctx, member: nextcord.Member, *, reason=None):
        await member.kick(reason=reason)


    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: nextcord.Member, *, reason=None):
        await member.ban(reason=reason)


    @commands.command(name="clear",
                      brief="Deletes a certain amount of messages ex. .clear 10")
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=5):
        amount += 1
        await ctx.channel.purge(limit=amount)


    @commands.command(name='support', brief='Gives link to support server')
    async def support(self, ctx):
        await ctx.send('Join our support server https://discord.gg/sz5VkuBGEj')
        embed = nextcord.Embed(
            title="Join our support server!",
            url="https://discord.gg/sz5VkuBGEj",
            description=
            "If you need more help, or have an idea to give us, come join our support community! This is the place where the developers of this bot work and talk! We work our harest to answer questions you may have and consider suggestions! This is the server: https://discord.gg/sz5VkuBGEj",
            color=0x4d7cff)
        await ctx.send(embed=embed)
        await ctx.send('https://discord.gg/sz5VkuBGEj')


    #idk
    #ill check
    #@commands.command()
    #async def admin(ctx, self, role: nextcord.Role, user: nextcord.Member):
    #    await client.add_roles(user, role)


    #i copyed it
    #??
    #coolcode.txt
    #ok
    @commands.command(brief="sends bot invite link")
    async def invite(
        self,
        ctx,
    ):
        await ctx.send(
            "Invite garfy to your oen server here: https://discord.com/api/oauth2/authorize?client_id=880519257107087362&permissions=8&scope=bot"
        )


    @commands.Cog.listener()
    async def on_message(self, message):
      #Blackhole code
      pass


    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def warn(self, ctx, member: nextcord.Member, *, reason='Not Specified'):
        if member == ctx.message.author:
            await ctx.send("You cannot warn yourself")
        else:
            fileread = open("saving/warns.txt", "r")
            data = eval(fileread.read())
            fileread.close()
            guild = ctx.message.guild.id
            guild = str(guild)
            guild = guild[0:18]
            member = str(member)
            if not guild in data:
                data[guild] = {}
                if not member in data[guild]:
                    data[guild][member] = [0, []]
            else:
                if not member in data[guild]:
                    data[guild][member] = [0, []]
            data[guild][member][0] += 1
            data[guild][member][1].append(reason)
            embed = nextcord.Embed(
                title="Warned",
                description=
                f"{member} was warned for {reason}. This is warn #{data[guild][member][0]} for them"
            )
            await ctx.send(embed=embed)
            filewrite = open("saving/warns.txt", "w")
            filewrite.write(str(data))
            filewrite.close()


    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def lock(self, ctx, channel: nextcord.TextChannel = None, setting=None):
        if setting == '--server':
            for channel in ctx.guild.channels:
                await channel.set_permissions(
                    ctx.guild.default_role,
                    reason=f"{ctx.author.name} locked {channel.name} with --server",
                    send_messages=False)
            await ctx.send('locked down server')

        if channel is None:
            channel = ctx.message.channel
        await channel.set_permissions(
            ctx.guild.default_role,
            reason=f"{ctx.author.name} locked {channel.name}",
            send_messages=False)
        await ctx.send('channel locked down')
        await channel.send("This channel has been locked.")


    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def unlock(self,
                    ctx,
                    channel: nextcord.TextChannel = None,
                    setting=None):
        if setting == '--server':
            for channel in ctx.guild.channels:
                await channel.set_permissions(
                    ctx.guild.default_role,
                    reason=f"{ctx.author.name} locked {channel.name} with --server",
                    send_messages=True)
            await ctx.send('unlocked server')

        if channel is None:
            channel = ctx.message.channel
        await channel.set_permissions(
            ctx.guild.default_role,
            reason=f"{ctx.author.name} locked {channel.name}",
            send_messages=True)
        await ctx.send('channel unlocked')
        await channel.send("This channel has been unlocked.")


    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def unmute(self, ctx, member: nextcord.Member):
        for channel in ctx.guild.channels:
            await channel.set_permissions(
                member,
                reason=f"{ctx.author.name} locked {channel.name} with --server",
                send_messages=True)
        await ctx.send(str(member) + " was unmuted")


    @commands.command()
    async def warns(self, ctx, member: nextcord.Member):
        fileread = open("saving/warns.txt", "r")
        data = eval(fileread.read())
        fileread.close()
        guild = ctx.message.guild.id
        guild = str(guild)
        guild = guild[0:18]
        member = str(member)
        if not guild in data:
            data[guild] = {}
            if not member in data[guild]:
                data[guild][member] = [0, []]
        else:
            if not member in data[guild]:
                data[guild][member] = [0, []]

        reasons = ""
        for x in data[guild][member][1]:
            reasons = reasons + str(x) + "\n"
        if reasons == "":
            reasons = reasons + "-"

        embed = nextcord.Embed(
            title=f"Warns for {member}",
            description=f"{member} has {data[guild][member][0]} warns")
        embed.add_field(name="Warn Reasons", value=reasons)
        await ctx.send(embed=embed)


    @commands.command(brief='mutes specified person')
    @commands.has_permissions(manage_messages=True)
    async def mute(self, ctx, member: nextcord.Member, *, reason='None'):
        guild = ctx.guild
        muteRole = nextcord.utils.get(guild.roles, name="GarfyMuted")

        if not muteRole:
            mutedRole = await guild.create_role(name="GarfyMuted")

            for channel in guild.channels:
                await channel.set_permissions(muteRole,
                                              speak=False,
                                              send_messages=False)

        await member.add_roles(muteRole, reason=reason)
        await ctx.send(f'Muted {member} for {reason}')
        await member.send(f"You were muted in {guild.name} for {reason}")





def setup(client):
    client.add_cog(moderation(client))
