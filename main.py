import sys
sys.path.insert(1,'package\Lib\site-packages') #to get all the package
import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('_rate'):
        if message.attachments:
            for attachment in message.attachments:
                if 'image' in attachment.content_type:
                    await message.channel.send("Ada gambar")
                else:
                    await message.channel.send("Gaada gambar artefaknya bang :angry:")
        else:
            await message.channel.send("Gaada gambar artefaknya bang")

client.run(open('token.txt','r').readline())