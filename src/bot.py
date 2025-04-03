import discord
from discord.ext import commands
from commands.moderation import kick_user, ban_user

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

bot.run('YOUR_BOT_TOKEN')  # Replace with your bot token