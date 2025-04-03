import discord
from discord.ext import commands

async def kick_user(ctx, user: discord.User):
    if ctx.author.guild_permissions.kick_members:
        await ctx.guild.kick(user)
        await ctx.send(f'User {user} has been kicked.')
    else:
        await ctx.send('You do not have permission to kick members.')

async def ban_user(ctx, user: discord.User):
    if ctx.author.guild_permissions.ban_members:
        await ctx.guild.ban(user)
        await ctx.send(f'User {user} has been banned.')
    else:
        await ctx.send('You do not have permission to ban members.')

def setup(bot: commands.Bot):
    bot.add_command(commands.Command(kick_user, name='rm'))
    bot.add_command(commands.Command(ban_user, name='rm -r'))