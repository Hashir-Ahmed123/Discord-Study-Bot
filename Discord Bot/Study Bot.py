import datetime
from discord.ext import commands, tasks
import discord
from dataclasses import dataclass
from googletrans import Translator

#Bot token etc
BOT_TOKEN = "Your Bot Token"
CHANNEL_ID = 1174658782983368755
MAX_SESSION_TIME_MINUTES = 1

@dataclass
class Session:
    is_active: bool = False
    start_time: int = 0 

# Command Prefix
bot = commands.Bot(command_prefix= "!", intents=discord.Intents.all())
session = Session()

# Gives message I'm online
@bot.event
async def on_ready():
    print("Hi! Study bot is online!")
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("Hi! Study bot is online!")


@tasks.loop(minutes=MAX_SESSION_TIME_MINUTES, count=2)
async def break_reminder():
    if break_reminder.current_loop == 0:
        return
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send(f"**Take a break!** You've been studying for {MAX_SESSION_TIME_MINUTES} minutes.")

# ---- Start the Study time ----


@bot.command()
async def start(ctx):
    if session.is_active:
        await ctx.send("A session is already active!")
        return

    session.is_active = True
    session.start_time = ctx.message.created_at.timestamp()
    human_readable_time = ctx.message.created_at.strftime("%H:%M:%S")
    break_reminder.start()
    await ctx.send(f"New session started at {human_readable_time}")

# ---- End the Study time ----

@bot.command()
async def end(ctx):
    if not session.is_active:
        await ctx.send("No session is active!")
        return

    session.is_active = False
    end_time = ctx.message.created_at.timestamp()
    duration = end_time - session.start_time
    human_readable_duration = str(datetime.timedelta(seconds=duration))
    break_reminder.stop()
    await ctx.send(f"Session ended after {human_readable_duration}.")
#______________X_____________X___________X____________

#---- Add -------


@bot.command()
async def Add(ctx, *arr):
    if len(arr) < 2:
        await ctx.send("Please provide at least two or more numbers to add.")
        return

    try:
        result = int(arr[0])
        for i in arr[1:]:
            result += int(i)
        await ctx.send(f"Addition Result: {result}")
    except ValueError:
        await ctx.send("Invalid input. Please provide valid numbers.")
#______________X_____________X___________X____________

#---- Subtract -------


@bot.command()
async def Subtract(ctx, *arr):
    if len(arr) < 2:
        await ctx.send("Please provide at least two or more numbers to subtract.")
        return

    try:
        result = int(arr[0])
        for i in arr[1:]:
            result -= int(i)
        await ctx.send(f"Subtraction Result: {result}")
    except ValueError:
        await ctx.send("Invalid input. Please provide valid numbers.")
#______________X_____________X___________X____________

#---- Multiply -------


@bot.command()
async def Multiply(ctx, *arr):
    if len(arr) < 2:
        await ctx.send("Please provide at least two or more numbers to multiply.")
        return

    try:
        result = int(arr[0])
        for i in arr[1:]:
            result *= int(i)
        await ctx.send(f"Multiplication Result: {result}")
    except ValueError:
        await ctx.send("Invalid input. Please provide valid numbers.")
#______________X_____________X___________X____________

#---- Divide -------


@bot.command()
async def Divide(ctx, *arr):
    if len(arr) < 2:
        await ctx.send("Please provide at least two or more numbers to divide.")
        return

    try:
        result = int(arr[0])
        for i in arr[1:]:
            if int(i) == 0:
                await ctx.send("Cannot divide by zero.")
                return
            result /= int(i)
        await ctx.send(f"Division Result: {result}")
    except ValueError:
        await ctx.send("Invalid input. Please provide valid numbers.")
#______________X_____________X___________X____________


bot.run(BOT_TOKEN)