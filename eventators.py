@bot.event
async def on_message(message):
  pass
  for guild in servers:
    for server in guild:
      if message.author != bot.user:
        if message.guild.id == server['id']:
          if message.channel.id == server['channel']:
            messages = ["no", "yes", "ugh", "hohoho", "hahaha", "*grunts*"]
            rand = random.choice(messages)
            print(f"{message.author} said '{message}', bot replied with '{rand}' \n \n")
            await message.channel.send(rand)
