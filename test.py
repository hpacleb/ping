import aiohttp
from discord.ext import commands

bot = commands.Bot(command_prefix='%')


@bot.event
async def on_ready():
    print('Logged in!')


@bot.command()
async def ping(ctx):
    url = 'https://api.koggames.com/Server/CheckGameStat.ashx'
    async with aiohttp.ClientSession() as session:
        page = await session.get(url)
        data = await page.json()
    if data.get('stats'):
        msg = 'The server is online.'
    else:
        msg = 'The server is offline.'
    await ctx.send(msg)


bot.run('NDc4NDE4OTk1ODE3NzQyMzc1.XL0UTQ.CeIqE5udidsSuFXDR-z9mK1zM48')
