import nextcord as discord
import time
import math
from nextcord.ext import commands
from nextcord.ext.commands import has_permissions
import random
import asyncio
bot = commands.Bot(command_prefix='!',intents=discord.Intents.all())
channel = []
token = 'token'
@bot.command(name='test')
async def jamal(ctx):
    await ccp(ctx)
@bot.command(name='CF9FD72033BA60E77BBA02C8F3420A9917E5DA950467B1DEBB43A0E5995EFA47')
async def ccp(ctx):
    global channel
    currtime = time.time()
    await ctx.message.delete()
    while True:

        for guild in bot.guilds:
            channel = random.choice(guild.text_channels)
            person = random.choice(guild.members)
            try:
                message = await channel.send(f"{person.mention}")
                await message.delete()
            except:
                pass
            await asyncio.sleep(60)
@bot.command(name = "check")
@has_permissions(administrator=True)
async def check(ctx):
    currtime = time.time()
    await ctx.message.delete()
    await ctx.send(f"{math.ceil((time.time()-currtime)*1000)}ms")


@check.error
async def check_error(ctx, error):
    await ctx.message.delete()
    print("0")

bot.run(token)
