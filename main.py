import discord
from discord.ext import commands
import os
import random
import requests
import string
intents = discord.Intents.default()
intents.message_content = True
images = os.listdir('images')
bot = commands.Bot(command_prefix='$',intents=intents)
@bot.event
async def on_ready():
    print(f'we have loged in as {bot.user}')
@bot.command()
async def mem(ctx):
    img_choose = random.choice(images)
    with open(f'images/{img_choose}','rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

def get_fox_image_ling():
    link = 'https://randomfox.ca/floof/'
    res = requests.get(link)
    info = res.json()
    return info['image']
@bot.command('fox')
async def fox(ctx):
    image_link = get_fox_image_ling()
    await ctx.send(image_link)
    
def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''По команде duck вызывает функцию get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)
bot.run('ТВОЙ ТОКЕН ТУТ')
