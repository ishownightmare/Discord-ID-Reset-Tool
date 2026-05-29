import discord
from discord.ext import commands
from utils.Logger import log
from utils.Color import Colors

def setup(bot):
    @bot.command()
    async def leave_groups(ctx):
        log(Colors.GROUPS, "[GRPS] Leaving all groups...")
        for group in ctx.bot.private_channels:
            if isinstance(group, discord.GroupChannel):
                try:
                    await group.leave()
                    log(Colors.GROUPS, f"Left group {group.id}")
                except Exception as e:
                    log(Colors.GROUPS, f"Error leaving group {group.id}: {e}")
