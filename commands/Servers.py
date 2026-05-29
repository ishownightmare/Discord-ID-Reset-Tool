import discord
from discord.ext import commands
from utils.Logger import log
from utils.Color import Colors

def setup(bot):
    @bot.command()
    async def leave_servers(ctx):
        log(Colors.SERVERS, "[SRVS] Leaving all servers...")
        for guild in ctx.bot.guilds:
            try:
                await guild.leave()
                log(Colors.SERVERS, f"Left server {guild.name}")
            except Exception as e:
                log(Colors.SERVERS, f"Error leaving server {guild.name}: {e}")
