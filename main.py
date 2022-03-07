import discord
import os
import random
import time
from discord.ext import commands
from webserver import start

servers = [{"name": "Talking Ben Bot Server", "id": "949848251752939560", "channel": "950218697665032222"}]

bot = commands.Bot(command_prefix="tb!")
token = os.environ['token']

@bot.event
async def on_connect():
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(bot.guilds)} servers!"))

@bot.command()
async def normal(ctx):
  await ctx.send(f"Loading chatbot...")
  await ctx.send("The chatbot hasn't started since the bot is under maintenance.")
  return
  await ctx.send(":white_check_mark: The bot has loaded its chatbot, try and say something! To stop the chatbot, say `tb!stop_normal`")
  

@bot.command()
async def stop_normal(ctx):
  await ctx.send(":white_check_mark: Stopped the chatbot.")
  os.system('pkill -f talking-chatbot.py')

@bot.command()
async def setup(ctx, channel_id=None):
  for guild in servers:
    for info in guild['name']:
      if ctx.guild.id == guild['id']:
        await ctx.send(f":white_check_mark: This server has already been setup, silly. The channel for the chatbot is {guild['channel']}")
        return
      else:
        if not guild['id'] == ctx.guild.id:
          servers.append({"name": ctx.guild.name, "id": ctx.guild.id, "channel": channel_id})
          await ctx.send(":white_check_mark: Server set up! Now try using the command `tb!normal` in the channel set to start the chatbot!")
          return

@bot.command()
async def verify(ctx):
  em = discord.Embed(title="Verify your Discord account to continue", description="Verify your not a bot by this simple verification. Go to the site supplied below to verify your not a bot and your a real discord user.", color=discord.Colour.gold())
  em.add_field(name="Go to this site:", value="https:// ")

@bot.command()
async def servers(ctx):
  await ctx.send("https://discord.gg/J2caNZHNsg")
  return

@bot.command()
async def eat_beans(ctx):
  msg = await ctx.send("*opens can of beans!*")
  time.sleep(2)
  await msg.edit(content="nom nom nom nom")
  time.sleep(3)
  await msg.edit(content="mmm, tasty! ")

@bot.command()
async def drink_wine(ctx):
  await ctx.send("*drinks wine* ahhh! 🍾")

@bot.command()
async def drink_applejuice(ctx):
  await ctx.send("*drinks apple juice* ahh fruity! 🧃")

@bot.command()
async def poke_ben(ctx):
  poke_opt = ["oooghhh *ben is disapointed :disappointed:*", "ouch! *ben is angry :rage:*"]
  rand = random.choice(poke_opt)
  await ctx.send(rand)

@bot.command(aliases=['chemistry_mode'])
async def experiment_mode(ctx, potion1, operator, potion2):
  if potion1:
    if potion2:
      messages = ["🌋 **Ben made a lava volcanic potion**", "🔥 **Ben made a fire potion**", "💥 **Ben made a explosion potion**", "🥶 **Ben made a freeze potion**", "😵 **Ben made a dizzy potion**"]
      rand = random.choice(messages)
      await ctx.send(rand)

start()
bot.run(token)
