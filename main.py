import discord
import os

TOKEN = os.environ.get("9577")

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Bot is online as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if "memory" in message.content.lower():
        await message.channel.send("A Presence watches silently… 🐍")

client.run(TOKEN)
