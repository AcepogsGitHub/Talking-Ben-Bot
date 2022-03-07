import os
import random
from discord.ext import commands

bot = commands.Bot(command_prefix="tb!")
token = os.environ['token']

@bot.event
async def on_message(message):
  if message.author != bot.user:
    messages = ["stop it", "ugh", "nah nah nah", "hmm", "shhhh"]
    rand = random.choice(messages)
    print(f"{message.author} said '{message}', bot replied with '{rand}' \n The bot is currently in newspaper mode. \n")
    await message.channel.send(rand)
  

bot.run(token)
