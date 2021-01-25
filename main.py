import discord
import random
import os
from discord.ext import commands

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.Member, *, reason=None):
  await user.ban(reason=reason)
  await ctx.send(f"{user} have been bannned sucessfully")

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('!wixent'):
    await message.channel.send('a')
  if message.content.startswith('hola'):
    await message.channel.send('tu naris contra mis bolas')
  if message.content.startswith('!nigger'):
    await message.channel.send('eres '+str(random.randint(1,101))+'% nigger')


client.run(os.getenv('TOKEN'))