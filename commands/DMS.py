import discord
from discord.ext import commands
from utils.Logger import log
from utils.Color import Colors

def setup(bot):
    @bot.command()
    async def clear_dms(ctx):
        log(Colors.DMS, "[DMS] Deleting all messages in DMs...")
        for channel in ctx.bot.private_channels:
            if isinstance(channel, discord.DMChannel):
                try:
                    async for msg in channel.history(limit=None):
                        try:
                            await msg.delete()
                            log(Colors.DMS, f"Deleted message in {channel.recipient}")
                        except Exception as e:
                            log(Colors.DMS, f"Error deleting message: {e}")
                except Exception as e:
                    log(Colors.DMS, f"Error accessing DM {channel}: {e}")
