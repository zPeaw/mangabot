import discord
from discord.ext import tasks
import json
import os
import time
import config
from scraper import get_new_items

os.makedirs("data", exist_ok=True)

intents = discord.Intents.default()
client = discord.Client(intents=intents)


# ---------------- FILE HELPERS ----------------
def load_json(path, default):
    if not os.path.exists(path):
        return default
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


# ---------------- SITE CHECK ----------------
@tasks.loop(seconds=config.CHECK_INTERVAL)
async def check_site():
    print("checking site...")

    user = await client.fetch_user(config.USER_ID)

    current = get_new_items()
    if not current:
        return

    known = set(load_json(config.KNOWN_FILE, []))
    new_items = [i for i in current[:5] if i not in known]

    if new_items:
        msg = "NEW ITEMS\n\n" + "\n\n".join(new_items)
        await user.send(msg)

    save_json(config.KNOWN_FILE, current)


# ---------------- CLEANUP ----------------
@tasks.loop(seconds=config.CLEAN_INTERVAL)
async def cleanup_old_messages():
    data = load_json(config.SENT_FILE, {})
    now = int(time.time())
    limit_time = now - 86400

    user = await client.fetch_user(config.USER_ID)
    channel = user.dm_channel or await user.create_dm()

    for mid, ts in list(data.items()):
        if ts < limit_time:
            try:
                msg = await channel.fetch_message(int(mid))
                await msg.delete()
            except:
                pass
            data.pop(mid, None)

    save_json(config.SENT_FILE, data)


@client.event
async def on_ready():
    print(f"bot ready: {client.user}")
    check_site.start()
    cleanup_old_messages.start()
    await check_site()


client.run(config.TOKEN)
