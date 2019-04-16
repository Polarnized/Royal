import discord
import asyncio
import random
import json
import datetime
import random
import requests as req
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get

bot = commands.Bot(command_prefix='.')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    await bot.change_presence(game=discord.Game(name='Scims | .rules'))






@bot.command(pass_context=True)
async def commands():
        embed = discord.Embed(title="Royal Scrims Commands", description="These are all the commands for this bot", color=0xffc801)
        embed.set_thumbnail(url='https://media.discordapp.net/attachments/546539833980616717/547977666620293132/A.png?width=1274&height=1262')
        embed.set_footer(text="Created by Polarnized#5536 CODE-POLAR", icon_url='https://media.discordapp.net/attachments/546539833980616717/548001173488140290/SCRIMS_CROPPED.jpg?width=1266&height=1262')
        
        embed.add_field(name="Brackets=Quotation marks", value=".", inline=False)
        embed.add_field(name=":pencil2: .code customcode Zone rule", value="Use when annoucing a custom code.", inline=False)
        embed.add_field(name=":pencil2: .req", value="Annonces a full REQ.", inline=False)
        embed.add_field(name=":pencil2: .anz [Announcement]", value=".anz (Announcement). This command will will send a Announcement.", inline=True)
        embed.add_field(name=":pencil2: .start", value="Announces that the game has been started.", inline=True)
        embed.add_field(name=":pencil2: .rules", value="Shows you all the scrim rules for Royal Scrims.", inline=True)
        embed.add_field(name=":pencil2: .poll option1 option2", value="Will create a poll between 2 things", inline=True)
        embed.add_field(name=":pencil2: .invite", value="Gives a invite link for Royal Scrims", inline=True)
        embed.add_field(name=":pencil2: .commands", value="This will list all the avalible commands for the bot.", inline=True)
        
         
        await bot.say(embed=embed)


@bot.command(pass_context=True)
async def rules():
        embed = discord.Embed(title="Royal Scrims Rules.", description="These are all the scrim rules for the server.<#546211385957416960>", color=0xffc801)
        embed.set_thumbnail(url='https://media.discordapp.net/attachments/546539833980616717/547977666620293132/A.png?width=1274&height=1262')
        embed.set_footer(text="Created by Polarnized#5536 CODE-POLAR", icon_url='https://media.discordapp.net/attachments/546539833980616717/548001173488140290/SCRIMS_CROPPED.jpg?width=1266&height=1262')
        
        embed.add_field(name=":one:", value="Do not kill until FOURTH CIRCLE CLOSES unless told otherwise, doing so will result in a ban.", inline=False)
        embed.add_field(name=":two:", value="Do not storm push.", inline=False)
        embed.add_field(name=":three:", value="Play smart and play for end game.", inline=True)
        embed.add_field(name=":four:", value="Only use planes for rotating", inline=False)
        embed.add_field(name=":five:", value="Do not follow other players.", inline=True)
        embed.add_field(name=":six:", value="Dont land polar peak (expect to get killed)", inline=False)
        embed.add_field(name="Break rules = Warning", value="**3 warnings = Ban**", inline=False)
         
        sg = await bot.say(embed=embed)
        await bot.add_reaction(sg, "\u2665")











@bot.command(pass_context=True)
async def code(ctx, skin, zone, mode):
    embed=discord.Embed(title='__New custom code posted!__', color=0x00ff00)
    author = ctx.message.author.mention
    embed.set_author(name='ROYAL SCRIMS', icon_url="https://cdn.discordapp.com/attachments/546539833980616717/548001173488140290/SCRIMS_CROPPED.jpg")
    embed.add_field(name='Host:', value=author + '  ', inline=True)
    embed.add_field(name='CODE:', value='**' + skin + '**', inline=False)
    embed.add_field(name='Zone Rule:', value='**' + zone + '**', inline=True)
    embed.add_field(name='Mode:', value='**' + mode + '**', inline=True)
    embed.set_footer(text="React with❤️if you're queued.")

   
    

    white_listed_channel = ["547405178068926507"] 
  
    if ctx.message.channel.id not in white_listed_channel: 
        x=await bot.say(f"{author} , You can't use this command here!:x:")
        await asyncio.sleep(3)
        await bot.delete_message(x)
        return
    
    await bot.say("Your code has been posted in <#546211531109695498>")
    sg = await bot.send_message(bot.get_channel('546211531109695498'), embed=embed)
    await bot.add_reaction(sg, "\u2665")
    await bot.send_message(bot.get_channel('546211531109695498'), '@everyone')
 
    
    
        
 
  


    

@bot.command(pass_context=True)
async def req(ctx):
    author = ctx.message.author.mention

    white_listed_channel = ["547405178068926507"] 
  
    if ctx.message.channel.id not in white_listed_channel:
        x=await bot.say(f"{author} , You can't use this command here!:x:")
        await asyncio.sleep(3)
        await bot.delete_message(x)
        return 
  

    embed=discord.Embed(title='', color=0x00ff00)
    embed.add_field(name='REQ Request', value='A REQ request has been sent!', inline=False)
    embed.set_footer(text="Created by Polarnized#5536 CODE-POLAR", icon_url="https://media.discordapp.net/attachments/546539833980616717/548001173488140290/SCRIMS_CROPPED.jpg?width=1266&height=1262")
    await bot.say(embed=embed)


    embed=discord.Embed(title='', color=0xff0011)
    embed.add_field(name=':x:FULL REQ:x:', value='**Back out of your game and look for the new code!**', inline=False)
    embed.set_footer(text="Created by Polarnized#5536 CODE-POLAR", icon_url="https://media.discordapp.net/attachments/546539833980616717/548001173488140290/SCRIMS_CROPPED.jpg?width=1266&height=1262")

    await bot.send_message(bot.get_channel('546211531109695498'), '@everyone')    #need to update these numbers to right channel
    await bot.send_message(bot.get_channel('546211531109695498'), embed=embed)




@bot.command(pass_context=True)
async def anz(ctx, skin):
    embed=discord.Embed(title='**:loudspeaker:New Announcement**:loudspeaker:', color=0xfffa00)
    author = ctx.message.author.mention
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/546539833980616717/547977637797298177/B.png')
    embed.add_field(name='Announced By:', value=author + '  ', inline=True)
    embed.add_field(name='Announcement:', value='**' + skin + '**', inline=False)           #need to update all this info
    embed.set_footer(text="Created by Polarnized#5536 CODE-POLAR")

    white_listed_channel = ["547405178068926507"] 
  
    if ctx.message.channel.id not in white_listed_channel: 
        x=await bot.say(f"{author} , You can't use this command here!:x:")
        await asyncio.sleep(3)
        await bot.delete_message(x)
        return 
    
    await bot.say("Your Announcement has been posted in <#546211531109695498>")
    await bot.send_message(bot.get_channel('546211531109695498'), embed=embed)
    await bot.send_message(bot.get_channel('546211531109695498'), '@everyone')


    

@bot.command(pass_context=True)
async def start(ctx):
    author = ctx.message.author.mention

    white_listed_channel = ["547405178068926507"] 
  
    if ctx.message.channel.id not in white_listed_channel:
        x=await bot.say(f"{author} , You can't use this command here!:x:")
        await asyncio.sleep(3)
        await bot.delete_message(x)
        return 
  

    embed=discord.Embed(title='', color=0x007bff)
    embed.add_field(name='Game Start', value='Game Start has been posted!', inline=False)
    await bot.say(embed=embed)


    embed=discord.Embed(title='', color=0x007bff)
    embed.add_field(name=':white_check_mark:Game Started:white_check_mark:', value='**Custom match has been Started! Another code will be posted in 30min.**', inline=False)
        
    await bot.send_message(bot.get_channel('546211531109695498'), embed=embed)
    await bot.send_message(bot.get_channel('546211531109695498'), '@here')


    
@bot.command(pass_context=True)
async def support(ctx):
    author = ctx.message.author.mention

    white_listed_channel = ["562434407231782918"] 
  
    if ctx.message.channel.id not in white_listed_channel:
        x=await bot.say(f"{author} , You can't use this command here!:x:")
        await asyncio.sleep(3)
        await bot.delete_message(x)
        return 
  

    embed=discord.Embed(title='', color=0xf4ff19)
    embed.add_field(name='Support Request', value='A new support request has been sent! They will get back to you shortly!', inline=False)
    embed.set_footer(text="Created by Polarnized#5536 CODE-POLAR", icon_url="https://media.discordapp.net/attachments/546539833980616717/548001173488140290/SCRIMS_CROPPED.jpg?width=1266&height=1262")
    await bot.say(embed=embed)


    embed=discord.Embed(title='', color=0xf4ff19)
    embed.add_field(name='Support Request', value=author + ' is in need of help!', inline=False)
    embed.set_footer(text="Created by Polarnized#5536 CODE-POLAR", icon_url="https://media.discordapp.net/attachments/546539833980616717/548001173488140290/SCRIMS_CROPPED.jpg?width=1266&height=1262")

    await bot.send_message(bot.get_channel('562435049224404998'), '@here')    #need to update these numbers to right channel
    await bot.send_message(bot.get_channel('562435049224404998'), embed=embed)
    


@bot.command(pass_context=True)
async def poll(ctx, skin, zone):
    embed=discord.Embed(title='Royal Scrims Poll', color=0xfcfcff)
    author = ctx.message.author.mention
    embed.set_author(name='ROYAL SCRIMS', icon_url="https://cdn.discordapp.com/attachments/546539833980616717/548001173488140290/SCRIMS_CROPPED.jpg")
    embed.add_field(name="Options:", value="@everyone", inline=True)
    embed.add_field(name='Option 1:', value='**' + skin + '**', inline=False)
    embed.add_field(name='Option 2:', value='**' + zone + '**', inline=True)
  

   
    

    white_listed_channel = ["547405178068926507"] 
  
    if ctx.message.channel.id not in white_listed_channel: 
        x=await bot.say(f"{author} , You can't use this command here!:x:")
        await asyncio.sleep(3)
        await bot.delete_message(x)
        return
    
    await bot.say("Your poll has been posted in <#546211531109695498>")
    sg = await bot.send_message(bot.get_channel('546211531109695498'), embed=embed)
    await bot.add_reaction(sg, "\u0031\u20e3")
    await bot.add_reaction(sg, "\u0032\u20e3")






async def invite(ctx):
    author = ctx.message.author.mention
    white_listed_channel = ["546217836490522634","546211421202153482"]
  
    if ctx.message.channel.id not in white_listed_channel:
        x=await bot.say(f"{author} , You can't use this command here!:x:")
        await asyncio.sleep(3)
        await bot.delete_message(x)
        return 
    await bot.say('https://discord.gg/8FqMwDs')
    await ctx.messeage.add_reaction(emoji="❤")




    


bot.run('NTQ3Mzk5MDc1MTIxNzI1NDUw.D0_vdg.-Fom53_7HwXeqpeJrVj7DCNxUj8')
