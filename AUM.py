import discord
from discord.ext import commands


TOKEN = 'TOKEN'

client = discord.Client()
bot = commands.Bot(command_prefix="!")

voice_channel_id = VoiceChanel Id

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    else:
        # You can customize the code by specifying channel or person who can mute others
        if message.content == "/mute":
            channel = client.get_channel(voice_channel_id)
            for i in channel.members:
                await i.edit(mute=True)
        elif message.content == "/unmute":
            channel = client.get_channel(voice_channel_id)
            for i in channel.members:
                await i.edit(mute=False)
        else:
            pass

@client.event
async def on_ready():
    print("Ready")


try:
    client.run(TOKEN)
except RuntimeError:
    pass
