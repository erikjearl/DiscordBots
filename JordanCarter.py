import discord
import os
import random
import asyncio
from keep_alive import keep_alive
from replit import db

client = discord.Client()
triggers = ["Jordan Carter",
            "carti",
            "slime",
            "slime",
            "slatt",
            "gaming",
            "fortnite",
            "bictini"
           ]
quotes = [  "ayoo <@&980890353634779268> wanna come out here",
            "slatt",
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
            "Ugh, ohh",
            "my bish, she got cake"
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


def get_jetpack():
  q = [  "ayoo <@196119754786734091> wanna come out here",
         "king cartii",
         "Pi'erre Bourne",
         "Sir Cartiere"
      ]
  return random.choice(q)

def get_lorralia():
  q = [ "ayoo <@574849756363489301> wanna come out here"
        "ayy lil mama",
        "wachu doin baby gurrll",
        "hnghhh",
        ">.<",
        "Ⴢ(⇀‸↼‶)⊃━☆ﾟ"
      ]
  return random.choice(q)

def get_bictini():
  q = [ "ayooo <@354562251039965184> wanna come out here"
        "bictini is now playing fortnite",
        "*Take The 'L' Fortnite Emote*",
        "harley quin is bad."
      ]
  return random.choice(q)
  

@client.event
async def on_ready(): #logon event
  print('logged in as {0.user}'.format(client))


@client.event
async def on_message(message): #message event
  if message.author == client.user:
    return
 
  #vars
  global adlibs
  msg = message.content
  channel = message.channel
  author = str(message.author)
  print("MESSAGE: " + author + " " + str(channel) + "\n\t"+ msg)
  
  #commands
  if msg.startswith('$help'):
    await channel.send("$bot, $triggers, $quotes, $toggle")
    return
  elif msg.startswith('$bot'):
    await channel.send("Jordan Carter: " +
                       str(db['adlibs'].get(author)))
    return
  elif msg.startswith('$channel'):
    await channel.send("channel: " + str(channel))
    return
  elif msg.startswith('$author'):
    await channel.send("author: " + author)
    return
  elif msg.startswith('$triggers'):
    await channel.send(triggers)
    return
  elif msg.startswith('$quotes'):
    await channel.send(quotes)
    return
  elif msg.startswith('$carti'):     #toggle adlibs
    if '[' in msg and ']' in msg:
      author = msg.split('[', 1)[1].split(']')[0]
    toggle_adlibs(author)
    print(str(db['adlibs']))
    await channel.send("adlibs: " + author + " " +
                       str(db['adlibs'].get(author)))
    return
  elif '<@&980554058186244129>' in msg or '<@972279731984662569>' in msg: #check for metntions
    await channel.send("<@%s>"%message.author.id+ " WhAt-WHaa (what?) ")
  elif '<' in msg and '>' in msg and '@' in msg: 
    if msg.find('<@') > -1 and msg.find('<@') < msg.find('>'):
      try:
        mention = str(msg.split('<', 1)[1].split('>')[0])
      except:
        print("no metion found")
      await channel.send('AYOOO <%s>' % mention)
      return
  elif msg.startswith('$slime'):
    await channel.send("slatty slatt slatt")
    return
  elif msg.startswith('$b'):
    await channel.send("BIHHHH")
    return

  # slime channel
  if str(channel) == "slime-only":
    if random.randint(0,2) == 0:
      if author == "jetpack#4027":
        await channel.send(get_jetpack())
        return
      if author == "lorralia#6623":
        await channel.send(get_lorralia())
        return
      if author == "bictini#1986":
        await channel.send(get_bictini())
        return


  # send message & react
  try:
    print("WAIT")
    await client.wait_for('message',timeout=2.1)
  except asyncio.TimeoutError:
    print("TIME UP")
    if any(word in msg for word in triggers):
      await channel.send(random.choice(quotes))
      for i in range(0,random.randint(0,5)):
        await message.add_reaction(random.choice(reactions))
    elif author in db['adlibs']:
      if db['adlibs'].get(author):
        await channel.send(random.choice(quotes))
        for i in range(0,random.randint(0,5)):
          await message.add_reaction(random.choice(reactions))
  else:
    print("NEW MESSAGE")

keep_alive()
client.run(os.environ['TOKEN'])