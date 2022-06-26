import discord
import os
import random
from keep_alive import keep_alive

client = discord.Client()
triggers = ["Jordan Carter",
            "gaming", 
            "carti", 
            "slime", 
            "b", 
            "fortnite",
            "bictini",
            "slime",
            "slatty"
           ]
quotes = [  "slatt",
            "my slime",
            "carti",
            "BIHHHHH",
            "phew (wind sound)",
            "what!",
            "bee🐝",
            "Cash Carti Bih",
            "wehh",
            "pshhh",
            "BOP",
            "money bags",
            "codeine",
            "lean",
            "hollup",
            "pipe up",
            "glocky",
            "VAMP",
            "PSPHSHPSSHSHPPPHPSHS",
            "Ugh, ohh"
        ]

def get_slime():
  return random.choice(quotes)
  

@client.event
async def on_ready():
  print('logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content
  channel = message.channel

  # slime channel
  if str(channel) == "slime-only":
    rand =  random.randint(0,2)
    if str(message.author) == "jetpack#4027":
      await channel.send("ayy babby girrl watchu doin")
    if str(message.author) == "lorralia#6623":
      await channel.send("ayy babby girrl watchu doin")
    if str(message.author) == "bictini#1986":
      await channel.send("ayy babby girrl watchu doin")
    else:
      await channel.send(message.author)
      #await channel.send(get_slime())
  else: # other channels
    if msg.startswith('$bot'):
      await channel.send("Jordan Carter")
    elif msg.startswith('$channel'):
      await channel.send("channel: " + str(channel))
    elif msg.startswith('$triggers'):
      await channel.send(triggers)
    elif msg.startswith('$quotes'):
      await channel.send(quotes)
    elif msg.startswith('$slime'):
      await channel.send("slatty slatt slatt")
    elif msg.startswith('$b'):
      await channel.send("BIHHHH")
    elif any(word in msg for word in triggers):
      await channel.send(get_slime())


  

keep_alive()
client.run(os.environ['TOKEN'])