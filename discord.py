import discord
import os


client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = Game("밀크봇")
    await client.change_presence(status=Status.online, activity=game)


@client.event
async def on_message(message):
    if message.content.startswith("안녕"):
        await message.channel.send("할말")
        
        
access_token = os.environ["BOT_TOKEN"]
client.run(acess_token)
                                
