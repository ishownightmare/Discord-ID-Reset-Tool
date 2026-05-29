import discord
from discord.ext import commands
from utils.Logger import log
from utils.Color import Colors

def setup(bot):
    @bot.command()
    async def clear_friends(ctx):
        log(Colors.FRIENDS, "[FRND] Removing all friends...")
        for friend in ctx.bot.user.friends:
            try:
                await friend.remove_friend()
                log(Colors.FRIENDS, f"Removed {friend}")
            except Exception as e:
                log(Colors.FRIENDS, f"Error removing {friend}: {e}")
