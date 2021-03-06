import discord

from discord.ext import commands
# good job, wg1gem, you have forced me to protect my private tokens
bottoken = open("bottoken", "r").read()
client = commands.Bot(command_prefix="?")



async def joinVC(currentGuild):
    targetChannel = discord.utils.get(currentGuild.voice_channels, name="TASC/W5AC on air")
    voiceClient = discord.utils.get(client.voice_clients, guild=currentGuild)
    if not voiceClient.is_connected:
        await targetChannel.connect()

@client.event
async def on_connect():
    guilds = await client.fetch_guilds(limit=150).flatten()
    for guild in guilds:
        await joinVC(guild)

@client.command()
async def rptjoin(context):
    if context.message.author.id == 733559115577557013:
        await context.send("Starting service...")
        await joinVC(context.guild)
    else:
        await context.send("You don't have permission to do that.")



client.run(bottoken)
