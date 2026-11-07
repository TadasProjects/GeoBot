# This example requires the 'message_content' intent.

import discord
from discord.ext import tasks
import random
import datetime as dt
import thread_id_file_manager as tim
from zoneinfo import ZoneInfo

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


command_word = "!"
cur_date = dt.datetime.now().date().strftime("%d.%m.%Y")
cur_day = dt.datetime.now().day
GEOGUESSR_CHANNEL_ID = 1568579550244511795
channel = client.fetch_channel(GEOGUESSR_CHANNEL_ID)
cur_date = "09.11.2026"

# CODE TO CREATE THREAD ON COMMAND
@client.event
async def on_message(message):

    if message.content.startswith(command_word + 'geoguessr'):
        try:
            latest_thread_id = tim.read_thread_id()
        except FileNotFoundError:
            thread = await message.channel.create_thread(name=cur_date, type=discord.ChannelType.private_thread)
            await thread.send("First daily Geoguessr game <3")
            latest_thread_id = thread.id
            tim.write_thread_id(thread.id)

        if (await client.fetch_channel(latest_thread_id)).name != cur_date:
            thread = await message.channel.create_thread(name=cur_date, type=discord.ChannelType.private_thread)
            await thread.send("Daily Geoguessr game <3")
            tim.write_thread_id(thread.id)
        else:
            await message.channel.send("The daily Geoguessr game thread has already been made.")


# CODE TO CREATE THREAD AUTOMATICALLY
@tasks.loop(time=dt.time(hour=2, minute=0, tzinfo=ZoneInfo("Europe/Oslo")))
async def daily_geoguessr():
    cur_date = dt.datetime.now(ZoneInfo("Europe/Oslo")).strftime("%d.%m.%Y")

    channel = await client.fetch_channel(GEOGUESSR_CHANNEL_ID)

    thread = await channel.create_thread(
        name=cur_date,
        type=discord.ChannelType.public_thread
    )

    await thread.send("Daily GeoGuessr game <3")
    tim.write_thread_id(thread.id)

@client.event
async def on_ready():
    if not daily_geoguessr.is_running():
        daily_geoguessr.start()

client.run('')
