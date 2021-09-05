"""Main module."""
import discord
import os

from dotenv import load_dotenv

class MyClient(discord.Client):
    async def on_ready(self):
        print("Logged on as {0}!".format(self.user))
    
    async def on_message(self, message):
        print("Message from {0.author}: {0.content}".format(message))

load_dotenv()
discord_token = os.getenv("HERALD_TOKEN")
client = MyClient()
client.run(discord_token)