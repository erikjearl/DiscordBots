import discord
import os
import random
import asyncio
from keep_alive import keep_alive
from replit import db

client = discord.Client()
triggers = ["Jordan Carter",
            "gaming", 
            "carti", 
            "slime", 
            "fortnite",
            "bictini",
            "slime",
            "slatt"
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
reactions = [
            "🧛‍♂️",
            "🩸",
            "🅱️",
            "💎",
            "🔫",
            "💵",
            "😈",
            "💀",
            "🔪",
            "💯",
            "❄️"
          ]


def toggle_adlibs(author):
  if 'adlibs' not in db.keys():
    db['adlibs'] = {}
  adlibs = db['adlibs']

  if author in adlibs:
    print("IN")
    adlibs[author] = not adlibs[author]
  else:
    print("OT+UT")
    adlibs[author] = True

  db['adlibs'] = adlibs

    

def get_slime():
  return random.choice(quotes)


def get_jetpack():
  q = [  "ayoo lil Jetpack wanna come out here",
         "king cartii",
         "Pi'erre Bourne",
         "Sir Cartiere"
      ]
  return random.choice(q)

def get_lorralia():
  q = [ "ayoo lorralia wanna come out here"
        "ayy lil mama",
        "wachu doin baby gurrll",
        "hnghhh",
        ">.<",
        "Ⴢ(⇀‸↼‶)⊃━☆ﾟ"
      ]
  return random.choice(q)

def get_bictini():
  q = [ "ayooo bictini wanna come out here"
        "bictini is now playing fortnite",
        "*Take The 'L' Fortnite Emote*",
        "harley quin is bad."
      ]
  return random.choice(q)
  

@client.event
async def on_ready():
  print('logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  global adlibs
  msg = message.content
  channel = message.channel
  author = str(message.author)
  
  # slime channel
  if str(channel) == "slime-only":
    if random.randint(0,2) == 0:
      if author == "jetpack#4027":
        await channel.send(get_jetpack())
      if author == "lorralia#6623":
        await channel.send(get_lorralia())
      if author == "bictini#1986":
        await channel.send(get_bictini())
    else:
      await channel.send(get_slime())
  
  # other channels
  else: 
    if msg.startswith('$help'):
      await channel.send("$bot, $triggers, $quotes, $toggle")
    elif msg.startswith('$bot'):
      await channel.send("Jordan Carter")
    elif msg.startswith('$channel'):
      await channel.send("channel: " + str(channel))
    elif msg.startswith('$author'):
      await channel.send("author: " + author)
    elif msg.startswith('$triggers'):
      await channel.send(triggers)
    elif msg.startswith('$quotes'):
      await channel.send(quotes)
    elif msg.startswith('$toggle'):
      if '[' in msg and ']' in msg:
        author = msg.split('[', 1)[1].split(']')[0]
      toggle_adlibs(author)
      print(str(db['adlibs']))
      await channel.send("adlibs: " + author + " " +
                         str(db['adlibs'].get(author)))
    elif msg.startswith('$slime'):
      await channel.send("slatty slatt slatt")
    elif msg.startswith('$b'):
      await channel.send("BIHHHH")
    else:
      try:
        print("WAIT")
        await client.wait_for('message',timeout=2.1)
      except asyncio.TimeoutError:
        print("TIME UP")
        if any(word in msg for word in triggers):
          for i in range(0,random.randint(0,5)):
            await message.add_reaction(random.choice(reactions))
          await channel.send(get_slime())
        elif author in db['adlibs']:
          if db['adlibs'].get(author):
            for i in range(0,random.randint(0,5)):
              await message.add_reaction(random.choice(reactions))
            await channel.send(get_slime())
      else:
        print("TYPING")
      

  

keep_alive()
client.run(os.environ['TOKEN'])