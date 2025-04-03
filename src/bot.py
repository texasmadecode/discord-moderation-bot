import discord
from discord.ext import commands
from commands.moderation import kick_user, ban_user
import os  # Import os to read environment variables or file-based tokens

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command(name='rm')
async def remove_user(ctx, user: discord.Member):
    await kick_user(ctx, user)

@bot.command(name='rm_r')
async def remove_user_recursive(ctx, user: discord.Member):
    await ban_user(ctx, user)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')

# Load the token dynamically
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")  # Use environment variable if available
if not DISCORD_TOKEN:
    try:
        from bot import DISCORD_TOKEN  # Fallback to the appended variable in bot.py
    except ImportError:
        print("Error: DISCORD_TOKEN not found. Please run setup.py to configure the token.")
        exit(1)

bot.run(DISCORD_TOKEN)