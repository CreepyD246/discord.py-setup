import discord

token = "INSERT TOKEN HERE"

client = discord.Client()

@client.event
async def on_ready():
    print(f"Bot logged in as {client.user}")

@client.event
async def on_message(msg):

    if msg.author != client.user:
        if msg.content.lower().startswith("?hi"):
            await msg.channel.send(f"Hi, {msg.author.display_name}")

client.run(token)
