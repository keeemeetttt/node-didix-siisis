import config
from multiprocessing import Lock
import os
import psutil
from telnetlib import STATUS
from sys import prefix
import discord
from discord.ext import commands
from discord.ext import commands
import discord
from discord_buttons_plugin import *
import requests, json, threading, requests, json, validators
import requests, time, os
from os import system
from typing_extensions import Required
import discord
from discord import client
from discord.utils import get
import gratient
from concurrent.futures import ThreadPoolExecutor 
from re import search
from time import sleep
import requests
from discord import embeds
from datetime import datetime
from discord import message
from discord.ext import commands
from discord.ext.commands.core import command, has_role
from requests import post, Session
from re import search
from random import choice
from string import ascii_uppercase, digits
from concurrent.futures import ThreadPoolExecutor
from discord.ext import commands
from json import loads, dumps, load
from discord.ext import commands
from datetime import datetime
from humanize import intcomma



blacklist = [
"0937345272",
"1669",
"",
]
 

bot = commands.Bot(command_prefix=config.Bot_prefix)
bot.remove_command("help")

def randomString(N):
    return ''.join(choice(ascii_uppercase + digits) for _ in range(N))

threading = ThreadPoolExecutor(max_workers=int(100000000))
useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.40"
header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"}


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
       msg = '**เพื่อป้องกันการสแปม**, กรุณาลองใหม่ในอีก {:.2f}วินาที',format(error.retry_after)
       await ctx.send(msg)




@bot.event
async def on_ready():
    print(gratient.red(f"login as {bot.user}"))
    system('title ' + (f"{bot.user}"))


def randomString(N):
    return ''.join(choice(ascii_uppercase + digits) for _ in range(N))

threading = ThreadPoolExecutor(max_workers=int(100000000))
useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.40"


    
 
    
def startall(phone, amount):
    for x in range(amount):
        
        
        
        threading.submit(config.cang01,phone)
        threading.submit(config.cang02,phone)
        threading.submit(config.cang03,phone)
        threading.submit(config.cang1,phone)
        threading.submit(config.cang2,phone)
        threading.submit(config.cang3,phone)
        threading.submit(config.cang3,phone)
        threading.submit(config.cang4,phone)
        threading.submit(config.cang5,phone)
        threading.submit(config.cang6,phone)
        threading.submit(config.cang7,phone)
        threading.submit(config.cang8,phone)
        threading.submit(config.cang9,phone)
        threading.submit(config.cang10,phone)
        threading.submit(config.cang11,phone)
        threading.submit(config.cang12,phone)
        threading.submit(config.cang13,phone)
        threading.submit(config.cang14,phone)
        threading.submit(config.cang15,phone)
        threading.submit(config.cang16,phone)
        threading.submit(config.cang17,phone)
        threading.submit(config.cang18,phone)
        threading.submit(config.cang19,phone)
        threading.submit(config.cang20,phone)        
        threading.submit(config.cang21,phone)
        threading.submit(config.cang22,phone)
        threading.submit(config.cang23,phone)
        threading.submit(config.cang24,phone)


@bot.event
async def on_command_error(ctx, error):
    print(str(error))

@bot.event
async def on_ready():
   await bot.change_presence(activity = discord.Streaming(name =f"{config.Bot_STATS}", url = "https://twitch.tv/Kamuisad")) #สเตตัสสีม่วง
   print(gratient.purple(f"    Login as : {bot.user.name}#{bot.user.discriminator}"))
   print(f'เซิฟเวอร์ที่บอทอยู่ {len(bot.guilds)} servers!')
   





@bot.command()
async def stats(ctx):
    bedem = discord.Embed(title = 'CPUและRAMที่ใช้ไป', description = 'นี่คือCPUและRAMที่ใช้ไป|by:KAMUI SHOP')
    bedem.add_field(name = 'CPU ที่ใช้ไป', value = f'{psutil.cpu_percent()}%', inline = False)
    bedem.add_field(name = 'หน่วยความจำที่ใช้ไป', value = f'{psutil.virtual_memory().percent}%', inline = False)
    bedem.add_field(name = 'หน่วยความจำที่เหลืออยู่', value = f'{psutil.virtual_memory().available * 100 / psutil.virtual_memory().total}%', inline = False)
    await ctx.send(embed = bedem)
    await ctx.message.delete()



@bot.command()
async def help(ctx):
    embed = discord.Embed
    await ctx.send(f"** คำสั่งยิงเบอร์ | {config.Bot_prefix}sms [เบอร์] [จำนวน0- {str(config.Bot_MAXLIMIT)}] รอบ **", delete_after=1000000)
    await ctx.send(embed= embed)



@bot.command()
@commands.cooldown(2,30,commands.BucketType.user)
async def sms(ctx, phone=None, amount=None):
    if (str(ctx.message.channel.id) == f"{config.Bot_LOCK}"):
        if (phone == None or amount == None):
            embed=discord.Embed( description="```#กรุณาใส่ข้อมูลให้ครบถ้วน#```", color=0x00ff00, timestamp=datetime.utcnow())
            embed.set_thumbnail(url= f"{config.Bot_IMAGE1}")
            await ctx.send(embed=embed,)
            
        else:
            if (phone not in blacklist):
                try:
                    amount = int(amount)
                    if (amount > config.Bot_MAXLIMIT):
                        embed=discord.Embed( description=f":alarm_clock: : ใส่ไม่เกิน {config.MAXLIMIT} รอบ.", color=0x00ff00, timestamp=datetime.utcnow())
                        embed.set_thumbnail(url= f"{config.IMAGE1}")
                        await ctx.send(embed=embed,)
                        

                    else:
                        embed=discord.Embed( description=f"\n```เบอร์ {phone}```  \n```จำนวน {amount}/{config.Bot_MAXLIMIT}รอบ``` \n```1รอบ=10ข้อความนะไอ้สัส``` ", color=0x00ff00, timestamp=datetime.utcnow())
                        embed.set_image(url= f"{config.Bot_IMAGE2}")
                        embed.set_footer(text=f"สั่งยิงโดย {ctx.author}")
                        await ctx.send(embed=embed,)
                        startall(phone, amount)
                        

                except:
                    embed=discord.Embed( description=":clipboard: : ใส่เบอร์คนที่จะยิงให้ถูก. ", color=0x00ff00, timestamp=datetime.utcnow())
                    embed.set_thumbnail(url= f"{config.Bot_IMAGE1}")
                    await ctx.message.delete()
                    await ctx.send(embed=embed,delete_after=10)

            else:
                embed=discord.Embed( description=f":face_with_symbols_over_mouth: : ไม่อนุญาติให้ยิงเบอร์นี้ : :face_with_symbols_over_mouth: ", color=0x00ff00, timestamp=datetime.utcnow())          
                await ctx.send(embed=embed,)
                await ctx.message.delete()

    else:
        embed=discord.Embed( description="#ยิงให้ถูกห้องด้วยนะคับ. ", color=0x00ff00, timestamp=datetime.utcnow())
        embed.set_thumbnail(url= f"{config.Bot_IMAGE1}")
        await ctx.send(embed=embed,)
        await ctx.message.delete()


bot.run(config.Bot_token, reconnect=True)