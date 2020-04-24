import os

import discord
from dotenv import load_dotenv
from modules.all import *

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

@client.event
async def on_message(message):
    print("{}: {}: {}: {}".format(message.channel, message.author, message.author.name, message.content))

    if (message.content.startswith("sup")):
        # output the message 
        await message.channel.send("What it do baby!!")
    
    if (message.content.startswith("date")):
        response = currentDate()
        await message.channel.send(response)

    if (message.content.startswith("time")):
        response = currentTime()
        await message.channel.send(response)

    if (message.content.startswith("weather")):
        response = currentWeather()
        await message.channel.send(response)


client.run(TOKEN)