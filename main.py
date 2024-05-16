import os
from discord import Intents,Client, Message
from dotenv import load_dotenv
from response import get_response
import discord

#Load discord token
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

#Load quyền
intents = Intents.default()
intents.message_content = True
client = Client(intents=intents)

#Nhắn tin
async def send_message(message, user_message):
    if not user_message:
        print("Message is empty")
        return
    try:
        await message.channel.send(get_response(user_message, message.author))
    except Exception as e:
        print(e)

@client.event
async def on_ready():
    print(f'{client.user} is running')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if client.user.mentioned_in(message) or isinstance(message.channel, discord.DMChannel):
        username = str(message.author)
        user_message = message.content
        channel = message.channel
        print(username, user_message, channel)
        await send_message(message, user_message)

def main():
    client.run(token =TOKEN)

if __name__ == '__main__':
    main()