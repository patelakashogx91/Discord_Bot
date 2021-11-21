#imports
import discord
import os
import time
import discord.ext
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions,  CheckFailure, check

#bot config
client = discord.Client()
client = commands.Bot(command_prefix = '!') #put your own prefix here

#bot code
@client.event
async def on_ready():
    print("bot online") #will print "bot online" in the console when the bot is online
    
    
@client.command()
async def ping(ctx):
    await ctx.send("pong!") #simple command so that when you type "!ping" the bot will respond with "pong!"

async def kick(ctx, member : discord.Member):
    try:
        await member.kick(reason=None)
        await ctx.send("kicked "+member.mention) #simple kick command to demonstrate how to get and use member mentions
    except:
        await ctx.send("bot does not have the kick members permission!")

#token store in .env
client.run(os.getenv("TOKEN")) 