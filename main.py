import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
import datetime

TOKEN = "ODcxMDcwODgwMDQ5MDE2ODUy.YQV9-Q.VPO0jNk7NC7TZTY9tPpHgAt_YkE"
BOT_ID = "871070880049016852"

#SERVER_ID = "236193481238773760"

#client = discord.Client()
client = commands.Bot(command_prefix = '!')

@client.event
async def on_reaction_add(reaction,user):
    channel = reaction.message.channel
    await channel.send('{} has added {} to the message {}'.format(user.name,reaction.emoji,reaction.message.content))



@client.command(name='chess')
async def launch_game(ctx):
    await ctx.channel.send('la partie va start bg le sang de la veine')


@client.command(pass_context=True)
async def join(ctx, meme):
    channel = ctx.message.author.voice.channel
    voice = await channel.connect()
    if meme=='valaba':
        source = FFmpegPCMAudio('valaba.mp3')
    player = voice.play(source)

@client.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.server
    voice_client = client.voice_clients_in(server)
    await voice_client.disconnect()



    
client.run(TOKEN)

