import discord
from discord.ext import commands
from passwords import DISCORD_BOT_KEY
import frankbot_rps
import frankbot_google
import frankbot_slotmachine
import frankbot_meme
import frankbot_bitcoin
import frankbot_youtube
import frankbot_avgweight
import random
import os
import png
from random import randint
import pyqrcode
description = "Frankbot"
bot = commands.Bot(command_prefix='%', description=description)
OwnerID = "183457916114698241"
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

@bot.event
async def on_ready():
	print('Logged in as')
	print(bot.user.name)
	print(bot.user.id)

'''bitcoin price'''
@bot.command()
async def bitcoin():
	price = frankbot_bitcoin.getprice()
	await bot.say("{} Current price: **${}**".format("\U0001F4B0", price))

'''youtube search'''
@bot.command()
async def youtube(*, message: str):
	await bot.say(frankbot_youtube.youtube(message))

'''weighted average calculator'''
@bot.command()
async def avg(*, message: str):
	await bot.say("Final average: {0:.2f}".format(frankbot_avgweight.getavg(message)))

'''google search'''
@bot.command(aliases=["Google"])
async def google(*, message: str):
	await bot.say("Top Google result for {}:\n {}".format(message, frankbot_google.google(message)))

@bot.command(pass_context=True)
async def qr(ctx, *, msg):
	qr = pyqrcode.create(msg)
	qr.png('qrcode.png', scale=5)
	await bot.send_file(ctx.message.channel, 'qrcode.png')

'''rock paper scissors game'''
@bot.command(pass_context=True)
async def rps(ctx, choice: str):
	choices = ["rock", "paper", "scissors"]
	if choice in choices:
		await bot.say(frankbot_rps.rps(choice, ctx.message.author.id))
	else:
		await bot.say("Syntax: ?rps <choice : rock, paper, scissors>")

'''coin flip'''
@bot.command(pass_context=True)
async def flipcoin(ctx):
	num = random.randint(0, 1)
	outcomes = ["heads", "tails"]

	msg = "{} The coin landed on **{}**!".format("\U0001F4B0", outcomes[num])
	await bot.say(msg)

'''random meme'''
@bot.command()
async def reddit(message: str=None):
	getpost = frankbot_meme.meme(message)
	await bot.say("**" + getpost[1] + "**" + "\n" + getpost[0])

'''code formatter'''
@bot.command()
async def f(*, message: str):
	await bot.say("```{}```".format(message))

'''8ball'''
@bot.command(aliases=["8ball"])
async def magic8ball(*, message: str):
	outcomes = ["It is certain", "It is decidedly so", "Without a doubt", "Yes, definitely", "You may rely on it",
	"As I see it, yes", "Most likely", "Outlook good", "Yes", "Signs point to yes",
	"Reply hazy, try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again",
	"Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]
	num = random.randint(0, 19)
	await bot.say("{} The magic 8 ball says: *{}*".format("\U0001F3B1", outcomes[num]))

'''B'''
@bot.command()
async def b(*, message: str):
	newmsg = message.replace("b", "\U0001F171").replace("B", "\U0001f171")
	await bot.say(newmsg)

@bot.command(pass_context=True)
async def penislength(ctx, member: discord.Member=None):
	member = member or ctx.message.author
	inches = random.randint(2, 12)
	cm = inches * 2.54
	str = "8" + ("=" * inches) + "D" + " " + "\U0001F4A6" * (inches // 2)

	await bot.say("{}'s penis is **{} inches!** ({} cm)\n{}".format(member.mention, inches, cm, str))
	if inches >= 9:
		await bot.say("\U0001F60D Wow! \U0001F60D")
	elif inches <= 4:
		await bot.say("Ehh \U0001F612")
	else:
		await bot.say("Nice \U0001F609")

'''dice roll'''
@bot.command(aliases=["dice"])
async def rolldice():
	num = random.randint(1, 6)
	await bot.say("{} You rolled a **{}**!".format("\U0001F3B2", num))

'''displays commands'''
@bot.command()
async def commands():
	f = open(os.path.join(__location__, "commands.txt"));
	contents = f.readlines()
	msg = ""
	for i in contents:
		msg = msg + i
	f.close()
	await bot.say(msg)

'''slot machine'''
@bot.command(pass_context=True)
async def slots(ctx):
	slots = frankbot_slotmachine.slotmachine()
	await bot.say("{} {} pulled the slot machine! {}".format("\U0001F3B0", ctx.message.author.mention, slots))

'''admin commands'''
@bot.command(pass_context=True)
async def shutdown(ctx):
	if ctx.message.author.id != OwnerID:
		await bot.say("{} You do not have admin access".format("\U0001F6AB"))
	else:
		await bot.say("Shutting down...")
		await bot.logout()

bot.run(DISCORD_BOT_KEY)
