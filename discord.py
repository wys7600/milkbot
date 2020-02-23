import discord


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


client.run("NjgwMDM4NTMxMjIxMDI4ODc2.XlIJ9Q.LaA6jNKHG04HG8COHNf5hm9AeTY")
                                
