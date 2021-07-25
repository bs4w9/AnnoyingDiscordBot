import os
import discord

client = discord.Client() 

botToken = os.environ['1']

@client.event
async def on_ready():

  print('Bot is logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith('$hello'):
    await message.channel.send('Hello!')

client.run(botToken)
