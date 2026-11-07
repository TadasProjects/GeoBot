import discord
from dotenv import load_dotenv
import os

def configure():
    load_dotenv()

configure()

class Client(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!') # Shows when the bot is logged in


# This tells discord what events the bot wants too use, "privileges"
intents = discord.Intents.default()
intents.message_content = True


client = Client(intents=intents) # build the bot with the description we set up
client.run(os.getenv('discord_token'))