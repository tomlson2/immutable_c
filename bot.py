import discord
from discord.ext import commands

class ChannelData:
    def __init__(self, channel_id, channel_name, guild_id):
        self.channel_id = channel_id
        self.channel_name = channel_name
        self.guild_id = guild_id

class MessageData:
    def __init__(self, author, content, channel):
        self.author = author
        self.content = content
        self.channel = channel

channel_data_list = []
message_data_list = []

@client.event
async def on_ready():
    for guild in client.guilds:
        for channel in guild.text_channels:
            new_channel_data = ChannelData(channel_id=channel.id, channel_name=channel.name, guild_id=guild.id)
            channel_data_list.append(new_channel_data)
    print('Bot is ready.')

message_data_buffer = []

@client.event
async def on_message(message):
    new_message_data = MessageData(author=message.author, content=message.content, channel=message.channel)
    message_data_buffer.append(new_message_data)

async def process_message_buffer():
    while True:
        if len(message_data_buffer) > 0:
            batch = message_data_buffer[:50]
            message_data_buffer = message_data_buffer[50:]
            # Send the batch of messages to the blockchain here
        await asyncio.sleep(1)

# Start the buffer processing loop
client.loop.create_task(process_message_buffer())