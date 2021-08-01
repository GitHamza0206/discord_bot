import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
import datetime
from jobs import job

TOKEN = "ODcxMDcwODgwMDQ5MDE2ODUy.YQV9-Q.v_WzDutxiKX7C6uCRhqM4yh0TZg"
BOT_ID = "871070880049016852"


#client = discord.Client()
client = commands.Bot(command_prefix = '!')

@client.event
async def on_reaction_add(reaction,user):
    channel = reaction.message.channel
    await channel.send('{} has added {} to the message {}'.format(user.name,reaction.emoji,reaction.message.content))

@client.command(name='info')
async def get_info(ctx):
    id = job.get_account()
    await ctx.channel.send(f'id :  {id}')


@client.command(name='chess')
async def launch_game(ctx):
    name_disc = [222018255210938369, 561297715430948876]
    name_lichess = ['mikoba', 'ryfern21']
    map = dict(zip(name_disc,name_lichess))

    url = job.challenge(map[ctx.message.author.id], rated=False)
    await ctx.channel.send(f'voila lurl les sangs de la veine <3 {url}')


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

