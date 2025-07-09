from __future__ import print_function
from __future__ import unicode_literals

import discord_buttons_plugin

try:
    import traceback
except:
    try:
        import os

        os.system("python -m pip install traceback")
    except:
        pass
    pass
try:
    import asyncio
    import bs4
    import datetime
    import fnmatch
    import json
    import locale
    import logging
    import math
    import numpy
    import os
    import pickle
    import random
    import re
    import requests
    import signal
    import string
    import sys
    import threading
    import time
    import urllib
    from discord import Spotify
    import spotipy
    from spotipy.oauth2 import SpotifyClientCredentials
    from collections import namedtuple
    from concurrent.futures import ThreadPoolExecutor
    from string import ascii_lowercase
    from typing import List
    from urllib.parse import parse_qs, urlparse
    import discord.user
    import discord_components
    from ahk import AHK
    from bs4 import BeautifulSoup, SoupStrainer
    import colorama
    from colorama import init, Fore, Back, Style
    from dotenv import load_dotenv
    from googleapiclient.discovery import build
    from httplib2 import Http
    from lxml import etree
    from oauth2client import file, client, tools
    from pafy import new
    from vocodes_api import VocodesAPI
    import youtube_dl
    from youtube_dl import YoutubeDL, DownloadError
    import discord
    from discord import FFmpegPCMAudio, HTTPException, NotFound
    from discord.errors import Forbidden, HTTPException, NotFound
    from discord.ext import commands
    from discord_buttons_plugin import *
    from discord.ext.commands import CommandNotFound, Bot
    import Logger
    import spotipy.oauth2 as oauth2
    from os import system, name
    from difflib import SequenceMatcher
    from discord import Status
    from discord import Activity, ActivityType
    from discord import Member
    import psutil
    import textdistance as txtdist
    from PIL import ImageFont, ImageDraw, Image
    import cv2
    from os.path import join, getsize
    import posixpath
    import nest_asyncio
    from pathlib import Path
    import bal
    #import pydub
    #import urllib2
    import imgur_url
    from shutil import copyfile
    from pydub import AudioSegment
    try:
        from http.cookiejar import CookieJar
    except ImportError:
        from cookielib import CookieJar
except ModuleNotFoundError:
    print(ModuleNotFoundError)
    import os
    try:
        import re
    except:
        os.system("python3.9 -m pip install re")
        os.execv(sys.executable, ['python'] + sys.argv)
        SystemExit()
        sys.exit()
    def find_between(s, first, last):
        try:
            start = s.index(first) + len(first)
            end = s.index(last, start)
            return s[start:end]
        except ValueError:
            return ""
    strStr = ModuleNotFoundError
    stringy = find_between(traceback.format_exc(), "\'", "\'")
    print(stringy)
    if stringy == "dotenv":
        try:
            os.system("python -m pip install --upgrade pip")
            os.system("python -m pip install pipwin --compile --no-cache-dir")
            os.system("pipwin install wheel")
        except:
            os.system("python3.9 -m pip install --upgrade pip")
            os.system("python3.9 -m pip install pipwin --compile --no-cache-dir")
            os.system("pipwin install wheel")
            pass
        try:
            os.system("python -m pip install python-" + stringy + " --compile --no-cache-dir")
            os.execv(sys.executable, ['python'] + sys.argv)
            SystemExit()
            sys.exit()
        except:
            os.system("python3.9 -m pip install python-" + stringy + " --compile --no-cache-dir")
            os.execv(sys.executable, ['python'] + sys.argv)
            SystemExit()
            sys.exit()
            pass
    if stringy == "pafy":
        try:
            os.system("python -m pip install youtube_dl")
        except:
            os.system("python3.9 -m pip install youtube_dl --compile --no-cache-dir")
            pass
        try:
            os.system("python -m pip install pafy")
        except:
            os.system("python3.9 -m pip install pafy")
            pass
        os.execv(sys.executable, ['python'] + sys.argv)
        SystemExit()
        sys.exit()
    if stringy == "win32api":
        try:
            os.system("python -m pip install pywin32")
        except:
            os.system("python3.9 -m pip install pywin32")
            pass
        os.execv(sys.executable, ['python'] + sys.argv)
        SystemExit()
        sys.exit()
    if stringy == "googleapiclient":
        try:
            os.system("python -m pip install apiclient --compile --no-cache-dir")
            os.system("python -m pip install --upgrade google-api-python-client --compile --no-cache-dir")
        except:
            os.system("python3.9 -m pip install apiclient --compile --no-cache-dir")
            os.system("python3.9 -m pip install --upgrade google-api-python-client --compile --no-cache-dir")
            pass
        os.execv(sys.executable, ['python'] + sys.argv)
        SystemExit()
        sys.exit()
    try:
        os.system("python -m pip install " + stringy + " --compile --no-cache-dir")
    except:
        os.system("python3.9 -m pip install " + stringy + " --compile --no-cache-dir")
        pass
    try:
        os.system("python -m pip install python-" + stringy + " --compile --no-cache-dir")
    except:
        os.system("python3.9 -m pip install python-" + stringy + " --compile --no-cache-dir")
        pass
    try:
        os.system("python -m pip install " + stringy + "-python --compile --no-cache-dir")
    except:
        os.system("python3.9 -m pip install " + stringy + "-python --compile --no-cache-dir")
        pass
    try:
        os.system("python -m pip install py" + stringy + " --compile --no-cache-dir")
    except:
        os.system("python3.9 -m pip install py" + stringy + " --compile --no-cache-dir")
        pass
    import sys
    os.execv(sys.executable, ['python'] + sys.argv)
    SystemExit()
    sys.exit()
    pass
nest_asyncio.apply()
#load_opus()
init()
quietOut = True
accTimers = False
#potatoesBool = False
potatoesBool = True
devMode = False
samuraibbot = False
#print(potatoesBool, "Potatoes")
sysChannel = None
playingEpoch = []
yt2mp3Array = []



ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'noplaylist': True,
}
ffmpeg_opts = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
HomeDir = 'F:\Tools\_Scripts\!-Python\MuseIT'
VarDir = HomeDir + r'\VariableVariables'
LogDir = HomeDir + r'\Logs'
StaticVarDir = HomeDir + r'\StaticVars'
SoundDir = HomeDir + r'\Sound'
ChromeDir = HomeDir + r'\Chrome'
ScriptDir = HomeDir + r'\SkrippitySkripz'
ImgDir = HomeDir + r'\ImageSearch'
SerbzDir = HomeDir + r'\SerbzDir'




counterButton = 0
with open(HomeDir + "\Saves\TheButtonCounter.txt", "r", encoding="utf8") as f:
    counterButton = f.read()
f.close()
if counterButton == "" or type(counterButton) is type(None):
    counterButton = 0
else:
    counterButton = int(counterButton)




#@bal.error
async def bal_error(self, ctx, error):
    if isinstance(error, discord.errors.NotFound):
        return
    else:
        raise error

####################################################################################
####################################################################################
####################################################################################
async def wrapped_connect(f, bots):
    global Bones, Serbz, BonesChannel, SerbzChannel
    bot = f[0]
    musicBot = bots[0]
    #utilityBot = bots
    Bones = await bot.fetch_user(210914635136630784)
    Serbz = await bot.fetch_user(246892047284436992)
    Serbz2 = await bot.fetch_user(855613733854642237)
    BonesChannel = await Bones.create_dm()
    SerbzChannel = await Serbz.create_dm()
    SerbzChannel2 = await Serbz2.create_dm()
    @bot.event
    async def on_guild_join(guild):
        if musicbotDisable == 0 and bot == musicBot and not devMode:
            print(f"{Fore.RED}J{Fore.LIGHTWHITE_EX}O{Fore.LIGHTCYAN_EX}I{Fore.LIGHTMAGENTA_EX}N"
                  f"{Fore.LIGHTGREEN_EX}E{Fore.LIGHTBLUE_EX}D "
                  f"{Fore.LIGHTYELLOW_EX}G{Fore.LIGHTRED_EX}U{Fore.YELLOW}I{Fore.LIGHTWHITE_EX}"
                  f"L{Fore.LIGHTGREEN_EX}D{Fore.LIGHTYELLOW_EX}!{Fore.LIGHTGREEN_EX}! "
                  f"{Fore.RED}{guild.name}{Fore.LIGHTWHITE_EX}")
            await asyncio.sleep(2)
            for textChan in guild.text_channels:
                if "general" in str(textChan.name).lower() or "bot" in str(textChan.name).lower() \
                    or "commands" in str(textChan.name).lower():
                    loop.create_task(messageHandler(ctx=textChan, lines=[f" @#F Hi! @#V My default command prefix is 1! \n"
                                                              f"You might want to change this!\n"
                                                              f"just simply use the 1!prefix command\n"
                                                              f"(ie. 1!prefix ! would change the prefix to !)\n"
                                                              f"please refer to 1!help if you like as well\n",
                                                              f" @#F Problems? Questions? @#V Feel free to add/message\n"
                                                              f"Serbz#0001 or Serbz#0002, any and all questions and feedback"
                                                              f"are welcome!\n enjoy."], quietMode=2))
                break
        return
    @bot.event
    async def on_guild_remove(guild):
        if musicbotDisable == 0 and bot == musicBot and not devMode:
            print(f"{Fore.RED}L{Fore.LIGHTWHITE_EX}E{Fore.LIGHTCYAN_EX}F{Fore.LIGHTMAGENTA_EX}T "
                  f"{Fore.LIGHTYELLOW_EX}G{Fore.LIGHTRED_EX}U{Fore.YELLOW}I{Fore.LIGHTWHITE_EX}"
                  f"L{Fore.LIGHTGREEN_EX}D{Fore.LIGHTYELLOW_EX}!{Fore.LIGHTGREEN_EX}! "
                  f"{Fore.RED}{guild.name}{Fore.LIGHTWHITE_EX}")
        return
    @bot.event
    async def on_command_error(ctx, error):
        if musicbotDisable == 0 and bot == musicBot:
            global megaArray
            if isinstance(ctx.message.channel, discord.channel.DMChannel):
                return
            if isinstance(error, NotFound):
                return
            quietMode = await getQuietMode(ctx)
            if isinstance(error, CommandNotFound):
                if quietMode is None:
                    loop.create_task(messageHandler(ctx=ctx,
                                     lines=[" @#F Error: @#V command " + str(str(ctx.message.content).split(" ")[0]) + \
                                            f" not found.\nYou can change the command prefix if "
                                            f"need be with {commandPrefix}prefix [NewPrefixHere]"]))
                return
            if isinstance(error, KeyError):
                return
            if isinstance(error, UnboundLocalError):
                return
            if isinstance(error, OSError):
                #await next(ctx)
                return
            var = traceback.format_exc()
            loop.create_task(messageHandler(ctx=ctx, lines=[" @#F Error: @#V " + \
                        f"```{formatString}\n" + str(error) + "```"], system=1))
            return
            #raise error

    @bot.event
    async def on_ready():
        global bots, sysChannel, musicBot
        taskloops = []
        counter = 0
        if bot.user.id == bots[0].user.id:
            sysChannel = await musicBot.fetch_channel(sysChannelID)

            for avariableforabot in bots:
                counter += 1
                taskloops.append(loop.create_task(yourArmyAwaits(avariableforabot)))
            print(f"{Style.RESET_ALL}{Fore.RED}In Guilds:")
            for guild in bot.guilds:
                print(f"{Style.RESET_ALL}{Fore.CYAN}{guild.name}{Style.RESET_ALL}")
        await asyncio.gather(*taskloops)
        return
    async def yourArmyAwaits(avariableforabot):
        global sysChannelID, sysChannel, ready

        print(str(avariableforabot.user.id) + " || " + str(avariableforabot.user.name) + "#" + str(avariableforabot.user.discriminator))
        #if avariableforabot == musicBot:
        ready = 1
        #DiscordComponents(bot, change_discord_methods=True)
        return

    async def setInitNames():
        global musicBot
        for guild in musicBot.guilds:
            await nameHandler(None, clear=1, p_guild=guild)
            await asyncio.sleep(6)
        return
    ###########################################################################

    @bot.event
    async def on_message(message):
        global musicBot, bots, SerbzChannel, BonesChannel
        #if samuraibbot is True and message.channel.guild.id !=
        if ready == 1 and musicbotDisable != 1 and \
                (not message.author.bot or message.author.id == 841794419635781662) \
                and bot == musicBot:
            #####
            if "serb" in message.content or "246892047284436992" in message.content or "855613733854642237" in message.content:
                await SerbzChannel2.send(f"{message.author.name}#{message.author.discriminator}-{message.author.id}\n\n>{message.content}")
            #####

            if isinstance(message.channel, discord.channel.DMChannel):
                if message.author.id == 246892047284436992:
                    if str(message.content.lower())[:1] == "?":
                        prefix = "?"
                        loop.create_task(musicBotCommands(bot,message,prefix))
                print(f"{Style.RESET_ALL}{Fore.YELLOW}" + str(message.author.name) + " DIRECT MESSAGED: " + str(
                    message.content))
                return
            elif not devMode and ((message.channel.guild.id == 859964575310282763 or
                    message.channel.guild.id == 856922937541394482)) and (message.author.id != musicBot.user.id):

                loadedPotatoes = HomeDir + f"\Saves\Sneks\\{message.channel.guild.name}-{message.channel.guild.id}\\"
                try:
                    os.mkdir(HomeDir + f"\Saves\Sneks\\{message.channel.guild.name}-{message.channel.guild.id}")
                except (FileNotFoundError, FileExistsError) as e:
                    pass
                for attachment in message.attachments:
                    image_types = ["png", "jpeg", "gif", "jpg", "mp4", "webm"]
                    for imgtype in image_types:
                        if attachment.filename.lower().endswith(imgtype):
                            filename2 = fr"{attachment.filename.lower()}"
                            await attachment.save(loadedPotatoes + filename2)
                            contX = message.author.name + "#" + message.author.discriminator + "\n" \
                                    + str(message.author.id) + "\n\n>" + message.content + f"\n\n"
                            try:
                                await SerbzChannel.send(file=discord.File(loadedPotatoes + filename2), content=contX+f"{message}")
                                await BonesChannel.send(file=discord.File(loadedPotatoes + filename2), content=contX+f"{message}")
                            except HTTPException:
                                pass
                            print(
                            f"{Style.RESET_ALL}{Fore.LIGHTMAGENTA_EX}Sneky{Fore.RED} SNEKS! {filename2}")
                if "http" in message.content and "discord" in message.content:
                    await SerbzChannel.send(f"{message.author.name}#{message.author.discriminator}\n{message.author.id}"
                                f"\n\n >{message.content} \n\n {message}")
                    await BonesChannel.send(f"{message.content} \n\n {message}")
                    print(f"{Style.RESET_ALL}{Fore.LIGHTMAGENTA_EX}Sneky{Fore.RED} SNEKS! (Discord Attachment Link)")
                    return
            ###########################################################################
            if (str(message.content) != "" and not quietOut) and not devMode: #or message.channel.guild.id == 859964575310282763:
                loop.create_task(printMessage(message))
            prefix = await determine_prefix(bot, message)
            #print(prefix)
            if str(message.content)[:len(prefix)+1] == prefix + " ":
                if len(message.content) > prefix + " ":
                    string2 = f"try {prefix}{str(message.content)[len(prefix)+1:]}"
                await messageHandler(ctx=ctx, lines=[f" @#F Command error: @#V There should never be a space after the command prefix. \n\n"
                    f"{string2}"])
                return
            if bot.user.id == musicBot.user.id and ready == 1 and str(message.content)[:len(prefix)] == prefix:
                if prefix == '':
                    return
                contentCount = 0
                lttrs = await splitword(message.content)
                for each in lttrs:
                    if each != f"{prefix}":
                        contentCount += 1
                if contentCount < 1:
                    return
                loop.create_task(musicBotCommands(bot,message,prefix))
        return

    async def splitword(word):
        return [char for char in word]

    async def printMessage(message):
        try:
            print(str(datetime.datetime.now().strftime(
                f"{Style.RESET_ALL}{Fore.GREEN}%m-%d %H:%M:%S")) + f"{Style.RESET_ALL}{Fore.LIGHTWHITE_EX}||-||{Style.RESET_ALL}{Fore.CYAN}" + str(
                message.guild) + f"--{message.guild.id}"
                  f"{Style.RESET_ALL}{Fore.LIGHTWHITE_EX}||-||{Style.RESET_ALL}{Fore.LIGHTMAGENTA_EX}" + str(
                message.channel) + f"{Style.RESET_ALL}{Fore.LIGHTWHITE_EX}||-||{Style.RESET_ALL}{Fore.YELLOW}" +
                  str(message.author.name) + "#" + str(
                message.author.discriminator) + f"{Style.RESET_ALL}{Fore.LIGHTCYAN_EX}: " + str(
                message.content) + f"{Style.RESET_ALL}")
        except:
            pass
    ###########################################################################
    ###########################################################################
    ###########################################################################
    async def musicBotCommands(bot, message, prefix):
        global bots, musicBot
        bot = musicBot
        #message.content = str(mesage.content).lower()
        loop.create_task(bot.process_commands(message))
        return
    @bot.command(name="button")
    async def discpycomp(ctx):
        global counterButton
        counterButton = int(counterButton) + 1
        with open(HomeDir + f"\Saves\TheButtonCounter.txt", "w") as f:
            f.write(str(counterButton))
        f.close()

        print(f"Initiate Button {counterButton}")
        await buttons.send(
        content = "Here is a button!",
	    channel = ctx.channel.id,
        components = [
            ActionRow([
                Button(
                    label="The Button",
                    # style=ButtonType().Primary,
                    style=random.randint(1, 4),
                    custom_id="btncountfunc"
                )
            ]
            )
        ])
        #@buttons.click
        #async def button_one(ctx):
        #    await messageHandler(ctx=ctx.channel, lines=[f" @#F CONGRAMUFLATIONS!!!!!@@ @#V You clicked a button!!"])
        #    await ctx.reply(content=None, channel=None, tts=False, embed=None, flags=None)
        #    return


        return

    #async def on_button_click(self, interaction):
    #    await interaction.respond(content=f"you clicked button {interaction.component.custom_id}")

    @bot.command(name="i")
    async def invite(ctx):
        if ctx.message.channel == SerbzChannel or ctx.message.channel == SerbzChannel2:
            if "inv" in ctx.message.content.lower():
                servername = str(ctx.message.content).split("inv")[1].strip()
                print(f"{Fore.RED}Serbz DM - inv[1] = {servername}")
                for guild in bot.guilds:
                    print(f"{Fore.LIGHTYELLOW_EX}{guild.name} <----> {Fore.CYAN}{servername}")
                    if servername.lower().strip() in guild.name.lower().strip() or \
                            servername.lower().strip() == guild.name.lower().strip() or \
                            servername.strip() == str(int(guild.id)):
                        print(f"{Fore.RED}{servername}{Fore.LIGHTWHITE_EX} == {Fore.LIGHTGREEN_EX}{guild.name}")
                        for textChan in guild.text_channels:
                            print(f"{Fore.LIGHTCYAN_EX}{textChan.name}")
                            if textChan.permissions_for(
                                    guild.me).create_instant_invite:  # make sure the bot can actually create an invite
                                print(f"{Fore.LIGHTRED_EX}Perms for {Fore.LIGHTGREEN_EX}{textChan.name} valid")
                                invite = None
                                try:
                                    invite = await textChan.create_invite(max_uses=1, unique=True, max_age=900)
                                    print(f"{Fore.LIGHTGREEN_EX}Success for {Fore.LIGHTYELLOW_EX}{invite}")
                                    booly = True
                                except:
                                    print(f"{Fore.LIGHTRED_EX}Failure")
                                    booly = False
                                    pass
                                if booly is True:
                                    try:
                                        Serbz = await bot.fetch_user(int(246892047284436992))
                                        SerbzChannel = await Serbz.create_dm()
                                        loop.create_task(SerbzChannel.send(invite))
                                        print(f"{Fore.LIGHTGREEN_EX}Success for DM")
                                    except:
                                        print(f"{Fore.LIGHTRED_EX}Failed on DM")
                                        if booly is True:
                                            print(invite)
                                        return
                                return
        return

    @bot.command(name="compare")
    async def musicCompareStrings(ctx):
        loop.create_task(compareStrings(ctx))
        return
    @bot.command(name="quiet")
    async def quiet(ctx):
        quietMode = None
        for each in megaArray:
            if each[0][0][0] == ctx.guild.id:
                quietMode = each[2]
                break
        if quietMode is None:
            quietMode = 1
            stringy = "active"
        else:
            quietMode = None
            stringy = "inactive"
        loop.create_task(messageHandler(ctx=ctx,
                lines=[f" @#F Quiet Mode: @#V Toggled - {stringy}"], quietMode=2))
        loop.create_task(arrayBuilder(ctx, quietMode=quietMode))
        return
    @bot.command(name="utilbots")
    async def toggleUtil(ctx):
        global utilbotDisable
        if ctx.message.author.id == 246892047284436992 or ctx.message.author.id == 855613733854642237:
            if utilbotDisable == 0:
                utilbotDisable = 1
            else:
                utilbotDisable = 0
            loop.create_task(messageHandler(ctx=ctx,
            lines=[f" @#F Done: @#V utilbotDisable = {utilbotDisable} "], quietMode=2))
        return
    @bot.command(name="n")
    async def next3(ctx):
        loop.create_task(next(ctx))
        return

    @bot.command(name="r")
    async def remove22(ctx):
        loop.create_task(
            loop.create_task((ctx)))
        return

    @bot.command(name="p")
    async def shorthandplay_p(ctx):
        await play2(ctx)
        return

    @bot.command(name='add')
    async def add(ctx):
        loop.create_task(add2(ctx, nosend="NotNaN"))
        return
    @bot.command(name="stop")
    async def stopf(ctx):
        await stopplaying(ctx, nosend="notNaN")
        await leave(ctx)
        return
    @bot.command(name="skip")
    async def skipf(ctx):
        if len((ctx.message.content).split(" ")) <= 1:
            loop.create_task(next(ctx))
        else:
            loop.create_task(skipto(ctx))
        return
    @bot.command(name="np")
    async def nowplayingf(ctx):
        loop.create_task(nowplayingf(ctx))
        return
    @bot.command(name="playing")
    async def nowplayingf(ctx):
        loop.create_task(nowplayingf(ctx))
        return
    @bot.command(name="nowplaying")
    async def nowplayingf(ctx):
        for each in megaArray:
            if each[0][0][0] == ctx.guild.id:
                songDuration = each[0][7]
                clip2 = each[0][5]
                video_title = each[0][6]
                songNumber = each[0][4]
                if songDuration is None or video_title is None:
                    localVideoData = await referenceDB(clip2, None, None, "load")
                    if localVideoData is not None:
                        songDuration = localVideoData[2]
                        video_title = localVideoData[1]
                    else:
                        video_title, videoDuration = await getVideoTitle(clip2=clip2, returnB="notNone")
                #voice = each[0][0][3]
                #print(str(each[2]))
                break
        if songNumber is not None:
            stringy = str(songNumber)
        else:
            stringy = ""
        commandPrefix = await determine_prefix(bot, ctx.message)
        try:
            songDuration = int(songDuration) - 1
        except:
            songDuration = 0
            pass
        loop.create_task(messageHandler(ctx=ctx, lines=[
            " @#F Now Playing: " +
            f" @#V {stringy}. - [" + str(video_title) + f"]({clip2})",
            f" @#F Duration: @#V {str(lessOrMore(int(math.floor(float(int(songDuration) / 60)))))}:"
            f"{str(lessOrMore(int(math.floor(float(60 * float(r'0.' + str(float(int(songDuration) / 60)).split(r'.')[1][:2]))))))}"
            f" ({commandPrefix}seek 00:00-"
            f"{str(lessOrMore(int(math.floor(float(int(songDuration) / 60)))))}:"
            f"{str(lessOrMore(int(math.floor(float(60 * float(r'0.' + str(float(int(songDuration) / 60)).split(r'.')[1][:2]))))))}"
            f")"]))
        return
    @bot.command(name="a")
    async def shorthandadd2_q(ctx):
        loop.create_task(add2(ctx))
        return

    @bot.command(name="cf")
    async def changeformat(ctx):
        global formatString, megaArray
        if ctx.message.author.id == 246892047284436992 or ctx.message.author.id == 855613733854642237:
            formatString = str(ctx.message.content).split(" ")[1]
        return
    @bot.command(name="fixnames")
    async def fixnames(ctx):
        if ctx.message.author.id == 246892047284436992 or ctx.message.author.id == 855613733854642237:
            await nameHandler(None, clear=1)
        return
    @bot.command(name="cf2")
    async def changeformat2(ctx):
        global megaArray
        lines = []
        if ctx.message.author.id == 246892047284436992 or ctx.message.author.id == 855613733854642237:
            for each in str(ctx.message.content)[5:].split("||"):
                lines.append(each)
            loop.create_task(messageHandler(ctx, lines, quietMode=2))
        return

    @bot.command(name=r"m")
    async def restart(ctx):
        global megaArray, sysChannel
        print(f"{Fore.RED}RESTARTING{Fore.LIGHTWHITE_EX}")
        if ctx.message.author.id == 246892047284436992 or ctx.message.author.id == 855613733854642237:
            loop.create_task(messageHandler(ctx=ctx, lines=["@#F RESTART INITIATED: @#V disconnecting voice clients, setting names. "], system=1))
            #await nameHandler(ctx, clear=1)
            for each in megaArray:
                voiceClient = each[0][0][3]
                print(f"{Fore.MAGENTA}Disconnected voice client in {each[0][0][0]}")
                try:
                    await voiceClient.disconnect()
                except:
                    pass
            #await backupCurrentServerData()
            with open(HomeDir + r"\botToggle.txt", "w", encoding='utf8',
                      errors="ignore") as text_file:
                text_file.write("0")
            text_file.close()
            os.execv(sys.executable, ['python'] + sys.argv)
            SystemExit()
            sys.exit()
        return
    async def backupCurrentServerData():
        tempList = []
        for each in megaArray:
            voiceChan = each[0][0][1].id
            ctxChan = each[0][0][5].id
            startEpoch = None
            seekTime = time.time()
            hours = None
            for f in playingEpoch:
            #    counter += 1
                if f[0] == each[0][0][0]:
                    startEpoch = each[1]
                    break
            seekStamp = []
            if startEpoch is not None:
                hours, rem = divmod(seekTime - startEpoch, 3600)
                minutes, seconds = divmod(rem, 60)
                hours = int(float((hours)))
                minutes = int(float(minutes))
                seconds = int(float(math.floor(seconds)))
                if hours < 10:
                    hours = str("0") + str(int(float(math.floor(hours))))
                if minutes < 10:
                    minutes = str("0") + str(int(float(math.floor(minutes))))
                if seconds < 10:
                    seconds = str("0") + str(int(float(math.floor(seconds))))
                seekStamp.append([hours, rem, minutes, seconds])
            else:
                seekStamp.append([None, None, None, None])
            #for key in each[0]: #vvv suppose I don't need it idk wtf
            tempList.append([each[0][0][0], each[0][0][2], each[0][1], each[0][2],
                            #id int       songNumList     listArray       shuffle #####9       10          11       12
                            each[0][4], each[0][5], each[0][6], each[0][7], each[1], each[2], voiceChan, ctxChan, seekStamp])
                    #current songnum clip2 title duration
        try:
            os.mkdir(HomeDir + f"\Saves\Databases\Temp\{each[0][0][0]}_megaarray")
        except:
            #print(f"{Fore.LIGHTRED_EX}I guess just go f yourself.{Fore.LIGHTWHITE_EX} :)")
            #suppose the file already exists
            pass
        numpy.save(HomeDir + f"\Saves\Databases\Temp\{each[0][0][0]}_megaarray\megarray_tempdata.npy", allow_pickle=True)#brave
        return

    async def loadCurrentServerData(bot):
        global musicBot, megaArray
        folders = []
        megaArrayTempData = []
        for filename in os.listdir(HomeDir + f"\Saves\Databases\Temp\\"):
            folders.append(filename)
        if bot == musicBot:
            for guild in bot.guilds:
                for folder in folders:
                    megaArrayTempData = numpy.load(HomeDir + f"\Saves\Databases\Temp\\" + str(folder)[-1*len("_megaarray"):] + "_megaarray\megarray_tempdata.npy", allow_pickle=True)
                    megaArrayTempData = megaArrayTempData.tolist()
                    guildID = str(folder)[-1*len("_megaarray")]
                    for each in megaArrayTempData:
                        voiceChan = await bot.fetch_channel(each[10])
                        ctxChan = await bot.fetch_channel(each[11])
                        #channel = await getChannel(ctxChan)
                        #
                        video = new(ach[5])
                        audio = video.getbestaudio().url
                        megaArray.append(
                            [[[guildID, voiceChan, each[1], None, None, None], each[2], each[3],
                              audio, # < = audio get
                              each[4], each[5], each[6], each[7]], each[8], each[9]])#fill emup later
                        if each[8] == 1:
                            try:
                                await voiceChan.connect()
                                #for key in each[12]:
                                    #[hours, rem, minutes, seconds]
                                hours = each[12][0]
                                rem = each[12][1]
                                minutes = each[12][2]
                                seconds = each[12][3]
                                #fing figure it out
                            except:
                                pass
                            #var = True

                            #work to be lazy oh no
        return
    @bot.command(name='oauth')
    async def oauth(ctx):
        loop.create_task(messageHandler(ctx=ctx, lines=[" @#F Oauth2 Link: @#V "
                                             "<https://discord.com/api/oauth2/authorize?client_id=866707281122426920&permissions=137543667393&scope=bot>"
                                             f"```{formatString}\nAdd me to your server :) ```"], quietMode=2))
        return
    @bot.command(name="sys")
    async def syssettings(ctx):
        global dbDict

        if ctx.message.author.id == 246892047284436992 or ctx.message.author.id == 855613733854642237:
            message2del = await ctx.send("Please Wait..")
            dbCountT = loop.create_task(countDB(dbDict))
            while dbCountT.done() is not True:
                print(dbCountT)
                await asyncio.sleep(1)
            dbCount = dbCountT.result()

            #with open(HomeDir + fr"\Saves\LastDBCount.txt", "rw") as dbCountFile:
            #    if len(str(ctx.message.content).split(" ")) > 1:
            #        if str(str(ctx.message.content).split(" ")[1]) == "-db":
            #            dbCount = countDB(dbDict)
            #            dbCountFile.write(str(dbCount))
            #    else:
            #        if os.path.exists(HomeDir + fr"\Saves\LastDBCount.txt"):
            #            dbCount = str(dbCountFile.read())
            #            if dbCount == "" or dbCount is None:
            #                dbCount = "Recount Required"
            #        else:
            #            dbCount = "Recount Required."
            #dbCountFile.close()
            await message2del.delete()
            loop.create_task(messageHandler(ctx=ctx, lines=[f" @#F System Settings: @#V "
                            f"Servers: {len(bot.guilds)}\n"
                            f"Latency: {round(bot.latency*1000, 2)}ms\n"
                            f"Memory Usage: {str(round(psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2, 2))}mb/16000mb\n"
                            f"quietOut: {quietOut}\n"
                            f"accTimers: {accTimers}\n"
                            f"timers: {timers}\n"
                            f"bots: List[Bot] length: {len(bots)}\n"
                            f"bot array prefix: % \n"
                            f"current active timers: {len(counterArray)} \n"
                            f"musicBotDisable: {musicbotDisable}\n"
                            f"utilbotDisable: {utilbotDisable}\n"
                            f"current entries in megaArray: {len(megaArray)} \n"
                            f"Entries in local DB: {dbCount}"], quietMode=2))

        return

    @bot.command(name="timers")
    async def toggletimers(ctx):
        global timers
        if ctx.message.author.id == 246892047284436992 or ctx.message.author.id == 855613733854642237:
            if timers:
                timers = False
            else:
                timers = True
        return
    @bot.command(name="accurate-timers")
    async def accuratetimers(ctx):
        global accTimers
        if ctx.message.author.id == 246892047284436992 or ctx.message.author.id == 855613733854642237:
            if accTimers:
                accTimers = False
            else:
                accTimers = True
        return
    @bot.command(name="quietout")
    async def quietMode(ctx):
        global quietOut
        if ctx.message.author.id == 246892047284436992 or ctx.message.author.id == 855613733854642237:
            if quietOut:
                quietOut = False
            else:
                quietOut = True
                #system("cls")
        return
    @bot.command(name="collage")
    async def collagecmd(ctx):
        if len(str(ctx.message.content).split(" ")) > 1:
            counter2=0
            for each in str(ctx.message.content).split(" "):
                counter2+=1
            counter = 0
            alisst = []
            for each in str(ctx.message.content)[9:].split(","):
                alisst.append(each.replace(" ", "+"))
            DIR = HomeDir + f"\Saves\ServerCreation\{ctx.message.author.id}_temp\\"
            image = await createCollage(ctx, alisst, DIR, numbered=True)
            loop.create_task(ctx.send(file=discord.File(image), content=""))
            return

    @bot.command(name="prefix")
    async def changeprefix(ctx):
        global commandPrefix, serverData

        #djRolePosition = None
        if ctx.message.author.guild_permissions.manage_roles or \
                (ctx.message.author.id == 246892047284436992 or ctx.message.author.id == 855613733854642237):
            for each in serverData:
                if each[0] == ctx.guild.id:
                    serverDataTemp = []
                    for key in serverData:
                        serverDataTemp.append(key)
                    serverData = []
                    for key in serverDataTemp:
                        if str(key) != str(each):
                            serverData.append(key)
                    prefix = str(str(ctx.message.content).split(" ")[1])
                    # print(prefix)
                    if prefix == '':
                        loop.create_task(messageHandler(ctx=ctx, lines=["@#F Error: @#V Prefix cannot be empty."], quietMode=2))
                        return
                    loop.create_task( messageHandler(ctx=ctx, lines=[
                        f"@#F Prefix Set: @#V {prefix} will now be used as this servers command prefix"], quietMode=2))
                    serverData.append(
                        [ctx.guild.id, str(str(ctx.message.content).split(" ")[1]), None, None])
                    try:
                        await nameHandler(ctx=ctx, commandPrefix=prefix)
                    except:
                        pass
                    numpy.save(HomeDir + r"\Saves\PrefixDB.npy", serverData, allow_pickle=True)
                    return
            #if exists == 0:
            serverDataTemp = []
            for key in serverData:
                serverDataTemp.append(key)
            serverData = []
            for key in serverDataTemp:
                serverData.append(key)
            prefix = str(str(ctx.message.content).split(" ")[1])
            if prefix == '':
                loop.create_task(messageHandler(ctx=ctx, lines=["@#F Error: @#V Prefix cannot be ''."]))
                return
            serverData.append([ctx.guild.id, str(str(ctx.message.content).split(" ")[1]), None, None])
            loop.create_task(messageHandler(ctx=ctx,
                                 lines=[
                                     f"@#F Prefix Set: @#V {prefix} will now be used as this servers command prefix"], quietMode=2))
            try:
                #await ctx.guild.me.edit(nick=prefix + "mц_ՏIꝎIϨ_ μm" + prefix)
                await ctx.guild.me.edit(nick=prefix + "MuseIT (" + prefix + ")")
            except:
                pass
            numpy.save(HomeDir + r"\Saves\PrefixDB.npy", serverData, allow_pickle=True)

        else:
            loop.create_task(messageHandler(ctx=ctx,
                                 lines=[
                                     " @#F Permission Denied: @#V You do not have permission to use this command.\n"
                                     "User must have manage roles permissions to change the bot prefix"]))
        serverData = numpy.load(HomeDir + r"\Saves\PrefixDB.npy", allow_pickle=True)
        return
    @bot.command(name="delmsgs")
    async def deletemsgs(ctx):
        global botData, deleteinprogress
        if deleteinprogress == 0:
            deleteinprogress = 1
            if ctx.message.author.id != 246892047284436992 and ctx.message.author.id != 855613733854642237:
                deleteinprogress = 0
                print("not serbz")
                return
            else:
                number = str(ctx.message.content).split(" ")[1]
                if str(ctx.message.content).split(" ")[1] is not None and str(ctx.message.content).split(" ")[
                    1] != [] and \
                        str(ctx.message.content).split(" ")[1] != "":
                    mgs = []  # Empty list to put all the messages in the log
                    number = int(number)  # Converting the amount of messages to delete to an integer
                    async for x in (await getCTX2(ctx)).history(limit=number):
                        mgs.append(x)
                    taskloops = []
                    count = 0
                    for every in mgs:
                        count += 1
                        taskloops.append(delMessageTask(ctx, every, count))
                    await asyncio.gather(*taskloops)
                    stringy = ""
                    for each in botData:
                        stringy += f"\n bot: {each[2]}#{each[0]} completed {each[1]} tasks"
                    await messageHandler(ctx=ctx, lines=[f" @#F Process Complete: @#V Deleted {count} messages",
                                                         f" @#F Stats: @#V {stringy}"], cloners=1)
            deleteinprogress = 0
        else:
            await messageHandler(ctx=ctx, lines=[f" @#F Error: @#V deletion command already in progress. Please wait."], cloners=1)
        return
    @bot.command(name='leave')
    async def leave(ctx, nosend="NaN"):
        global sysChannel, megaArray
        if str(ctx.message.content).lower() == commandPrefix + "leave":
            nosend = "yup"
        channel = await getChannel(ctx)
        voice = None
        if channel is not None:
            try:
                voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
            except:
                pass
        loop.create_task(stopplaying(ctx, nosend="no"))
        loop.create_task(arrayBuilder(ctx, isPlaying=0))
        if voice is not None:
            loop.create_task(voice.disconnect())
        return

    @bot.command(name='pause')
    async def stopplaying(ctx, nosend="NaN"):
        global megaArray
        try:
            server = ctx.message.guild
        except AttributeError:
            server = ctx.guild
            pass
        voice = None
        for each in megaArray:
            if each[0][0][0] == server.id:
                voice = each[0][0][3]
        if voice is not None or type(voice) is not None:
            try:
                voice.pause()
            except:
                try:
                    voice.pause()
                except:
                    pass
                pass
        loop.create_task(arrayBuilder(ctx, isPlaying=0))
        if nosend == "NaN":
            loop.create_task(messageHandler(ctx=ctx, lines=[
                f"@#F Audio Paused: @#V play with {commandPrefix}play or clear the list with {commandPrefix}clear"]))
        return

    @bot.command(name="seek")
    async def seek(ctx):
        global megaArray, rrt
        msgSpl = str(str(ctx.message.content).split(" ")[1]).split(":")
        offset = 0
        try:
            if len(msgSpl) > 2:
                hour = int(msgSpl[0])
                offset = 1
            else:
                hour = '00'
            minute = int(msgSpl[0 + offset])
            second = int(msgSpl[1 + offset])
        except (TypeError, AttributeError, IndexError, NameError) as e:
            loop.create_task(messageHandler(ctx=ctx,
                                 lines=[f"@#F Error: @#V Correct usage is: {commandPrefix}seek HH:MM:SS or "
                                        f"MM:SS where HH, MM, and SS represent double digit integer values (ie. {commandPrefix}seek 00:48 "
                                        f"would seek the currently playing or queued to play audio source to 48 seconds."],
                                 quietMode=2))
            return
        for each in megaArray:
            if each[0][0][0] == ctx.guild.id:
                voiceChannel = each[0][0][1]
                voice_client = each[0][0][3]
                try:
                    loop.create_task(voice_client.connect())
                except:
                    try:
                        loop.create_task(voiceChannel.connect())
                    except:
                        pass
                    pass
                playingSongNum = each[0][4]
                audio = each[0][3]
                clip2 = each[0][5]
                songDuration = each[0][7]
                video_title = each[0][6]
                if video_title is None:
                    video_title, songDuration = await getVideoTitle(clip2, returnB="notNone")
                try:
                    voice.pause()
                except:
                    pass
                #stopArray.append(ctx.guild.id)
                seekffmpeg_opts = {
                    'before_options': f'-ss {str(hour)}:{str(minute)}:{str(second)}.00 -reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
                    'options': '-vn'}
                stopArray.append(ctx.guild.id)
                await asyncio.sleep(1)
                loop.create_task(playingLoop(ctx, voice_client, ctx.guild, ProjectFFMPEG, audio,
                                  clip2, video_title, playingSongNum, songDuration, skipMessage="notNone",
                                  ffmpeg_opts=seekffmpeg_opts))
                print(stopArray)
                counter = -1
                while counter < len(stopArray):
                    if stopArray[counter] == ctx.guild.id:
                        stopArray.pop(counter)
                print(stopArray)

                loop.create_task(messageHandler(ctx=ctx, lines=[
                    f"@#F Seeking: @#V Skipped to: timestamp {str(hour)}:{str(minute)}:{str(second)}.00 for currently playing audio source"]))
                return
        loop.create_task(messageHandler(ctx=ctx, lines=[
            f"@#F Error: @#V Nothing is currently playing, or I have disconnected from the voice channel. There is no data to use."]))
        return

    @bot.command(name="skipto")
    async def skipto(ctx, lotus=-1, direct=None):
        global megaArray, stopArray
        #for each in stopArray:
        #    if each == ctx.guild.id:
        #        return
        #stopArray.append(ctx.guild.id)
        counter = -1
        megaExist = 0
        voice_client = None
        server = None
        clip2 = None
        if direct is not None:
            clip2 = direct[0]
            video_title = direct[1]
            songDuration = direct[2]
        try:
            songNumber = direct[3]
        except:
            songNumber  = None
            pass
        if direct is None:
            clip2 = ""
            video_title = ""
            for each in megaArray:
                if each[0][0][0] == ctx.message.guild.id:
                    songNumList = each[0][0][2]
                    megaExist = 1
                    for key in songNumList:
                        counter = counter + 1
                        try:
                            if key[1] == int(str(ctx.message.content).split(" ")[1]):
                                clip2 = key[0]
                                video_title = key[2]
                                songDuration = each[0][7]
                        except:
                            commandPrefix = await determine_prefix(bot, ctx.message)
                            await messageHandler(ctx=ctx, lines=[f" @#F Error: @#V You must specify a song "
                            f"number to skip to\nRefer to {commandPrefix}list for a song number to skip to."], quietMode=2)
                            return
                        voice_client = each[0][0][3]
                        server = each[0][0][4]

                    break
            if megaExist == 0:
                await ctx.send("There is nothing to skip to.")
                return
            if int(str(ctx.message.content).split(" ")[1]) - 1 > counter:
                await messageHandler(ctx=ctx, lines=[f" @#F Error: @#V There are not that many songs on the play list.\n there are " + str(
                    counter + 1) + " entries in the current playlist"], quietMode=2)
                return
            if int(str(ctx.message.content.split(" ")[1])) - 1 < 0:
                await ctx.send("Impossible")
                return
        audio = None
        if clip2 != "" and clip2 is not None:
            try:
                video = new(clip2)
                audio = video.getbestaudio().url
            except:
                try:
                    video = new(clip2)
                    audio = video.getbestaudio().url
                except:
                    try:
                        await messageHandler(ctx=ctx, lines=[f" @#F Error: @#V Unsure why, but this video seems unavailable. :("])
                        if songNumber is None:
                            songNumber = int(str(ctx.message.content).split(" ")[1])
                        await arrayBuilder(ctx, audio=None, playingSongNum=songNumber,
                                           videoDuration=songDuration, clip2=clip2, video_title=video_title)

                        print("SKIPTO FUNC - back to next")
                        await next(ctx)
                    except:
                        return
                pass
            if songNumber is None:
                songNumber = int(str(ctx.message.content).split(" ")[1])
            if voice_client is None:
                channel = await getChannel(ctx)
                voice_client = await getVoice(ctx, channel)
            if server is None:
                server = ctx.guild
            await arrayBuilder(ctx, audio=audio, playingSongNum=songNumber,
                               videoDuration=songDuration, clip2=clip2, video_title=video_title)
            print(f"{stopArray}")
            counter = -1
            while counter < len(stopArray)-1:
                counter += 1
                if stopArray[counter] == ctx.guild.id:
                    stopArray.pop(counter)
                    print(f"SKIPTO FUNC - removed entry in stopArray")
            print(f"{stopArray}")
            #stopArray.append(ctx.guild.id)
            print(f"{stopArray}")
            print("SKIPTO FUNC - playing loop")
            await playingLoop(ctx, voice_client, server, ProjectFFMPEG, audio, clip2, video_title, songNumber,
                              songDuration, skipMessage=None)
            return
    @bot.command(name="m4a")
    async def yt2mp323123(ctx):
        await yt2mp3(ctx)
        return
    @bot.command(name="mp3")
    async def yt2mf902(ctx):
        await yt2mp3(ctx)
        return
    @bot.command(name="download")
    async def yt2mf902(ctx):
        await yt2mp3(ctx)
        return

    @musicBot.command(name='list')
    async def list2list(ctx):
        list2array = await list2cmd(ctx)
        await arrayBuilder(ctx, listArray=list2array)
        return
    @bot.command(name="dl")
    async def yt2mf902(ctx):
        await yt2mp3(ctx)
        return
    async def yt2mp3(ctx):
        global yt2mp3Array
        for each in yt2mp3Array:
            if each == ctx.guild.id:
                await messageHandler(ctx=ctx, lines=[" @#F Error: @#V Only one of these commands can run per server. \n Please wait."])
                return
        yt2mp3Array.append(ctx.guild.id)
        clipStr = ""
        counter = 0
        for each in str(ctx.message.content).split(" "):
            counter = counter + 1
            if counter != 0:
                clipStr = clipStr + " " + each
        video_title1 = None
        if "http" in clipStr.lower() and "youtube.com" in clipStr.lower() and "://" in clipStr.lower():
            print("link")
            clipStr2 = clipStr.split("watch?v=")
            print(str(len(clipStr2)))
            if len(clipStr2) > 1:
                f_clip = "http://www.youtube.com/watch?v=" + clipStr2[1][:11]
                video_title1, video_duration = await getVideoTitle(clip2=f_clip, returnB="notNone")
                print(str(clip2))
                clip2 = f_clip
        else:
            music_name = clipStr
            query_string = urllib.parse.urlencode({"search_query": music_name})
            formatUrl = urllib.request.urlopen("https://www.youtube.com/results?" + query_string)
            search_results = re.findall(r"watch\?v=(\S{11})", formatUrl.read().decode())
            clip2 = str("https://www.youtube.com/watch?v=" + "{}".format(search_results[0]))
        try:
            os.mkdir(f'{HomeDir}\Saves\YTMP3\\{ctx.message.author.id}')
        except:
            pass
        await ballsoffingtungstencarbide(ctx, clip2, video_title1)
        return
    async def systemYtdl(dir, ID, mmpeg, clip2):
        os.system("youtube-dl -f bestaudio[ext=m4a] --extract-audio -o "  # --get-filename -o "
                   f"{dir}" + f"\Saves\YTMP3\\{ID}\\" + str("%(title)s.%(ext)s").replaceAll("[^a-zA-Z0-9\\s+]", "") + " "
                                                         f"--no-part "
                                                         f"--no-playlist "
                                                         f"--write-thumbnail "
                                                         f"--no-warnings "
                                                         f"--ffmpeg-location {mmpeg} "
                                                         f"{clip2}")
        folder = f"{dir}" + fr"\Saves\YTMP3\{ID}"
        return folder
    async def osWrapper():
        folder = await systemYtdl(HomeDir, ctx.message.author.id, ProjectFFMPEG4, clip2)

    async def ballsoffingtungstencarbide(ctx, clip2, video_title1):
        global yt2mp3Array
        try:
            await osWrapper()
        except:
            pass
        folder = HomeDir + f"\Saves\\{ctx.message.author.id}"
        video_title1, video_duration = await getVideoTitle(clip2=clip2, returnB="notNone")
        if video_title1 is None or video_title1 == "error 298":
            with YoutubeDL(ydl_opts) as ydl:
                video_title1 = str((ydl.extract_info(clip2, download=False)).get('title', None))\
                    .replaceAll("[^a-zA-Z0-9\\s+]","")
        if video_title1 is None or video_title1 == "error 298":
            await messageHandler(ctx=ctx, lines=[f" @#F Error: @#V Error 298"])
            return
        file = folder + f"\\{video_title1}.m4a"
        if os.path.exists(str(folder+fr"\{video_title1}.jpg")):
            image = str(folder+fr"\{video_title1}.jpg")
        elif os.path.exists(str(folder+fr"\{video_title1}.webp")):
            image = str(folder+fr"\{video_title1}.webp")
        else:
            image = None
        counter = -1
        for each in yt2mp3Array:
            counter += 1
            if each == ctx.guild.id:
                yt2mp3Array.pop(counter)
        await messageHandler(ctx=ctx, lines=[f" @#F Complete! @#V ** " + str(video_title1.replace("_", " ")) + "**\n"],image=image, file=discord.File(file))
        return
    @bot.command(name="gentext")
    async def gentexrcmd(ctx):
        await generateText(ctx, None, cmdSplList[1], cmdSplList[0], cmdSplList[2])
        return
    @bot.command(name="text")
    async def gentexrcmd(ctx):
        await generateText(ctx, None, cmdSplList[1], cmdSplList[0], cmdSplList[2])
        return
    @bot.command(name="gt")
    async def gentexrcmd(ctx):
       # ctxSpl = str(ctx.message.content).split(" ")
       # counter = -1
       # count = 1
       # stringy = ""
       # for each in ctxSpl:
       #     counter+=1
       #     if counter != 0:
       #         stringy += each + " "
       #     if each == "!@#":
       #         if each[]
       #         count = int(ctxSpl[counter+1])
       #         break
        #await generateText(ctx, None, count)
        stringy, gentextAmount, font, arg3 = await commandSplitter(ctx=ctx, command="gt", cmdSelString="!@#")

        gentextAmount = int(gentextAmount)
        stringy = str(stringy)
        font = str(font.strip())
        #print(cmdSplList)
        #if cmdSplList[1] == 0 and cmdSplList[2] == "" and cmdSplList[3] is None:
        await generateText(ctx=ctx, gentextAmount=gentextAmount,
                           stringSt=stringy, fontreq=font)
        return

    async def commandSplitter(ctx, command="", cmdSelString=r"//", mode=0):
        if ctx is not None:
            ctxSpl = str(ctx.message.content).split(" ")
            stringy = ""
            counter = -1
            selective = 0
            skipNext = 0
            arg1 = 1 # gt = count ||
            arg2 = "" # gt = font ||
            arg3 = None # gt None
            for each in ctxSpl:
                counter+=1
                print(counter, "counter")
                if skipNext == 0:
                    print(skipNext, "skipNext = 0")
 #                   if command == "gt":
                        #print(command, "command = gt")
                    print(f" if {each[:3]} == r\"!@#\" or {selective} == 1:")
                    if each[:3] == r"!@#" or selective == 1:
                        #print(cmdSelString, each[:3], selective,
                        #      f"{each[:3]} == {cmdSelString} or {selective} == 1")
                        selective = 1
                        if each[:1] == "-":
                            print(each[:1],
                                  f"{each[1:]} == \"-\"")
                            if each[1:] == "c" or each[1:] == "count":
                                arg1 = int(ctxSpl[counter+1])
                                if arg1 > 10:
                                    arg1 = 10
                                skipNext = 1
                                print(cmdSelString, each[:3], selective,
                                      f"{each[1:]} == \"c\" or {each[1:]} == count")
                            if each[1:] == "f" or each[1:] == "font":
                                print(cmdSelString, each[:3], selective,
                                      f"{each[1:]} == \"c\" or {each[1:]} == count")
                                arg2 = ctxSpl[counter+1]
                                skipNext = 1
                else:
                    skipNext = 0
                if counter != 0 and selective != 1:
                    stringy += each + " "
                    print(stringy)
        return stringy, arg1, arg2, arg3

    @bot.command(name='shuffle')
    async def shuffle(ctx):
        global megaArray
        shuffle = "unset"
        for each in megaArray:
            if each[0][0][0] == ctx.guild.id:
                shuffle = each[0][2]
                if shuffle is None or shuffle == 0:
                    shuffle = 1
                    stringy = "enabled"
                else:
                    shuffle = 0
                    stringy = "disabled"
                await messageHandler(ctx=ctx, lines=[f"@#F Toggled Shuffle: @#V Shuffle is now {stringy}."])
                await arrayBuilder(ctx=ctx, shuffle=shuffle)

                break
        if shuffle == "unset":
            await arrayBuilder(ctx=ctx, shuffle=1)
            await messageHandler(ctx=ctx, lines=[f" @#F Toggled Shuffle: @#V Shuffle is now enabled."])
        commandPrefix = await determine_prefix(bot, ctx.message)
        await nameHandler(ctx=ctx, commandPrefix=commandPrefix)
        return

    @bot.command(name='save')
    async def save(ctx):
        global sysChannel, megaArray
        ctxSpl = str(ctx.message.content).split(" ")
        for each in megaArray:
            if each[0][0][0] == ctx.guild.id:
                server = ctx.guild.id
        SaveDir = HomeDir + r"\Saves\\" + str(ctx.message.author.id)
        try:
            os.mkdir(SaveDir)
        except FileExistsError:
            pass
        counter = 0
        loadStr = ""
        for name in os.listdir(SaveDir):
            if os.path.isfile and ".songs.npy" not in str(name):
                counter = counter + 1
                nameSpl = str(name).split(".")
                loadStr = loadStr + "\n-- II " + str(counter) + ". " + nameSpl[1]
        NumSaves = int(
            float(len([name for name in os.listdir(SaveDir) if os.path.isfile(os.path.join(SaveDir, name))])))
        if len(ctx.message.content) <= 6:
            await messageHandler(ctx=ctx, lines=[
                f"@#F Error! @#V ```{formatString}\n-Please, specify a playlist name ie. \n ({commandPrefix}save PlayListName)```"], quietMode=2)
            if NumSaves >= 1:
                await messageHandler(ctx=ctx, lines=[f"@#F Playlists currently saved: @#V ```" + loadStr + "```"], quietMode=2)
            return
        if NumSaves >= 5:
            saveNumDifference = NumSaves - 4
            await messageHandler(ctx=ctx, lines=[
                f"@#F Error! @#V ```{formatString}\nYou have too many saves already, please remove atleast " + str(
                    saveNumDifference) + f" saved playlist(s) ({commandPrefix}delsave PlayListNumber) before saving a new one for user: "
                + str(ctx.message.author.name) + " with ID: " + str(ctx.message.author.id) + "```"], quietMode=2)
            return
        playListName = str(ctxSpl[1]).lower()
        if len(playListName) > 25:
            await messageHandler(ctx=ctx,
                                 lines=[f"@#F Error! @#V ```{formatString}\n-Please choose a shorter play list "
                                        f"name. Character limit of 25.```"], quietMode=2)
            return
        playListNameSpl = await splitword(playListName)
        alphabet = ""
        for each in ascii_lowercase:
            alphabet = alphabet + each
        for each in playListNameSpl:
            if str(each).lower() not in str(alphabet):
                await messageHandler(ctx=ctx, lines=[
                    f"@#F Error! @#V ```{formatString}\n-Only letters are allowed in playlist names```"], quietMode=2)
                return
        exists = 0
        songNumList = []
        Save = "\Playlist." + str(playListName)
        for each in megaArray:
            if each[0][0][0] == ctx.guild.id:
                songNumList = each[0][0][2]
                exists = 1
        if exists == 1:
            if songNumList != []:
                counter = 0
                for each in songNumList:
                    counter = counter + 1
                numpy.save(SaveDir + Save + ".clips" + ".npy", songNumList)
                await messageHandler(ctx=ctx,
                                     lines=["@#F Saved! @#V Playlist with " + str(playListName) + " is now saved to"
                                                                                                  " the user: " + str(
                                         ctx.message.author.name) + "\n ID: " + str(ctx.message.author.id),
                                            "@#F ----- @#V " +
                                            str(counter) + " songs in the playlist."], quietMode=2)
            else:
                await messageHandler(ctx=ctx, lines=["@#F Error: @#V There is nothing to save. (390)"], quietMode=2)
        else:
            await messageHandler(ctx=ctx, lines=["@#F Error: @#V There is nothing to save. (392)"], quietMode=2)
        return


    @bot.command(name="cls")
    async def clscmd(ctx):
        if ctx.message.author.id == 246892047284436992 or ctx.message.author.id == 855613733854642237:
            os.system('cls')
        return

    @bot.command(name="delsave")
    async def delsave(ctx):
        global sysChannel, megaArray
        try:
            server = ctx.message.guild
        except AttributeError:
            server = ctx.guild
            pass
        SaveDir = HomeDir + r"\Saves\\" + str(ctx.message.author.id)
        try:
            os.mkdir(SaveDir)
        except FileExistsError:
            pass
        counter = 0
        NumSaves = int(
            float(len([name for name in os.listdir(SaveDir) if os.path.isfile(os.path.join(SaveDir, name))])))
        if NumSaves <= 0:
            await messageHandler(ctx=ctx, lines=[
                f" @#F Error: @#V ```{formatString}\n-There are no playlists saved to be deleted.```"], quietMode=2)
            return
        loadStr = ""
        loadArray = []
        delNameArry = []
        for name in os.listdir(SaveDir):
            if os.path.isfile:
                counter = counter + 1
                nameSpl = str(name).split(".")
                loadStr = loadStr + "\n-- II " + str(counter) + ". " + nameSpl[1]
                delNameArry.insert(counter - 1, nameSpl[1])
                loadArray.insert(counter - 1, name)
        if len(ctx.message.content) <= 9:
            await messageHandler(ctx=ctx, lines=[
                "@#F Playlists Available: " +
                "@#V ```yaml\n" + str(loadStr) + "``` ",
                "@#F You can use: " + f" @#V {commandPrefix}delsave 1-5 for this command."], quietMode=2)
            return
        ctxSpl = str(ctx.message.content).split(" ")
        playListName = str(ctxSpl[1]).lower()
        if len(playListName) > 1:
            await messageHandler(ctx=ctx, lines=["@#F Incorrect usage: @#V please specify a number 1-5"], quietMode=2)
            return
        try:
            if 5 >= int(str(playListName)) >= 1:
                playListNumber = int(str(playListName))
            else:
                await messageHandler(ctx=ctx, lines=["@#F Incorrect usage: @#V Please specify a number 1-5"], quietMode=2)
                return
        except:
            await messageHandler(ctx=ctx, lines=["@#F Incorrect usage: @#V Please specify a number 1-5"], quietMode=2)
            return
        if playListNumber > counter:
            await messageHandler(ctx=ctx, lines=[
                "@#F Incorrect usage: @#V Playlist #" + str(playListNumber) + " does not exist."], quietMode=2)
            return
        counter = 0
        Save1 = ""
        for each in loadArray:
            counter = counter + 1
            if counter == playListNumber:
                Save1 = SaveDir + "\\" + each
                break
        SaveToDel = delNameArry[counter - 1]
        try:
            os.remove(Save1)
        except:
            await messageHandler(ctx=ctx, lines=[f" @#F Error: @#V f```{formatString}\n Unable to delete save for"
                    f" some reason who knows, I don't else I would have deleted it. (622)"])#, dummy, but I don't know and I "
            return
        await messageHandler(ctx=ctx,
                             lines=[f" @#F Playlist Removed: @#V ```{formatString}\nPlaylist: " + str(SaveToDel) + \
                                    " for user: " + str(ctx.message.author.name) + " with ID: " + str(
                                 ctx.message.author.id) + "```"])
        return

    @bot.command(name='load')
    async def load(ctx):
        global sysChannel, megaArray
        songList = []
        for each in megaArray:
            if each[0][0][0] == ctx.guild.id:
                songList = each[0][0][2]
                guildObj = each[0][0][4]
        SaveDir = HomeDir + r"\Saves\\" + str(ctx.message.author.id)
        try:
            os.mkdir(SaveDir)
        except FileExistsError:
            pass

        NumSaves = int(
            float(len([name for name in os.listdir(SaveDir) if os.path.isfile(os.path.join(SaveDir, name)) and
                       not name.endswith(r'.txt')])))
        if NumSaves <= 0:
            loop.create_task(messageHandler(ctx=ctx, lines=["@#F error: "
            f" @#V ```{formatString}\n-There are no playlists saved to user to be loaded.``` "
                        f"use {commandPrefix}save PlayListName"], quietMode=2))
            return
        loadStr = ""
        loadArray = []
        counter = 0
        for name in os.listdir(SaveDir):
            if os.path.isfile and not name.endswith(r'.txt'):
                counter = counter + 1
                nameSpl = str(name).split(".")
                loadStr = loadStr + "\n-- II " + str(counter) + ". " + nameSpl[1]
                loadArray.insert(counter - 1, name)
        if len(ctx.message.content) <= 6:
            loop.create_task(messageHandler(ctx=ctx,
                                 lines=["@#F Playlists Available: @#V ```" + loadStr + "```", "@#F You can use:"
            f" @#V {commandPrefix}load 1-5 for this command\n or just {commandPrefix}load shows this list."],
                                       quietMode=2))
            return
        ctxSpl = str(ctx.message.content).split(" ")
        playListName = str(ctxSpl[1]).lower()
        if len(playListName) > 1:
            loop.create_task(messageHandler(ctx=ctx,
                                       lines=["@#F Incorrect Usage: @#V Please specify a number 1-5"], quietMode=2))
            return
        try:
            if 5 >= int(str(playListName)) >= 1:
                playListNumber = int(str(playListName))
            else:
                loop.create_task(messageHandler(ctx=ctx,
                                     lines=["@#F Incorrect Usage: @#V Please specify a number 1-5"], quietMode=2))
                return
        except:
            loop.create(messageHandler(ctx=ctx,
            lines=["@#F Incorrect Usage: @#V Please specify a number 1-5"], quietMode=2))
            return
        if playListNumber > counter:
            loop.create_task(messageHandler(ctx=ctx, lines=[
                "@#F Incorrect Usage: @#V Playlist #" + str(playListNumber) + " does not exist."], quietMode=2))
            return
        counter = 0
        Save1 = ""
        for each in loadArray:
            counter = counter + 1
            if counter == playListNumber:
                Save1 = SaveDir + "\\" + each
                saveName = each.split(".")[1]
                break
        playLists = numpy.load(Save1, allow_pickle=True)
        counter3 = 0
        counter2 = -1
        #print(playLists)
        for each in playLists:
            counter3 = counter3 + 1
            if len(each) < 4:
                print(f"{Style.RESET_ALL}{Fore.RED}REBUILDING PLAYLIST{Save1} FOR USER "
                      f"{ctx.message.author}-{ctx.message.author.id}{Fore.LIGHTWHITE_EX}")
                playLists = await rebuildPlaylist(ctx=ctx, file=Save1)
                break
        if len(songList) > 0 and songList != [] and songList is not None:
            for each in songList:
                counter2 = counter2 + 1
        counter = 0
        for each in playLists:
            counter = counter + 1
            counter2 = counter2 + 1
            await add2(ctx, f_clip=each[0], f_title=each[2], video_duration=each[3], SongNumber=counter2)
        loop.create_task(messageHandler(ctx=ctx, lines=[
            f"@#F Success: @#V Added {str(len(playLists))} songs to the playlist from {saveName}"], quietMode=2))
        print(f"{Style.RESET_ALL}{Fore.LIGHTBLUE_EX}{str(ctx.message.guild.name)} {Fore.LIGHTWHITE_EX} ||-||  "
              f"{str(ctx.message.channel.name)}{Fore.LIGHTWHITE_EX}  ||-||  "
              f"{Fore.LIGHTGREEN_EX} Loaded: {Fore.YELLOW} {str(len(playLists))} songs {Fore.LIGHTWHITE_EX}from {str(saveName)}")
        return

    @bot.command(name='next')
    async def next(ctx):
        global megaArray, stopArray
        #for each in stopArray:
        #    if each == ctx.guild.id:
        #        return
        #stopArray.append(ctx.guild.id)
        print(f"NEXT FUNC - function begin - {ctx.guild.name}")
        exists = 0
        nextDuration = None
        nextTitle = None
        shuffle = None
        nextClip = None
        for each in megaArray:
            if each[0][0][0] == ctx.guild.id and exists != 1:
                exists = 1
                songList = each[0][0][2]
                voice_client = each[0][0][3]
                server = each[0][0][4]
                clip2 = each[0][5]
                keyCounter = -1
                keyCountLimit = -1
                shuffle = each[0][2]
                if songList == []:
                    print(f"NEXT FUNC - if songList == []: await stopplaying await leave - {ctx.guild.name}")
                    await stopplaying(ctx, nosend="notNaN")
                    await leave(ctx)
                    return
                if len(songList) == 1:
                        nextClip = songList[0][0]
                        nextTitle = songList[0][2]
                        nextDuration = songList[0][3]
                        nextSongNum = 1
                        print(f"NEXT FUNC - if len(songList) == 1: await skipto - {ctx.guild.name}")
                        await skipto(ctx, direct=[nextClip, nextTitle, nextDuration, nextSongNum])
                        return
                if shuffle is None or shuffle == 0:
                    for each3 in songList:
                        keyCountLimit = keyCountLimit + 1
                    for each2 in songList:
                        keyCounter = keyCounter + 1
                        if str(each2[0]) == str(clip2):
                            if keyCounter + 1 > keyCountLimit:
                                keyCounter = -1
                            keyCounter = keyCounter + 1
                            nextClip = songList[keyCounter][0]
                            nextClip, nextTitle, nextDuration = await getVideoTitle(clip2=nextClip,
                            returnB="clip2", video_title=None, mode="load", spopifoo=None)
                            nextSongNum = songList[keyCounter][1]
                            print(f"NEXT FUNC -  if shuffle is None or shuffle == 0: await skipto - {ctx.guild.name}")
                            await skipto(ctx, direct=[nextClip, nextTitle, nextDuration, nextSongNum])
                            return
        counter = 0
        if exists == 1 and shuffle == 1:
            if len(songList) > 1:
                nextSongNum = random.randint(1, len(songList))
            elif len(songList) == 1:
                nextSongNum = 1
            else:
                await messageHandler(ctx=ctx, lines=[f"@#F Information: @#V There is nothing in the playlist."])
                await leave(ctx=ctx)
                return
            for each in songList:
                if each[1] == nextSongNum:
                    nextClip = each[0]
                    nextClip, nextTitle, nextDuration = await getVideoTitle(clip2=nextClip,
                        returnB="clip2", video_title=None, mode="load", spopifoo=None)
            try:
                video = new(nextClip)
            except KeyError:
                video = None

                if video == None:
                    try:
                        video = new(nextClip)
                    except KeyError:
                        await next(ctx)
                        pass
                pass
            audio = video.getbestaudio().url
            if nextTitle is None or nextDuration is None:
                nextTitle, nextDuration = await getVideoTitle(songList[keyCounter + 1][0], returnB="notNone")

            await arrayBuilder(ctx=ctx, songList=songList, clip2=nextClip,
                               playingSongNum=nextSongNum, videoDuration=nextDuration, audio=audio)
            if counter >= 10:
                await next(ctx)
                await messageHandler(ctx=ctx, lines=[f" @#F Error: @#V KeyError in next function, skipped for "
                                    f"{ctx.guild.name} {ctx.guild.id}"], system=1)
                return
            print(f"NEXT FUNC - if exists == 1 and shuffle == 1: await skipto - {ctx.guild.name}")
            await skipto(ctx, direct=[nextClip, nextTitle, nextDuration, nextSongNum])
            #await playingLoop(ctx, voice_client, server, ProjectFFMPEG, audio,
            #                  nextClip, nextTitle, nextSongNum, nextDuration)


            return
        #await messageHandler()
        await stopplaying(ctx, nosend="notNaN")
        await leave(ctx)
        return

    @bot.command(name='prev')
    async def prev(ctx):
        global megaArray, rrt
        exists = 0
        set = 0
        nextDuration = None
        nextTitle = None
        nextClip = None
        for each in megaArray:
            if each[0][0][0] == ctx.guild.id and exists != 1:
                exists = 1
                songList = each[0][0][2]
                voice_client = each[0][0][3]
                server = each[0][0][4]
                clip2 = each[0][5]
                keyCounter = -1
                keyCountLimit = -1
                shuffle = each[0][2]

                if shuffle is None or shuffle == 0:
                    for each3 in songList:
                        keyCountLimit = keyCountLimit + 1
                    for each2 in songList:
                        keyCounter = keyCounter + 1
                        if str(each2[0]) == str(clip2):
                            if keyCounter - 1 < 0:
                                keyCounter = len(songList)
                            nextClip = songList[keyCounter - 1][0]
                            nextTitle = songList[keyCounter - 1][2]
                            nextSongNum = songList[keyCounter - 1][1]
                            try:
                                nextDuration = songList[keyCounter - 1][3]
                            except:
                                try:
                                    nextTitle, nextDuration = await getVideoTitle(songList[keyCounter - 1][0],
                                                                                  returnB="notNone")
                                except:
                                    if keyCounter - 2 < 0:
                                        direct = [songList[0][0], songList[0][1], songList[0][2]]
                                    else:
                                        direct = [songList[keyCounter - 1][0], songList[keyCounter - 1][1],
                                                  songList[keyCounter - 1][2]]
                                    await skipto(ctx, direct=direct)
                                    songNumList.remove(songNumList[keyCounter - 1])
                                    await arrayBuilder(ctx=ctx, songList=songList)
                                pass
                            set = 1
                            break

                    break
                elif shuffle == 1:
                    await messageHandler(ctx=ctx,
                                         lines=[f"@#F Information: @#V This command is currently disabled while"
                                                f"shuffle is enabled"], quietMode=2)#, iterating backward through a shuffled list in the order in which was played"
                                                #f"is... look... okay... I don't wanna, just like.. use skipto for now lmao"])
                    return
                break
        if set != 1 and exists == 1:
            if len(songList) > 1:
                nextSongNum = random.randint(1, len(songList))
            elif len(songList) == 1:
                nextSongNum = 1
            else:
                await messageHandler(ctx=ctx, lines=[f"@#F Information: @#V There is nothing in the playlist."])
                await leave(ctx=ctx)
                return
            for each in songList:
                if each[1] == nextSongNum:
                    nextClip = each[0]
                    nextTitle = each[2]
                    nextDuration = each[3]
        if exists == 1:
            try:
                video = new(nextClip)
            except KeyError:
                video = None
                try:
                    while video == None:
                        video = new(nextClip)
                        await asyncio.sleep(0.25)
                except:
                    await messageHandler(ctx=ctx, lines=[f"@#F Error: @#V unknown error (1515)"])
                    return
                pass
            audio = video.getbestaudio().url
            if nextTitle is None or nextDuration is None:
                nextTitle, nextDuration = await getVideoTitle(songList[keyCounter + 1][0], returnB="notNone")
            await arrayBuilder(ctx=ctx, songList=songList, clip2=nextClip,
                               playingSongNum=nextSongNum, videoDuration=nextDuration, audio=audio)
            await playingLoop(ctx, voice_client, server, ProjectFFMPEG, audio,
                              nextClip, nextTitle, nextSongNum, nextDuration)
        return

    async def generate_spotipy_token():
        client_secret="068f99f2e3a84bdbbd9f94afce7e8f7e"
        client_id="49fbed4200634ef08a2d04566d0606e4"
        credentials = oauth2.SpotifyClientCredentials(
            client_id=client_id,
            client_secret=client_secret)
        token = credentials.get_access_token()
        return token
    @bot.command(name='addlist')
    async def addlist(ctx, URL=None):
        for each in addListsActive:
            if each == ctx.guild.id:
                await messageHandler(ctx=ctx, lines=[
                    "@#F Error: @#V there is already an addlists command running, please wait."], quietMode=2)
                return
        if "https://open.spotify.com/playlist/" in ctx.message.content:
            token = await generate_spotipy_token()
            playlistID = str(str(ctx.message.content).split("https://open.spotify.com/playlist/")[1])[:22]
            playlist_id = f'spotify:user:spotifycharts:playlist:{playlistID}'
            spotify = spotipy.Spotify(auth=token['access_token'])
            results = spotify.playlist(playlist_id)
            tracks = []
            counter3 = 0
            for item in results['tracks']['items']:
                counter3+=1
                tracks.append(f"{item['track']['name']} - {item['track']['artists'][0]['name']}")
                print(f"{item['track']['name']} - {item['track']['artists'][0]['name']}")
            stringy = ""
            msg2edit = await ctx.send(f"```Please wait... 0/{counter3}```")
            args = {
                'ctx': ctx,
                'f': spotifylistadd,
                't': asyncio.create_task,
                'count': 1,
                'waittime': 0.1
            }
            kwargs = {
                'ctx': ctx,
                'tracks': tracks,
                'totaltracknumber': counter3,
                'msg2edit': msg2edit,
            }
            #new_eventloop = asyncio.new_event_loop()
            #new_eventloop.run_until_complete(
            addListsActive.append(ctx.guild.id)
            await asyncio.gather(*(await asyncio.ensure_future(taskBuilder2(**args, kwargs=kwargs))))#)
            for each in addListsActive:
                if each == ctx.guild.id:
                    #await messageHandler(ctx=ctx, lines=[
                    #    f"@#F Task(s) Completed: @#V added {msgSplLen} list(s) to the current playlist."])
                    addListsActive.remove(each)
            return
        msgSplLen = len(str(ctx.message.content[9:]).split(" "))
        if msgSplLen > 5:
            await messageHandler(ctx=ctx,
                                 lines=["@#F Error: @#V This command is limited to 5 lists at a time."], quietMode=2)
            return
        ############## YOU TUBE LIST $$$$$$$$$$$$$$$
        if "youtube" in ctx.message.content.lower() and "http" in ctx.message.content.lower() and "playlist" in ctx.message.content.lower():
            args = {
                'ctx': ctx,
                'listT': str(ctx.message.content).split(" "),
                'f': addlist2,
                't': asyncio.create_task
            }
            addListsActive.append(ctx.guild.id)
            #new_eventloop = asyncio.new_event_loop()
            #new_eventloop.run_until_complete(
            await asyncio.gather(*(await asyncio.ensure_future(taskBuilder(**args))))#)
            for each in addListsActive:
                if each == ctx.guild.id:
                    await messageHandler(ctx=ctx, lines=[
                        f"@#F Task(s) Completed: @#V added {msgSplLen} list(s) to the current playlist."])
                    addListsActive.remove(each)
                    return
        loop.create_task(messageHandler(ctx=ctx, lines=[f" @#F Error: @#V Link not recognized."]))
        return

    async def spotifylistadd(ctx, tracks, totaltracknumber, msg2edit):
        counter = 0
        counter2 = 0
        for each in tracks:
            print(f"Spotify List Add: {each}")
            counter += 1
            counter2 += 1
            if counter2 >= 5:
                counter2 = 0
                await msg2edit.edit(content=f"```Please wait... {counter}/{totaltracknumber}```")
            #    stringy += f'{counter}. {each} \n'
            f_clip, f_title, video_duration, data = await getVideoTitle(clip2=None, returnB="clip2",
                                                                        video_title=each,
                                                                        mode="loadmatch")
            if f_clip is None or f_title is None or video_duration is None:
                f_clip = await getClip(each)
                f_title, video_duration = await getVideoTitle(clip2=f_clip, returnB="notNone", mode="load")
            args = {
                'ctx': ctx,
                'f': add2,
                't': asyncio.create_task,
                'count': 1,
                'waittime': 0.1
            }
            kwargs = {
                'ctx': ctx,
                'retrplz': False,
                'f_clip': f_clip,
                'f_title': each,
                'nosend': "NaN",
                'SongNumber': None,
                'addlistcmd': None,
                'video_duration': video_duration,
                'noLinkCheck': 1
            }
            #new_eventloop = asyncio.new_event_loop()
            #new_eventloop.run_until_complete(
            await asyncio.gather(*(await asyncio.ensure_future(taskBuilder2(**args, kwargs=kwargs))))#)
            await asyncio.sleep(0.5)
        await msg2edit.edit(content=f"```Added {counter}/{totaltracknumber} from your spotify playlist```", quietMode=2)
        return

    @bot.command(name='active')
    async def reportactive(ctx):
        global megaArray
        if ctx.message.author.id == 246892047284436992 or ctx.message.author.id == 855613733854642237:
            for each in megaArray:
                GuildID = each[0][0][0]
                server = each[0][0][4]
                voice_client = each[0][0][3]
                voiceChannel = each[0][0][1]
                songNumList = each[0][0][2]
                songNumListLen = len(songNumList)
                if voiceChannel is None or type(voiceChannel) is None:
                    voiceChannelStr = "None"
                    voice_members = "None"
                    member_string = "None"
                else:
                    voiceChannelStr = voiceChannel.name
                    voice_members = voiceChannel.members
                    for each in voice_members:
                        print(each)
                    member_string = len(voice_members)
                if type(voice_client) is not None and voice_client is not None:
                    voice_clientSTR = str(voice_client)
                else:
                    voice_clientSTR = "None"
                print(
                    f"{Style.RESET_ALL}{Fore.LIGHTWHITE_EX}------------------------------------------------------------")
                print(f"{Style.RESET_ALL}{Fore.CYAN}Voice Channel Guild: " + str(server))
                print(f"{Style.RESET_ALL}{Fore.CYAN}Voice Channel Name: " + str(voiceChannelStr))
                print(f"{Style.RESET_ALL}{Fore.LIGHTRED_EX}Voice Channel members: " + str(member_string))
                print(f"{Style.RESET_ALL}{Fore.MAGENTA}Number of songs in current list: " + str(songNumListLen))
                print(f"{Style.RESET_ALL}{Fore.YELLOW}Voice client obj: " + str(voice_clientSTR))
                print(
                    f"{Style.RESET_ALL}{Fore.LIGHTWHITE_EX}------------------------------------------------------------{Style.RESET_ALL}")
        return

    @bot.command(name="play")
    async def play2(ctx):
        global megaArray
        voice_client = None
        if len(str(ctx.message.content).split(" ")) <= 1:  # message was just ~play
            for each in megaArray:
                guildID = each[0][0][0]
                if guildID == ctx.message.guild.id:
                    songNumList = each[0][0][2]
                    voice_client = each[0][0][3]
                    try:
                        if voice_client.is_paused():
                            voice_client.resume()
                            return
                    except:
                        pass
                    if voice_client is None or type(voice_client) is type(None):
                        channel = await getChannel(ctx)
                        voice_client = await getVoice(ctx, channel)
                        await arrayBuilder(ctx, voice_client=voice_client)
                    if len(songNumList) >= 1:
                        try:
                            clip2 = each[0][5]  # first entry in megaArray clips
                            for key in songNumList:
                                if key[0] == clip2:
                                    video_title = key[2]
                                    songNumber = key[1]
                                    songDuration = key[3]
                            video = new(clip2)
                            audio = video.getbestaudio().url
                            channel = await getChannel(ctx)
                            voice_client = await getVoice(ctx, channel)
                            if voice_client is None or type(voice_client) is type(None):
                                channel = await getChannel(ctx)
                                voice_client = await getVoice(ctx, channel)
                                await arrayBuilder(ctx, voice_client=voice_client)
                            server = ctx.guild
                            playingSongNum = each[0][4]
                            if playingSongNum is None or playingSongNum == 0:
                                playingSongNum = 1
                            await arrayBuilder(ctx=ctx, audio=audio, clip2=clip2, playingSongNum=songNumber,
                                               videoDuration=songDuration, video_title=video_title)
                            await playingLoop(ctx, voice_client, server, ProjectFFMPEG, audio, clip2, video_title,
                                              playingSongNum, songDuration)
                            return
                        except:
                            clip2 = songNumList[0][0]  # first entry in megaArray clips
                            video_title = songNumList[0][2]  # first for title
                            # print(str(songNumList))
                            try:
                                songDuration = songNumList[0][3]
                            except:
                                await messageHandler(ctx=ctx,
                                                     lines=[f" @#F Information: @#V Error found in current playlist"
                                                            f"\nPlease wait.\nRebuilding list, and correcting data."])
                                songNumList = await rebuildPlaylist(ctx, file=None, listT=songNumList)
                                clip2 = songNumList[0][0]  # first entry in megaArray clips
                                video_title = songNumList[0][2]
                                songDuration = songNumList[0][3]
                                pass
                            video = new(clip2)
                            audio = video.getbestaudio().url
                            channel = await getChannel(ctx)
                            voice_client = await getVoice(ctx, channel)
                            server = ctx.guild
                            await arrayBuilder(ctx=ctx, audio=audio, clip2=clip2, videoDuration=songDuration,
                                               video_title=video_title)
                            await playingLoop(ctx, voice_client, server, ProjectFFMPEG, audio, clip2,
                                              video_title, 1, songDuration)
                            return
                    else:
                        await messageHandler(ctx=ctx, lines=["@#F Error: @#V There is nothing to play, or audio is already currently playing (777)"])
                    return
        else:
            try:
                clip2, video_title, SongNumber = await add2(ctx, retrplz=True)
            except TypeError:
                #leave me alone. We're spitting an error already at this point if this fails and want to go no further
                # ---> nope pass
                return
            for each in megaArray:
                guildID = each[0][0][0]
                if guildID == ctx.message.guild.id:
                    video = new(clip2)
                    songNumList = each[0][0][2]
                    if SongNumber is None:
                        SongNumber = 0
                        for each in songNumList:
                            SongNumber += 1
                    try:
                        songDuration = songNumList[0][3]
                    except:
                        video_title, songDuration = await getVideoTitle(clip2, returnB="notnone")
                        pass
                    audio = video.getbestaudio().url
                    await arrayBuilder(ctx, audio=audio, playingSongNum=SongNumber, clip2=clip2,
                                       video_title=video_title)
                    if len(songNumList) == 1:
                        voice_client = None
                        try:
                            voice_client = each[0][0][3]
                        except:
                            pass
                        if voice_client is None:
                            channel = await getChannel(ctx)
                            voice_client = await getVoice(ctx, channel)
                        await playingLoop(ctx, voice_client, ctx.guild, ProjectFFMPEG, audio, clip2,
                                          video_title, SongNumber, songDuration=songDuration)
                    commandPrefix = await determine_prefix(bot, ctx.message)
                    await messageHandler(ctx=ctx,
                                         lines=[" @#F Added: @#V " + f"```{formatString}\n" + str(video_title) + \
                                                "```\n to the playlist \n\n Position : " + str(len(songNumList)) + \
                                                f"\nYou can use {commandPrefix}skipto {str(len(songNumList))}"])

                    return
        return

    @bot.command(name='remove')
    async def remove(ctx):
        global sysChannel, megaArray
        megaExists = 0
        for each in megaArray:
            guildID = each[0][0][0]
            if guildID == ctx.message.guild.id:
                megaExists = 1
        if megaExists == 0:
            await messageHandler(ctx=ctx, lines=["@#F Error: @#V Nope. (1326)"], quietMode=2)
            return
        counter = -1
        for each in str(ctx.message.content)[8:]:
            counter = counter + 1
            if str(each) == r"-":
                strSpl = str(ctx.message.content)[8:].split(r"-")
                range1 = int(strSpl[0])
                range2 = int(strSpl[1])
                await r_range(range1, range2, ctx)
                return
        strSpl = str(ctx.message.content).split(" ")
        range1 = int(strSpl[1])
        await r_range(range1, range1, ctx)
        return

    @bot.command(name='clear')
    async def clear(ctx):
        global megaArray
        songs = 0
        for each in megaArray:
            if each[0][0][0] == ctx.guild.id:
                voice = each[0][0][3]
                songs = len(each[0][0][2])
                await arrayBuilder(ctx, songList=[])
        if str(ctx.message.content).lower() == commandPrefix + "clear":
            await messageHandler(ctx=ctx, lines=[f"@#F Playlist cleared: @#V Removed all from the playlist."], quietMode=2)
        return
    @bot.command(name="q")
    async def shortlistq(ctx):
        await list2cmd(ctx)
        return
    @bot.command(name="queue")
    async def shortlistq(ctx):
        await list2cmd(ctx)
        return
    #@bot.command(name='list')
    async def list(ctx):
        global megaArray
        if len(str(ctx.message.content).split(" ")) <= 1:
            msgString = ""
            listArray = []
            counter2 = 0
            for each in megaArray:
                guildID = each[0][0][0]
                if guildID == ctx.message.guild.id:
                    SongList = each[0][0][2]
                    if SongList is None:
                        await messageHandler(ctx=ctx,
                                             lines=[f" @#F Playlist: @#V There is nothing in the list."], quietMode=2)
                        return
                    if SongList == [] or len(SongList) <= 0:
                        await messageHandler(ctx=ctx,
                                             lines=[f" @#F Playlist: @#V There is nothing in the list."], quietMode=2)
                        return
                    counter2 = 0
                    for key in SongList:
                        if len(str(key[2])) >= 45:
                            stringy = "..."
                        else:
                            stringy = ""
                        msgString = msgString + " " + str(key[1]) + ". " + str(key[2])[:45] + stringy + "\n"
                        if len(msgString) > 500:
                            counter2 = counter2 + 1
                            listArray.append([ctx.guild, counter2, msgString])
                            msgString = ""
            if counter2 <= 0:
                if msgString != "":
                    listArray.append([ctx.guild, counter2, msgString])
                    await messageHandler(ctx=ctx, lines=[
                        f" @#F Playlist: @#V ```{formatString}\n" + str(msgString) + "```"])
            else:
                await messageHandler(ctx=ctx, lines=[f" @#F Playlist: @#V ```{formatString}\n"
                                                     "The list is " + str(
                    counter2 + 1) + " pages long\n You can use"
                                    f" {commandPrefix}list 1-" + str(counter2 + 1) + " ```",
                                                     " @#F Playlist Page 1: @#V " + f"```"
                                                                                    f"{formatString}\n" + str(
                                                         listArray[0][2]) + "```"], quietMode=2)
            await arrayBuilder(ctx, listArray=listArray)
        elif len(str(ctx.message.content).split(" ")) == 2:
            try:
                pageNumber = int(str(ctx.message.content).split(" ")[1])
            except:
                await messageHandler(ctx=ctx,
                                     lines=[f" @#F Error: @#V command syntax is {commandPrefix}list #"], quietMode=2)
                return
            msgString = ""
            listArray = []
            counter2 = 0
            for each in megaArray:
                guildID = each[0][0][0]
                if guildID == ctx.message.guild.id:
                    SongList = each[0][0][2]
                    if SongList is None:
                        message = await messageHandler(ctx=ctx,
                                                       lines=[f" @#F Playlist: @#V There is nothing in the list."], quietMode=2)
                        return
                    if SongList == [] or len(SongList) <= 0:
                        message = await messageHandler(ctx=ctx,
                                                       lines=[f" @#F Playlist: @#V There is nothing in the list."], quietMode=2)
                        return
                    counter2 = 0
                    for key in SongList:
                        if len(str(key[2])) >= 45:
                            stringy = "..."
                        else:
                            stringy = ""
                        msgString = msgString + " " + str(key[1]) + ". " + str(key[2])[:45] + stringy + "\n"
                        if len(msgString) > 500:
                            counter2 = counter2 + 1
                            listArray.append([ctx.guild, counter2, msgString])
                            await arrayBuilder(ctx, listArray=listArray)
                            msgString = ""
            if msgString != "":
                listArray.append([ctx.guild, counter2, msgString])
            for each in megaArray:
                if each[0][0][0] == ctx.guild.id:
                    listArray = each[0][1]
                    if len(listArray) + 1 >= pageNumber >= 1:
                        counter = 0
                        for each in listArray:
                            counter = counter + 1
                            if counter == pageNumber:
                                await messageHandler(ctx=ctx, lines=[f" @#F Playlist: @#V ```{formatString}\n"
                                                                     "The list is " + str(
                                    counter2 + 1) + " pages long\n You can use"
                                                    f" {commandPrefix}list 1-" + str(counter2 + 1) + " ```",
                                                                     f" @#F Playlist Page {pageNumber}: @#V " + f"```"
                                                                                                                f"{formatString}\n" + str(
                                                                         listArray[pageNumber - 1][2]) + "```"], quietMode=2)
                                break
                    else:
                        await messageHandler(ctx=ctx,
                                             lines=[
                                                 f" @#F Error: @#V there are {str(len(listArray) + 1)} pages in the list."
                                                 "\n\npage number must be less than or equal number of pages in the list and greater than 0"], quietMode=2)
                        return
        return

    @bot.command(name='help')
    async def help(ctx):
        if len(str(ctx.message.content).split(" ")) <= 1:
            await messageHandler(ctx=ctx, lines=[f" @#F Help Options: @#V {commandPrefix}Help c / coms / commands \n "
            f"{commandPrefix}Help a / all"])
            return
        if str(ctx.message.content).split(" ")[1] == "c" or str(ctx.message.content).split(" ")[1] == "coms" or str(ctx.message.content).split(" ")[1] == "commands":
            await messageHandler(ctx=ctx, lines=[
                f" @#F {commandPrefix}Commands: @#V \n"
                f"{commandPrefix}Play / p \n "
                f"{commandPrefix}Leave \n "
                f"{commandPrefix}Pause \n "
                f"{commandPrefix}Next / N \n "
                f"{commandPrefix}Prev \n "
                f"{commandPrefix}Shuffle \n "
                f"{commandPrefix}Seek \n "
                f"{commandPrefix}Skipto / skip \n "
                f"{commandPrefix}Addlist \n "
                f"{commandPrefix}Add \n "
                f"{commandPrefix}Remove \n "
                f"{commandPrefix}List \n "
                f"{commandPrefix}Clear \n "
                f"{commandPrefix}Load \n "
                f"{commandPrefix}Save \n "
                f"{commandPrefix}Delsave \n "
                f"{commandPrefix}Quiet \n "
                f"{commandPrefix}Prefix \n "
                f"{commandPrefix}Gentext / gt \n "
                f"{commandPrefix}tts"
                f"{commandPrefix}button"
                f"{commandPrefix}Oauth \n"
            ])
            return
        if str(ctx.message.content).split(" ")[1] == "a" or str(ctx.message.content).split(" ")[1] == "all":
            await messageHandler(ctx=ctx, lines=[
            f"@#F Commands: @#V .", f" @#F "
                                    f"{commandPrefix}Play: @#V \n Description: \n "
                                    f""
                                    f"  -   When used WITH parameters it will: \n"
                                    f"            -    -  Initiate playing with a song if the current list is empty, "
                                    f"else it will add to the currently playing list and "
                                    f"shares similar functionality with {commandPrefix}add\n "
                                    f"  -   When used WITHOUT parameters it will:  \n "
                                    f"            -    -  Begin/resume playing the list\n "
                                    f"            -    -  If audio was paused, will resume\n\n "
                                    #f"            -    -  If audio is playing, will restart the audio source that is playing \n\n "
                                    f"Can be used as: {commandPrefix}p \n\n "
                                    f"Syntax: {commandPrefix}p [string/Youtube URL/blank]",
            f" @#F {commandPrefix}Leave: @#V "
            f"Description: \n leaves the voice channel. "
            f"Does not clear the list",

            f" @#F {commandPrefix}Pause: @#V \n "
            f"Description: \n Simply pauses the currently playing audio,",

            f" @#F {commandPrefix}Next: @#V \n "
            f"Description: \n plays the next song in the current list, if shuffle is on will play a random song in the list.",

            f" @#F {commandPrefix}prev: @#V \n "  # ```"
            f"Description: \n plays the previous song in the current list, CURRENTLY DISABLED IF SHUFFLE IS ON",

            f" @#F {commandPrefix}Shuffle: @#V \n "
            f"Description: \n Toggles shuffle on or off",

            f" @#F {commandPrefix}Seek: @#V \n"
            f"Description: \n Seeks to time in currently playing audio. \n\n "
            f"Syntax: {commandPrefix}seek [MM:SS or HH:MM:SS] (ie. {commandPrefix}seek 00:45)",  # ```"

            f" @#F {commandPrefix}Skipto: @#V \n "
            f"Description: \n Skips to a song in the current list. \n\n "
            f"Syntax: {commandPrefix}skipto [Integer Number] \n\n ",  # ```"
            #f"Example: {commandPrefix}skipto 31",  # ```"

            f" @#F {commandPrefix}Addlist: @#V \n "
            f"Description: \n Adds every song in youtube or spotify playlist to the currently playing playlist \n\n "
            f"Syntax: {commandPrefix}addlist [youtube/spotify playlist URL(s)]",  # ```"

            f" @#F {commandPrefix}Add: @#V \n "
            f"Description: \n Must have parameters. Only adds a song to the current list, "
            f"syntax: {commandPrefix}add [string/Youtube URL]",  # ```"

            f" @#F {commandPrefix}Remove: @#V \n "
            f"Description: \n removes item(s) by number from the current list. Can be a range of numbers. \n\n "
            f"Syntax: {commandPrefix}remove [number or range (ie. 3, or 3-10)]",  # ```"

            f" @#F {commandPrefix}List: @#V \n "
            f"Description: Displays the currently playing list\n\n "
            f"Syntax: {commandPrefix}list [blank/Integer Number]",  # ```"

            f" @#F {commandPrefix}Clear: @#V \n "
            f"Description: clears the currently playing list of all songs.",  # ```"

            f" @#F {commandPrefix}Delsave: @#V \n "
            f"Description: \n Deletes a saved playlist, 1-5, \n TIP: use {commandPrefix}load with no parameter to view your saved lists. \n\n "
            f"Syntax: {commandPrefix}delsave [Integer Number 1-5]",  # ```"

            f" @#F {commandPrefix}Load: @#V \n "
            f"Description: \n Displays the current saved playlists to load or loads a playlist. \n\n "
            f"Syntax: {commandPrefix}load [Blank/Integer Number 1-5]",  # ```"

            f" @#F {commandPrefix}Save: @#V \n "
            f"Description: \n Saves the current list to the user that can be loaded later, \n TIP: "
            f"when loaded it **adds** to the currently playing list."
            f"**this is a great way to share or merge playlists.** \n\n "
            f"Syntax: {commandPrefix}save [PlaylistName (may not contain spaces, numbers, or special characters)]",

            f" @#F {commandPrefix}Prefix: @#V \n "
            f"Description: \n Changes the command prefix, currently: {commandPrefix} \n\n "
            f"Syntax: {commandPrefix}prefix [NewCommandPrefix]",

            f" @#F {commandPrefix}quiet: @#V \n"
            f"Description: \n silences most output from the bot, this is a toggle\n\n",
            f" @#F {commandPrefix}Gentext / text / gt: @#V \n "
            f"Description: \n generates text, with random outline, color, font, for the text parameter you specify\n\n"
            f"Syntax: {commandPrefix}gt [Some Text To Generate]",
            f" @#F {commandPrefix}Tts: @#V \n "
            f"Description: \n picks from a random list of famous voices to say the text for the parameter you specify\n\n"
            f"Syntax: {commandPrefix}tts [Some text to say]",
            f" @#F {commandPrefix}Button: @#V \n "
            f"Description: \n Spawns the button. (With leaderboards) \n\n ",
            f" @#F {commandPrefix}Oauth: @#V \n "
            f"Description: \n shares the link used to add this bot to a server. \n\n\n\n ",

            "\n @#F Enjoy :) @#V ~Serbz"], quietMode=2) # ```\n"
        return

    async def resumeplay(ctx):
        for each in megaArray:
            guildID = each[0][0][0]
            if guildID == ctx.message.guild.id:
                songNumList = each[0][0][2]
                voice_client = each[0][0][3]
                try:
                    if voice_client.is_paused():
                        voice_client.resume()
                        return
                except:
                    pass
        return
    @bot.command(name="tts")
    async def tts(ctx):
        global megaArray, ProjectFFMPEG, stopArray, playingEpoch
        try:
            for each in stopArray:
                if each == ctx.guild.id:
                    returnz
            seconds = None
            minutes = None
            hours = None
            stopArray.append(ctx.guild.id)
            stringy3 = ""
            stringy = ctx.message.content[5:]
            voices = ["david-attenborough", "arnold-schwarzenegger", #"mitch-mcconnel",
                      "bob-barker", "bill-gates", "bill-clinton", "bill-nye", "homer-simpson",
                      "peter-griffin", "gilbert-gottfried"]
            stringy2 = voices[random.randint(0, len(voices) - 1)]
            next = 0
            for each in ctx.message.content.split(" "):
                if next == 0 and each != f"{commandPrefix}tts":
                    stringy3 = stringy3 + each + " "
                if next == 1:
                    stringy2 = each
                if each == r"//":
                    next = 1
                    stringy = stringy3[:-3]
            await asyncio.ensure_future(loop.create_task(messageHandler(ctx=ctx, lines=[
                f" @#F Processing: \n @#V Please wait. Processing text to speach may take a moment.",
                f" @#F Voice Selected: \n @#V {stringy2}", f" @#F Text: @#V {stringy}"])))
            try:
                file = await asyncio.create_task(tts_api.save_to_file(stringy2, stringy, HomeDir + r"\temp.wav"))
                if "504" in file['status'] or "500" in file['status']:
                    loop.create_task(messageHandler(ctx=ctx, lines=[" @#F Failure: @#V try again."]))
            except:
                for each in stopArray:
                    counter += 1
                    if each == ctx.guild.id:
                        stopArray.pop(counter)
                        break
                return
            audio = HomeDir + r"\temp.wav"
            voice = None
            startEpoch = None
            seekTime = time.time()
            counter = -1
            hours = None
            for each in playingEpoch:
                counter += 1
                if each[0] == ctx.guild.id:
                    startEpoch = each[1]
                    #print(startEpoch, seekTime)
                    playingEpoch.pop(counter)
                    break
            if startEpoch is not None:
                hours, rem = divmod( seekTime - startEpoch, 3600)
                minutes, seconds = divmod(rem, 60)
                print(hours, rem, minutes, seconds)

            channel = await getChannel(ctx)
            voice = await getVoice(ctx, channel)
            try:
                if not voice.is_connected():
                    try:
                        await voice.connect()
                    except:
                        try:
                            await channel.connect()
                        except:
                            pass
                        pass
            except:
                pass
            try:
                voice.pause()
            except:
                pass
            await asyncio.sleep(1)
            voice.play(discord.FFmpegPCMAudio(audio, executable=ProjectFFMPEG))
            while voice.is_playing():
                await asyncio.sleep(0.1)
            await asyncio.sleep(1)
            counter = -1
            for each in stopArray:
                counter+=1
                if each == ctx.guild.id:
                    stopArray.pop(counter)
                    #print(stopArray)
                    break
            for each in megaArray:
                if ctx.guild.id == each[0][0][0]:
                    videoDuration = each[0][7]
                    audio = each[0][3]
                    playingSongNum = each[0][4]
                    clip2 = each[0][5]
                    video_title = each[0][6]
                    if hours is not None:
                        hours = int(float((hours)))
                        minutes = int(float(minutes))
                        seconds = int(float(math.floor(seconds)))
                        if hours < 10:
                            hours = str("0") + str(int(float(math.floor(hours))))
                        if minutes < 10:
                            minutes = str("0") + str(int(float(math.floor(minutes))))
                        if seconds < 10:
                            seconds = str("0") + str(int(float(math.floor(seconds))))
                        print(
                            f"{Fore.CYAN}TTS COMMAND: {Fore.LIGHTYELLOW_EX}time to seek: {Fore.LIGHTGREEN_EX}{str(hours)}:{str(minutes)}:{str(seconds)}")

                    #print(hours, minutes, seconds)


                    print("playingLoop")
                            #skip = 1

                    args = {
                        'ctx': ctx,
                        'f': playingLoop,
                        't': asyncio.create_task,
                        'count': 1,
                        'waittime': 0.1
                    }
                    if type(seconds) is not type(None) and type(minutes) is not type(None) and type(hours) is not type(None):
                        await taskBuilder2(**args, kwargs={'ctx': ctx,
                           'voice': voice,
                           'server': ctx.guild,
                           'ProjectFFMPEG': ProjectFFMPEG,
                           'audio': audio,
                           'clip2': clip2,
                           'video_title': video_title,
                           'songNumber': playingSongNum,
                           'songDuration': videoDuration,
                           'ffmpeg_opts':
                               {
                                   'before_options': f'-ss {str(hours)}:{str(minutes)}:{str(seconds)} -reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
                                   'options': '-vn'
                               },
                           'skipMessage': "notNone"})  # )
                    break
        except:
            loop.create_task(messageHandler(ctx=ctx, lines=[" @#F Failure: @#V try again."]))
            pass
        counter = -1
        for each in stopArray:
            counter += 1
            if each == ctx.guild.id:
                stopArray.pop(counter)
                break
        await asyncio.sleep(0.5)
        return

    async def getChannel(ctx):
        global sysChannel, megaArray
        channel = None
        try:
            channel = ctx.message.author.voice.channel
        except:
            try:
                channel = ctx.author.voice.channel
            except:
                pass
            pass
        return channel

    async def getVoice(ctx, channel):
        global sysChannel, megaArray
        if channel is None or not channel or channel == "" or channel == None:
            try:
                channel = ctx.message.author.voice.channel
            except:
                try:
                    channel = message.author.voice.channel
                except:
                    pass
                return
        voice = discord.utils.get(ctx.guild.voice_channels, name=channel.name)
        voice_client = discord.utils.get(bot.voice_clients, guild=ctx.guild)
        if voice_client is None or type(voice_client) is None:
            try:
                await voice_client.connect()
            except:
                try:
                    await voice.connect()
                except:
                    pass
                pass
            else:
                await voice_client.move_to(channel)
                try:
                    await voice_client.move_to(channel)
                except:
                    try:
                        await voice.move_to(channel)
                    except:
                        pass
                    pass
        voice_client = discord.utils.get(bot.voice_clients, guild=ctx.guild)
        return voice_client

    async def splitword(word):
        return [char for char in word]

    async def getClip(stringy):
        music_name = stringy
        query_string = urllib.parse.urlencode({"search_query": music_name})
        formatUrl = urllib.request.urlopen("https://www.youtube.com/results?" + query_string)
        search_results = re.findall(r"watch\?v=(\S{11})", formatUrl.read().decode())
        clip2 = "https://www.youtube.com/watch?v=" + "{}".format(search_results[0])
        return clip2

    async def getVideoTitle(clip2, returnB=None, nocheck=0, video_title=None, mode="load", spopifoo=None):
        global ydl_opts, megaArray
        if nocheck == 0:
            videoData = await referenceDB(clip2, video_title, None, mode, spopifoo)
            if videoData is not None and videoData[1] is not None and videoData[1] != "None":
                if mode != "loadmatch" and mode != "spopify":
                    print(f"{Style.RESET_ALL}{Fore.LIGHTGREEN_EX}Found data for {Fore.YELLOW}{videoData[1]}{Fore.LIGHTGREEN_EX} in local database!")
                if returnB is None:
                    return videoData[1],
                elif returnB == "clip2" and (mode=="loadmatch" or mode == "spopify"):
                    return videoData[0], videoData[1], videoData[2], videoData[3]
                elif returnB == "clip2" or mode == "load" and returnB != "notNone":
                    return videoData[0], videoData[1], videoData[2],
                else:
                    return videoData[1], videoData[2]
            #elif returnB == "clip2":
            #    if mode == "loadmatch":
            #        return None, None, None, None
            #    return None, None, None, None

        if clip2 is None and video_title is not None:
            clip2 = await getClip(video_title)
        with YoutubeDL(ydl_opts) as ydl:
            try:
                info_dict = ydl.extract_info(clip2, download=False)
                video_title = info_dict.get('title', None)
                video_duration = info_dict.get('duration', None)
                print(str(clip2))
                loop.create_task(referenceDB(clip2, video_title, video_duration, "save"))
                if returnB is None:
                    return video_title
                else:
                    return video_title, video_duration
            except DownloadError:
                if returnB is None:
                    return "error 298"
                else:
                    return "error 298", ""

    async def nameHandler(ctx, commandPrefix=None, specialCharacter=None, guildObject=None, clear=0, p_guild=None):
        global megaArray, serverData
        if clear == 1:
            specialCharacter = ""
            if p_guild is not None:
                try:
                    await p_guild.me.edit(nick=f"Muse{specialCharacter}IT" + "  (" + commandPrefix + ")")
                    print(f"{Style.RESET_ALL}{Fore.LIGHTGREEN_EX}Nick successfully set for"
                          f" {Style.RESET_ALL}{Fore.LIGHTBLUE_EX}" + str(p_guild.name))
                except:
                    print(f"{Style.RESET_ALL}{Fore.LIGHTRED_EX}Unable to set nick for"
                          f" {Style.RESET_ALL}{Fore.YELLOW}" + str(p_guild.name))
                    pass
                return
            for guild in bot.guilds:
                commandPrefix = '1!'
                guildID = guild.id
                for key in serverData:
                    if key[0] == guildID:
                        commandPrefix = key[1]
                        if specialCharacter is None:
                            specialCharacter = ""
                        try:
                            await guild.me.edit(nick=f"Muse{specialCharacter}IT" + "  (" + commandPrefix + ")")
                            print(f"{Style.RESET_ALL}{Fore.LIGHTGREEN_EX}Nick successfully set for"
                                  f" {Style.RESET_ALL}{Fore.LIGHTBLUE_EX}" + str(guild.name))
                        except:
                            print(f"{Style.RESET_ALL}{Fore.LIGHTRED_EX}Unable to set nick for"
                                  f" {Style.RESET_ALL}{Fore.YELLOW}" + str(guild.name))
                            pass
                        break
            return
        if specialCharacter is None:
            specialCharacter = ""
        if guildObject is None:
            guildObject = ctx.guild
        if commandPrefix is None:
            commandPrefix = '1!'
            for key in serverData:
                if key[0] == ctx.guild.id:
                    commandPrefix = key[1]
        for each in megaArray:
            if each[0][0][0] == guildObject.id:
                shuffle = each[0][2]
                if specialCharacter != "🔀":
                    if shuffle == 1:
                        specialCharacter = "🔀"
        await ctx.guild.me.edit(
            nick=f"Muse{specialCharacter}IT" + "  (" + commandPrefix + ")")
        return


    async def playingLoop(ctx, voice, server, ProjectFFMPEG, audio,
                          clip2, video_title, songNumber, songDuration, ffmpeg_opts=ffmpeg_opts, skipMessage=None):
        global megaArray, rrt, stopArray, playingEpoch
        counter = -1
        for each in stopArray:
            if each == ctx.guild.id:
                counter += 1
                print(f"P{ctx.guild.name} stopArray counter: {counter}")
                if counter > 0:
                    print(f"P{ctx.guild.name} stopArray counter: sent return")
                    return
        counter = -1
        #print("here")
        for each in playingEpoch:
            counter += 1
            if each[0] == ctx.guild.id:
                playingEpoch.pop(counter)
        playingEpoch.append([ctx.guild.id, time.time()])
        await asyncio.sleep(1)

        if clip2 == "NaN":
            return
        #print("here2")
        for each in megaArray:
            if each[0][0][0] == ctx.guild.id:
                voice = each[0][0][3]
                break
        tryVar = False
        try:
            tryVar = voice.is_connected()
        except:
            tryVar = False
        if not voice or voice is None or not tryVar:
            try:
                channel = await getChannel(ctx)
                voice = await getVoice(ctx, channel)
                loop.create_task(arrayBuilder(ctx, audio=audio, voice_client=voice, clip2=clip2, video_title=video_title,
                                   videoDuration=songDuration))
            except:
                pass
            loop.create_task(arrayBuilder(ctx, audio=audio, voice_client=None, clip2=clip2, video_title=video_title,
                               videoDuration=songDuration))
        try:
            if voice.is_playing():
                voice.stop()
        except:
            channel = await getChannel(ctx)
            voice = await getVoice(ctx, channel)
            loop.create_task(arrayBuilder(ctx, audio=audio, voice_client=voice, clip2=clip2, video_title=video_title,
                                          videoDuration=songDuration))
            pass
        if songNumber is not None:
            stringy = str(songNumber)
        else:
            stringy = ""
        if skipMessage is None:
            if songDuration is None:
                video_title, video_duration = await getVideoTitle(clip2, returnB="notNone")
            commandPrefix = await determine_prefix(bot, ctx.message)

            loop.create_task(messageHandler(ctx=ctx, lines=[
                    " @#F Now Playing: " +
                    f" @#V {stringy}. - [" + str(video_title) + f"]({clip2})",
                    f" @#F Duration: @#V {str(lessOrMore(int(math.floor(float(int(songDuration) / 60)))))}:"
                    f"{str(lessOrMore(int(math.floor(float(60 * float(r'0.' + str(float(int(songDuration) / 60)).split(r'.')[1][:2]))))))}"
                    f" ({commandPrefix}seek 00:00-"
                    f"{str(lessOrMore(int(math.floor(float(int(songDuration) / 60)))))}:"
                    f"{str(lessOrMore(int(math.floor(float(60 * float(r'0.' + str(float(int(songDuration) / 60)).split(r'.')[1][:2]))))))}"
                    f")"]))

        voice.play(FFmpegPCMAudio(executable=ProjectFFMPEG, source=audio, **ffmpeg_opts))
        print(voice)
        await arrayBuilder(ctx, isPlaying=1)
        #voice.pause()
        #await asyncio.sleep(0.5)
        #voice.resume()
        #for each in megaArray:
        #    if each[0][0][0] ==
        while voice.is_playing() or voice.is_paused():
            await asyncio.sleep(0.5)
            for each in stopArray:
                if each == ctx.guild.id:
                    print("killed voice")
                    voice.pause()
                    return
            if not voice.is_playing() and not voice.is_paused() and voice.is_connected():
                print("playingloop - append to stoparray, break, next function")
                stopArray.append(ctx.guild.id)
                await next(ctx)
                voice.pause()
                break
        return

    def lessOrMore(someInteger):
        someString = str(someInteger)
        if someInteger < 10:
            someString = "0" + str(someInteger)
        return someString



    async def addlist2(ctx=None, url=None):
        global megaArray
        waitcounter = 0
        for each in megaArray:
            waitcounter = waitcounter + 1
        query = parse_qs(urlparse(url).query, keep_blank_values=True)
        try:
            playlist_id = query["list"][0]
        except KeyError:
            loop.create_task(messageHandler(ctx=ctx, lines=[f"@#F Error: @#V Can't find list in {url}"]))
            return
        youtube = build("youtube", "v3", developerKey="#")
        request = youtube.playlistItems().list(
            part="snippet",
            playlistId=playlist_id,
            maxResults=50
        )
        playlist_items = []
        songList = []
        counter = 0
        for each in megaArray:
            if each[0][0][0] == ctx.guild.id:
                songList = each[0][0][2]
                counter = 0
                for each in songList:
                    counter = counter + 1
        if songList == []:
            counter = 0
        while request is not None:
            response = request.execute()
            playlist_items += response["items"]
            request = youtube.playlistItems().list_next(request, response)
        print(f"total: {len(playlist_items)}")
        links = [f'https://www.youtube.com/watch?v={t["snippet"]["resourceId"]["videoId"]}&list={playlist_id}&t=0s'
                 for t in playlist_items]
        counter3 = counter
        counter = 0
        counter2 = 0
        boolyBool = False
        messageSent = await ctx.send("```Processed: " + str(counter) + "/" + str(len(playlist_items)) + "```")
        for link in links:
            clip2 = link
            videoData = await referenceDB(clip2, None, None, "load")
            if videoData is not None:
                video_title, video_duration = videoData[1], videoData[2]
                print(f"{Style.RESET_ALL}{Fore.LIGHTGREEN_EX}Found data "
                                      f"for {Fore.YELLOW}{videoData[1]}{Fore.LIGHTGREEN_EX} in local database!")
            else:
                video_title, video_duration = await getVideoTitle(clip2, returnB="NotNone")
            if "error 298" != str(video_title):
                counter3 = counter3 + 1
                counter = counter + 1
                counter2 = counter2 + 1
                loop.create_task(add2(ctx, f_clip=clip2, f_title=video_title, video_duration=video_duration,
                           addlistcmd="notnone", noLinkCheck=1))
                #await asyncio.sleep(0.25 * waitcounter)
                if (counter2 > int(float(len(playlist_items) / (float(len(playlist_items)/5))))):
                    if bool(boolyBool):
                        boolyBool = False
                        loop.create_task(messageSent.edit(
                            content="```Processed: " + str(counter) + "/" + str(len(playlist_items)) + "\n" + str(
                                video_title)[:25] + "...```" + "_PLEASE WAIT_"))
                        #await asyncio.sleep(0.25)
                    else:
                        boolyBool = True
                        loop.create_task(messageSent.edit(
                            content="```Processed: " + str(counter) + "/" + str(len(playlist_items)) + "\n" + str(
                                video_title)[:25] + "...```"))

                    counter2 = 0
        localVideoData = []
        await messageSent.edit(content="```-Added: \n" + str(counter) + " / " + str(
            len(playlist_items)) + "\nsongs from youtube playlist\nto the current playlist```")
        return

    async def rebuildPlaylist(ctx, file=None, listT=None):
        global megaArray
        if file is None and listT is None:
            return
        if listT is not None:
            PlayList = listT
        else:
            PlayList = numpy.load(file, allow_pickle=True)
            PlayList = PlayList.tolist()
        newList = []
        for each in PlayList:
            clip2 = each[0]
            position = each[1]
            title = each[2]
            localVideoData = referenceDB(clip2, None, None, "load")
            if localVideoData is not None:
                exist = 1
                newList.append([localVideoData[0], position, localVideoData[1], localVideoData[2]])
                break
            if exist == 0:
                title, duration = await getVideoTitle(clip2, returnB="notnone")
                newList.append([clip2, position, title, duration])
        if file is not None:
            numpy.save(file, newList, allow_pickle=True)
        # numpy.save(HomeDir + "\Saves\Local_video_data.npy", localVideoData, allow_pickle=True)
        loop.create_task(messageHandler(ctx=ctx, lines=[f"@#F Information: @#V Finished rebuilding playlist."]))
        return newList



    async def referenceDB(clip2, video_title, video_duration, mode, spopifoo=None):
        stupify = []
        spsave = 0
        skipSave = 0
        if clip2 is not None:
            letter = str(str(clip2)[32:33])
            array = numpy.load(HomeDir + f"\Saves\Databases\VideoDB\\{letter}_array.npy", allow_pickle=True)
            array = array.tolist()

            for each in array:
                if str(each[0]) == str(clip2):
                    if mode == "save":
                        skipSave = 1
                        array = []
                        break
                    if mode == "load":
                        video_title = each[1]
                        video_duration = each[2]
                        if video_title is None or video_title == "None":
                            return [None, None, None]
                        return [clip2, video_title, video_duration]
                    if mode == "spopify":
                        if os.path.exists(HomeDir + f"\Saves\Databases\SpotifyDB\\{spopifoo}.npy"):
                            stupify = numpy.load(HomeDir + f"\Saves\Databases\SpotifyDB\\{spopifoo}.npy", allow_pickle=True)
                            stupify = stupify.tolist()
                        video_title = each[1]
                        video_duration = each[2]
                        stupify.append([clip2, video_title, video_duration])
                        numpy.save(HomeDir + f"\Saves\Databases\SpotifyDB\\{spopifoo}.npy", stupify,
                                       allow_pickle=True)
                        return [clip2, video_title, video_duration]

            if mode == "load":
                return None
            if skipSave == 0:
                array.append([clip2, video_title, video_duration])
                numpy.save(HomeDir + f"\Saves\Databases\VideoDB\\{letter}_array.npy", array, allow_pickle=True)
        elif (clip2 is None and video_title is not None) or mode == "loadmatch" or mode == "spopify":
            cases = []
            for each in ascii_lowercase:
                cases.append(each)
            cases.extend(["-","_","0","9","8","7","6","5","4","3","2","1"])
            video_clip = None
            video_duration = None
            titleMatch = None
            for each in cases:
                array = []
                array = numpy.load(HomeDir + f"\Saves\Databases\VideoDB\\{each}_array.npy", allow_pickle=True)
                array = array.tolist()
                counting = -1
                leng = len(array)
                while counting < leng:
                    for key in array:
                        counting += 1
                        if key[2] is None or key[2] == "None" or \
                                key[0] is None or key[0] == "None" or \
                                        key[1] is None or key[1] == "None":
                            array.pop(counting)
                            numpy.save(HomeDir + f"\Saves\Databases\VideoDB\\{each}_array.npy", array, allow_pickle=True)
                            array = numpy.load(HomeDir + f"\Saves\Databases\VideoDB\\{each}_array.npy", allow_pickle=True)
                            array = array.tolist()
                            leng = len(array)
                            counting = -1
                            break
                        percentMatch = int(float(await similar(video_title,key[1])))
                        if mode == "loadmatch":
                            matchThreshold = 90
                        elif mode == "spopify":
                            matchThreshold = 90
                        else:
                            matchThreshold = 90
                        if percentMatch >= matchThreshold:
                            print(f"{Fore.LIGHTGREEN_EX}Percent match for {Fore.LIGHTCYAN_EX}{video_title}"
                                  f" {Fore.LIGHTWHITE_EX}against {Fore.LIGHTCYAN_EX}{key[1]} "
                                  f"{Fore.LIGHTWHITE_EX}was {Fore.LIGHTMAGENTA_EX}{percentMatch}"
                                  f"{Fore.LIGHTWHITE_EX}! {Fore.LIGHTYELLOW_EX}Using video clip and duration from local DB!")
                            video_clip = key[0]
                            video_duration = key[2]
                            video_title = key[1]
                            titleMatch = f"{video_title[:20]}.. ** {percentMatch}% ** Matched {key[1][:20]}.. in local DB"
                            matchThreshold = percentMatch
                            spsave = 1
            if mode == "spopify" and spsave == 1:
                if os.path.exists(HomeDir + f"\Saves\Databases\SpotifyDB\\{spopifoo}.npy"):
                    stupify = numpy.load(HomeDir + f"\Saves\Databases\SpotifyDB\\{spopifoo}.npy", allow_pickle=True)
                    stupify = stupify.tolist()
                    print(str(stupify))
                stupify.append([video_clip, video_title, video_duration])
                print(str(stupify))
                numpy.save(HomeDir + f"\Saves\Databases\SpotifyDB\\{spopifoo}.npy", stupify, allow_pickle=True)
            return [video_clip, video_title, video_duration, titleMatch]
        return None

    async def arrayBuilder(ctx,
                           audio=None, playingSongNum=None, voice_client=None, clip2=None, songList=None,
                           listArray=None, shuffle=None, videoDuration=None, video_title=None, isPlaying=None,
                           quietMode=None):
        global megaArray, sysChannel
        megaCounter = -1
        songNumList = []
        voiceChannel = None
        for each in megaArray:
            megaCounter = megaCounter + 1
            if each[0][0][0] == ctx.guild.id:
                guildID = ctx.guild.id
                voiceChannel = each[0][0][1]
                server = ctx.guild
                quietMode = each[2]
                voice_client_exists = 0
                videoDuration = each[0][7]
                if isPlaying is None:
                    isPlaying = each[1]
                if voice_client is None:
                    voice_client = each[0][0][3]
                    if voice_client is not None:
                        voice_client_exists = 1
                    else:
                        try:
                            userVoiceChannel = ctx.message.author.voice.channel
                            voiceChannel = discord.utils.get(ctx.guild.voice_channels, name=userVoiceChannel.name)
                            voice_client = discord.utils.get(bot.voice_clients, guild=ctx.guild)
                        except:
                            voice_client = None
                            pass
                        if voice_client is not None:
                            voice_client_exists = 1
                if shuffle is None:
                    shuffle = each[0][2]
                if voice_client is not None:
                    voice_client_exists = 1
                if voice_client_exists == 0:
                    voice_client = None
                if listArray is None:
                    listArray = each[0][1]
                if audio is None:
                    audio = each[0][3]
                if playingSongNum is None:
                    playingSongNum = each[0][4]
                if songList is not None:
                    songNumList = songList
                else:
                    songNumList = each[0][0][2]
                if clip2 is None:
                    clip2 = each[0][5]
                if videoDuration is None and clip2 is not None:
                    localVideoData = await referenceDB(clip2, None, None, "load")
                    if localVideoData is not None:
                        videoDuration = localVideoData[2]
                        video_title = localVideoData[1]
                    else:
                        video_title, videoDuration = await getVideoTitle(clip2=clip2, returnB="notNone")
                megaArray.remove(each)
                break
        if songNumList == []:
            if clip2 is not None and video_title is not None:
                songNumList = [[str(clip2), 1, str(video_title), str(videoDuration)]]
        megaArray.append( # MY fING HEADSET
            [[[ctx.guild.id, voiceChannel, songNumList, voice_client, ctx.guild, ctx], listArray, shuffle, audio,
              playingSongNum, clip2, video_title, videoDuration], isPlaying, quietMode]
        )       #4              5           6           7
        return megaArray

    async def add2(ctx, retrplz=False, f_clip=None, f_title=None, nosend="NaN",
                   SongNumber=None, addlistcmd=None, video_duration=None, noLinkCheck=None):
        global megaArray
        songNumList = []
        skip = 0
        if ("http" in ctx.message.content and ("youtube" in ctx.message.content \
                                               or "spotify" in ctx.message.content) and \
                "playlist" in ctx.message.content and noLinkCheck is None):
            loop.create_task(messageHandler(ctx=ctx, lines=[f" @#F Hmm... @#V Please use the addlist "
                                                 f"command for youtube and spotify **playlist** links."], quietMode=2))
            return
        if addlistcmd is not None and (f_clip is not None or f_title is not None) and \
                (f_title is None or video_duration is None):
            for each in localVideoData:
                for key in each:
                    if (key == f_clip and f_clip is not None) or (key == f_title and f_title is not None):
                        f_clip = each[0]
                        f_title = each[1]
                        video_duration = each[2]
        if f_clip is None and f_title is None:
            counter = -1
            clipStr = ""
            for each in str(ctx.message.content).split(" "):
                counter = counter + 1
                if counter != 0:
                    clipStr = clipStr + " " + each
            clip2 = None
            skip = 0
            if "http" in clipStr.lower() and "youtube.com" in clipStr.lower() and "://" in clipStr.lower():
                print("link")
                clipStr2 = clipStr.split("watch?v=")
                print(str(len(clipStr2)))
                if len(clipStr2) > 1:
                    f_clip = "http://www.youtube.com/watch?v=" + clipStr2[1][:11]
                    f_title, video_duration = await getVideoTitle(clip2=f_clip, returnB="notNone")
                    print(str(clip2))
                    clip2 = f_clip
                    skip = 1
            if skip == 0:
                if counter <= 0:
                    loop.create_task(messageHandler([f""
                    f" @#F Error: @#V Please specify something to add to the list."]))
                    return
                f_clip, f_title, video_duration, dataString = await getVideoTitle(clip2=f_clip, returnB="clip2",
                                                                                  video_title=clipStr,
                                                                                  mode="loadmatch", spopifoo=None)
                if f_clip is None or f_title is None or video_duration is None:
                    f_clip = await getClip(clipStr)
                    f_title, video_duration = await getVideoTitle(clip2=f_clip, returnB="notNone")

        video_title = f_title
        exists = 0
        for each in megaArray:
            if each[0][0][0] == ctx.guild.id and exists != 1:
                exists = 1
                songNumList = each[0][0][2]
                if songNumList is not None and songNumList != []:
                    if len(songNumList) > 0:
                        songNumList.append([f_clip, len(songNumList) + 1, video_title, video_duration])
                else:
                    if video_duration is None:
                        if f_clip is None:
                            f_clip = await getClip(f_title)
                        video_title, video_duration = await getVideoTitle(f_clip, returnB="notNone")
                    songNumList = [[f_clip, 1, video_title, video_duration]]
        if exists == 0:
            songNumList = [[f_clip, 1, video_title, video_duration]]
            await arrayBuilder(ctx=ctx, playingSongNum=1, clip2=f_clip, songList=songNumList,
                               video_title=video_title,
                               videoDuration=video_duration)
        else:
            await arrayBuilder(ctx=ctx, songList=songNumList)
        if retrplz is True or retrplz is not False:
            return f_clip, video_title, SongNumber
        if nosend != "NaN":
            commandPrefix = await determine_prefix(bot, ctx.message)
            await messageHandler(ctx=ctx, lines=[" @#F Added: @#V " + f"```{formatString}\n" + str(video_title) + \
                                                 "```\n to the playlist \n Position : " + str(len(songNumList)) + \
                                                 f"\nYou can use {commandPrefix}skipto {str(len(songNumList))}"])
        return

    async def r_range(range1, range2, ctx):
        global sysChannel, megaArray
        msgStr = ""
        songListCounter2 = 0
        megaExist = 0
        songremovedcounter = 0
        songListNew = []
        for each in megaArray:
            guildID = each[0][0][0]
            if guildID == ctx.message.guild.id:
                songList = each[0][0][2]
                playingSongNum = each[0][4]
                megaExist = 1
                newSongNum = 0
                for key in songList:
                    songListCounter2 = songListCounter2 + 1
                    if songListCounter2 < range1 or songListCounter2 > range2:
                        newSongNum = newSongNum + 1
                        songListNew.append([key[0], newSongNum, key[2], key[3]])
                    else:
                        songremovedcounter = songremovedcounter + 1
                await arrayBuilder(ctx=ctx, songList=songListNew)
                break

        if megaExist == 0:
            await messageHandler(ctx=ctx, lines=[" @#F Error : @#V There's nothing to remove"])
            return
        await messageHandler(ctx=ctx,
                             lines=[f"@#F Complete: @#V Removed {songremovedcounter} songs from the playlist"])
        return

    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   ####################################################################################
    #   #   #####################################################################################





async def wrappedConnect3(f, bottyfus):
    global globalIteratorLimit, botIterator, botius
    botIterator = 0
    bot = bottyfus[1]
    bottycounter = -1
    newBotius = []
    for bottyBots in bottyfus:
        bottycounter += 1
        if bottycounter != 0:
            newBotius.append(bottyBots)
    botius = newBotius
    bot = botius[0]
    newBotius = None
    globalIteratorLimit = bottycounter - 1
    pop = False
    @bot.event
    async def on_command_error(ctx, error):

        if isinstance(error, CommandNotFound):
            return
        if isinstance(error, KeyError):
            return
        if isinstance(error, UnboundLocalError):
            return
        var = traceback.format_exc()
        raise error

    @bot.event
    async def on_message(message):
        stopScrape = False
        botIterator = 0
        for bottsbotts in botius:
            if not message.author.bot and bottsbotts == botius[0]:
                prefix = await determine_prefix(bot, message)
                if prefix == '' or utilbotDisable == 1:
                    return

                if str(message.content).split(" ")[0] == "^collage":
                    await bot.process_commands(message)
                    return
                if str(message.content[:len(prefix)]) == prefix:
                    if message.author.id == 226925882168705025 or message.author.id == 855613733854642237:
                        if str(message.content).split(" ")[0] == str(prefix + "cserver"):
                            print("registered cjcarlosTTV cmd")
                            await bot.process_commands(message)
                            return
                    if message.author.id == 829088888488198214 or message.author.id == 855613733854642237:
                        if str(message.content).split(" ")[0] == str(prefix + "fmysstupfam"):
                            print("registered powder cmd")
                            await bot.process_commands(message)
                            return
                    if message.author.id == 246892047284436992 or message.author.id == 855613733854642237:
                        if isinstance(message.channel, discord.channel.DMChannel):
                            print(f"{Style.RESET_ALL}{Fore.YELLOW}" + str(message.author.name) + " DIRECT MESSAGED: " + str(
                                message.content))
                            return
                        for boat in botius:
                            print("here " + str(boat.user.id) + f" against {botius[0].user.id}")
                            if boat.user.id == botius[0].user.id:
                                 sysChannelIDS = [871650162655780864, 871650184881401876, 871650226828619808]
                                 if int(message.author.id) == int(855613733854642237) or \
                                        int(message.author.id) == int(246892047284436992):
                                    if str(message.content).lower()[1:] == "stopscrape":
                                        stopScrape = not stopScrape
                                    if not boat == botius[0]:
                                        await asyncio.sleep(0.1)
                                    if boat == botius[botIterator]:  # or bot == bots[botIterator2]:
                                        combinedSysChannel = await botius[botIterator].fetch_channel(866356303626240050)
                                        for id in sysChannelIDS:
                                            if int(id) == int(message.channel.id):
                                                txt = str(message.content).replace("@", "<AT>")
                                                txt = txt.replace("```", "")
                                                await combinedSysChannel.send(
                                                    "#" + str(botius[botIterator].user.discriminator) + "```" + str(
                                                        message.channel.name) + " - " \
                                                    + r"#" + str(message.author.name) + str(message.author.discriminator) \
                                                    + r": " + str(message.content) + "```")
                                                break

                                    if boat == botius[0]:
                                        print(str(message.content))
                                        if pop == False or str(message.content).lower()[1:] == ">?>?>?":
                                            args = {
                                                'ctx': message,
                                                'f': boat.process_commands,
                                                't': asyncio.create_task,
                                                'count': 1,
                                                'waittime': 0.1
                                            }
                                            kwargs = {
                                                'message': message,
                                            }
                                            #new_eventloop = asyncio.new_event_loop()
                                            #new_eventloop.run_until_complete(await asyncio.gather(
                                            #    *(
                                            await asyncio.ensure_future(taskBuilder2(**args, kwargs=kwargs))#))#)

                                            #new_eventloop = asyncio.new_event_loop()
                                            #new_eventloop.run_until_complete(
                                            #await boat.process_commands(message)#)
                                            break
                                    return
                        else:
                            await message.channel.send("you are not Serbz.")
                            break
            return



    @bot.command(name="genalottxt")
    async def genalottxt(ctx):
        args = {
            'ctx': ctx,
            'f': generateText,
            't': asyncio.create_task,
            'count': 30,
            'waittime': 10
        }
        kwargs = {
            'ctx': ctx,
            'botarrayswitch': "notNone"
        }
        await asyncio.gather(*(await asyncio.ensure_future(taskBuilder2(**args, kwargs=kwargs))))
        return
    @bot.command(name="gtalot")
    async def genalottxt(ctx):
        args = {
            'ctx': ctx,
            'f': generateText,
            't': asyncio.create_task,
            'count': 30,
            'waittime': 10
        }
        kwargs = {
            'ctx': ctx,
            'botarrayswitch': "notNone"
        }
        await asyncio.gather(*(await asyncio.ensure_future(taskBuilder2(**args, kwargs=kwargs))))
        return
    @bot.command(name="sys-status")
    async def syssettings(ctx):
        if ctx.message.author.id == 246892047284436992 or ctx.message.author.id == 855613733854642237:
            await messageHandler(ctx=ctx, lines=[f" @#F System Settings: @#V "
                            f"Servers: {len(bot.guilds)}\n"
                            f"Latency: {round(bot.latency*1000, 2)}ms\n"
                            f"Memory Usage: {str(round(psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2, 2))}mb/16000mb\n"
                            f"quietOut: {quietOut}\n"
                            f"accTimers: {accTimers}\n"
                            f"timers: {timers}\n"
                            f"bots: List[Bot] length: {len(bots)}\n"
                            f"bot array prefix: ^ \n"
                            f"current active timers: {len(counterArray)} \n"
                            f"musicBotDisable: {musicbotDisable}\n"
                            f"utilbotDisable: {utilbotDisable}\n"
                            f"current entries in megaArray: {len(megaArray)} \n"], quietMode=2)
        return
    @bot.command(name="delmsgs")
    async def deletemsgs(ctx):
        global botData, deleteinprogress
        if deleteinprogress == 0:
            deleteinprogress = 1
            if ctx.message.author.id != 246892047284436992 and ctx.message.author.id != 855613733854642237:
                deleteinprogress = 0
                print("not serbz")
                return
            else:
                number = str(ctx.message.content).split(" ")[1]
                if str(ctx.message.content).split(" ")[1] is not None and str(ctx.message.content).split(" ")[
                    1] != [] and \
                        str(ctx.message.content).split(" ")[1] != "":
                    mgs = []  # Empty list to put all the messages in the log
                    number = int(number)  # Converting the amount of messages to delete to an integer
                    async for x in (await getCTX2(ctx)).history(limit=number):
                        mgs.append(x)
                    taskloops = []
                    count = 0
                    for every in mgs:
                        count += 1
                        taskloops.append(delMessageTask(ctx, every, count))
                    await asyncio.gather(*taskloops)
                    stringy = ""
                    for each in botData:
                        stringy += f"\n bot: {each[2]}#{each[0]} completed {each[1]} tasks"
                    await messageHandler(ctx=ctx, lines=[f" @#F Process Complete: @#V Deleted {count} messages",
                                                         f" @#F Stats: @#V {stringy}"], cloners=1)
            deleteinprogress = 0
        else:
            await messageHandler(ctx=ctx, lines=[f" @#F Error: @#V deletion command already in progress. Please wait."], cloners=1)
        return

    @bot.command(name="string")
    async def splitsBotsStrings(ctx):
        splStringsBots = str(ctx.message.content).split(" ")
        counter = -1
        for bot in botius:
            counter = counter + 1
        taskloops = []
        counter2 = -1
        for key in splStringsBots:
            counter2 = counter2 + 1
            if counter2 > counter:
                counter2 = 0
            # bots[counter2]
            taskloops.append(stringSplBots(ctx, botius[counter2], key))
        await asyncio.gather(*taskloops)
        return

    async def stringSplBots(ctx, bot, stringy):
        try:
            await (await bot.fetch_channel(int(ctx.message.channel.id))).send(
                str(bot.user.id) + "\n" + str(stringy))
        except:
            pass
        return

    @bot.command(name='oauth')
    async def oauths(ctx):
        for bot in botius:
            ctx2 = await getCTX2(ctx)
            await ctx2.send(
                f"https://discord.com/api/oauth2/authorize?client_id={str(bot.user.id)}&permissions=8&scope=bot")
        return

    @bot.command(name='>?>?>?')
    async def restart(ctx):
        if str(ctx.author.name).lower() == 'serbz' and (
                str(ctx.author.discriminator) == '0001' or str(ctx.author.discriminator) == '0002'):
            await messageHandler(ctx=ctx, lines=["@#F RESTART INITIATED: @#V disconnecting voice clients, setting names. "], system=1)
            with open(HomeDir + r"\botToggle.txt", "w", encoding='utf8',
                      errors="ignore") as text_file:
                text_file.write("1")
            text_file.close()
            os.execv(sys.executable, ['python'] + sys.argv)
            SystemExit()
            sys.exit()
        return

    @bot.command(name="claim")
    async def claim(ctx):
        ctxSpl = str(ctx.message.content).split(" ")
        counter = -1
        for each in ctxSpl:
            guildName = "NaN"
            skip = 0
            counter = counter + 1
            if counter != 0:
                claim, claimedBy, claimedByID = await checkClaim(ctx, int(each))
                for guild in botius[0].guilds:
                    if int(guild.id) == int(each):
                        guildName = str(guild)
                if guildName == "NaN":
                    await ctx.send("No Access to any guild with ID: " + str(each))
                    skip = 1
                if claim:
                    await ctx.send("Guild " + str(guildName) + " **is already** claimed by: " + str(
                        claimedBy) + " with user ID: " + str(claimedByID) + "**")
                    skip = 1
                if skip != 1:
                    with open(HomeDir + r"\Saves\Databases\ClonerDB\Claims.txt", "a", encoding='utf8', errors="ignore") as text_file:
                        text_file.write("\n" + str(ctx.message.author.id) + " " + str(each) + " " +
                                        str(ctx.message.author.name) + " " + str(guildName))
                        await ctx.send("Guild: " + str(guildName) + " **is now** claimed by: " + str(
                            ctx.message.author.name) + " with user ID: " \
                                       + str(ctx.message.author.id))
                        await asyncio.sleep(1.75)
                    text_file.close()
        return

    @bot.command(name="unclaim")
    async def unclaim(ctx):
        ctxSpl = str(ctx.message.content).split(" ")
        for each in ctxSpl:
            skip = 1
            guildName = "NaN"
            for guild in botius[0].guilds:
                if str(guild.id) == str(each):
                    guildName = guild
            if str(each).lower() != "unclaim" and guildName != "NaN":
                claimed, claimed_user, claimed_userID = await checkClaim(ctx, str(each))
                if str(claimed_userID) == str(ctx.message.author.id) and claimed:
                    line = await getClaimLine(each)
                    await claimsUpdater(line)
                    await asyncio.sleep(2)
                    await ctx.send("Guild: " + str(guildName) + " with ID: " + str(each) + " **unclaimed**.")
                    break
                elif not claimed:
                    await asyncio.sleep(2)
                    await ctx.send(
                        "Guild: " + str(guildName) + " with ID: " + str(each) + " **was already unclaimed**.")
                elif str(claimed_userID) != str(ctx.message.author.id):
                    await asyncio.sleep(2)
                    await ctx.send(
                        "Guild: " + str(guildName) + " with ID: " + str(each) + " **is already claimed by: " +
                        str(claimed_user) + " with ID: " + str(claimed_userID) + "**")
        return


    @bot.command(name="mbot")
    async def disablembot(ctx):
        global musicbotDisable
        if ctx.message.author.id == 855613733854642237 or ctx.message.author.id == 246892047284436992:
            if musicbotDisable == 0:
                musicbotDisable = 1
            else:
                musicbotDisable = 0
            await messageHandler(ctx=ctx, lines=[f" @#F Done: @#V musicbotDisable = {musicbotDisable} "])
        return
    @bot.command(name="cserver")
    async def cserver(ctx):

        authorObj = ctx.message.author
        ServerName = None
        image_types = ["png", "jpeg", "gif", "jpg"]
        skip = 1
        while ServerName is None:
            settingString = "Server Name"
            instructString = ""
            skipConfirmation = False
            ServerName = await userInput(ctx, authorObj, settingString, instructString, skipConfirmation)
        ServerTopic = None
        while ServerTopic is None:
            settingString = "Server Topic"
            instructString = ""
            skipConfirmation = False
            ServerTopic = await userInput(ctx, authorObj, settingString, instructString, skipConfirmation)
        specialChannelList = None
        while specialChannelList is None:
            settingString = "Special Channel List"
            instructString = "Please comma seperate channel names (ie. name1, name2). \n Or just say None for no special channels"
            skipConfirmation = True
            setting = await userInput(ctx, authorObj, settingString, instructString, skipConfirmation)
            specialChannelList = await listConfirmation(ctx, setting, authorObj)
        specialRolesList = None
        while specialRolesList is None:
            settingString = "Special Roles List"
            instructString = "Please comma seperate role names, and list in order (ie. name1, name1 Has A Higher Role Than name2, name2). \n Or just say None for no special channels"
            skipConfirmation = True
            setting = await userInput(ctx, authorObj, settingString, instructString, skipConfirmation)
            specialRolesList = await listConfirmation(ctx, setting, authorObj)
        serverImage = None
        try:
            os.mkdir(HomeDir + f"\Saves\ServerCreation\\")
            os.mkdir(HomeDir + f"\Saves\ServerCreation\{ctx.message.author.id}_temp")
        except:
            pass
        while serverImage is None:
            settingString = "Server Icon"
            instructString = "Would you like to provide a server Icon? if so paste it in the chat or say no. \n If an icon is" \
                             " not provided, no worries, we will get one for you related to your topic."
            skipConfirmation = True
            message, messageObj = await userInput(ctx, authorObj, settingString, instructString, skipConfirmation, returnObj=2)
            saved = 0
            image_types = ["jpg", "png"]
            if message.lower() != "no":
                for attachment in messageObj.attachments:
                    for imgtype in image_types:
                        if attachment.filename.lower().endswith(imgtype):
                            saved = 1
                            await attachment.save(HomeDir + f"\Saves\ServerCreation\{ctx.message.author.id}_temp\{ServerName}Banner.{imgtype}")
                            serverImage = HomeDir + f"\Saves\ServerCreation\{ctx.message.author.id}_temp\{ServerName}Banner.{imgtype}"
                            ctx2 = await getCTX2(ctx)
                            await ctx2.send(file=discord.File(serverImage), content="")
                            break
            else:
                saved = 0
                urlArray = []
                DIR = HomeDir + f"\Saves\ServerCreation\{ctx.message.author.id}_temp\\"
                if saved == 0:
                    ctx2 = await getCTX2(ctx)
                    await ctx2.send("Please wait")
                    image, imagelist = await createCollage(ctx, [ServerTopic], DIR, numbered=True, returnlist=True)
                    ctx2 = await getCTX2(ctx)
                    settingString = "Server Icon"
                    instructString = "Would you like one of these images? if so reply with a number. else, say none"
                    await ctx2.send(file=discord.File(image), content="")
                    message, messageObj = await userInput(ctx, authorObj, settingString, instructString,
                                                          skipConfirmation, returnObj=2)
                    picnum = 0
                    try:
                        number = int(message)
                        if number > 0:
                            picnum = number
                    except:
                        pass

                    if picnum <= 0 or message.lower() == "none":
                        await ctx2.send("Would you like to proceed without a server icon?")
                        message, messageObj = await userInput(ctx, authorObj, settingString, instructString,
                                                              skipConfirmation, returnObj=2)
                        if message.lower() == "yes":
                            serverImage = ""
                    else:
                        ctx2 = await getCTX2(ctx)
                        for each in imagelist:
                            if each[1] == picnum:
                                url = each[0]
                                print(url)
                                serverImage = f"{url}"
                                await ctx2.send(file=discord.File(serverImage), content="Server Icon set.")
                                break
        serverID = None
        while serverID is None:
            settingString = "Server ID"
            instructString = "Please specify a server ID or say 'this' to use the current server or say 'cancel' or 'stop' to discontinue the current opteration."
            skipConfirmation = True
            message, messageObj = await userInput(ctx, authorObj, settingString, instructString, skipConfirmation,
                                                  returnObj=2)
            if 'this' in message.lower():
                    serverID = ctx.message.channel.guild.id
            elif 'cancel' in message.lower() or 'stop' in message.lower():
                    return
            else:
                serverID = int(message)
            counter = 0
            for botsbots in botius:
                for guild in botsbots.guilds:
                    if guild.id == serverID:
                        servercreatebots.append(botsbots)
                        counter+=1
            if counter <= 0:
                ctx2 = await getCTX2(ctx)
                await ctx2.send("Not enough bots in selected guild. 0 or less.")
                return
            ctx2 = await getCTX2(ctx)
            await ctx2.send(f"{counter} bots in guild. Beginning creation.")
        await createServerWithInfo(ctx, serverID, serverImage, specialRolesList, specialChannelList, ServerTopic, ServerName)
        return

    async def createServerWithInfo(ctx, serverID, serverImage, specialRolesList, specialChannelList, ServerTopic, ServerName):
        defaultVoiceChannels = ["General", str(ServerTopic)]
        defaultTextChannels = ["general", "bot-spam", str(ServerTopic)]
        defaultRoles = []
        defaultCats = ["General", str(ServerTopic)]

        return

    @bot.command(name="collage")
    async def collagecmd(ctx):
        if len(str(ctx.message.content).split(" ")) > 1:
            counter2=0
            for each in str(ctx.message.content).split(" "):
                counter2+=1
            counter = 0
            alisst = []
            for each in str(ctx.message.content)[9:].split(","):
                alisst.append(each.replace(" ", "+"))
            DIR = HomeDir + f"\Saves\ServerCreation\{ctx.message.author.id}_temp\\"
            image = await createCollage(ctx, alisst, DIR, numbered=True)

            #ctx2 = await getCTX2(ctx)
            await ctx.send(file=discord.File(image), content="")
            return


    async def listConfirmation(ctx, setting, authorObj):
        ctx2 = await getCTX2(ctx)
        if str(setting).lower() != "none":
            setting = str(setting).strip().split(",")
        else:
            setting = []
        if type(setting) is list and setting != []:
            stringy = ""
            ctx2 = await getCTX2(ctx)
            newSetting = []
            for each in setting:
                if each != "" and each is not None and each != "," and not each.isspace():
                    stringy += f"- {each.strip()}\n\n"
                    newSetting.append(each)
            setting = newSetting
            await messageHandler(ctx=ctx2, lines=[f" @#F You specified: @#V ```{formatString}\n{stringy}``` ", "@#F Confirm: @#V "
                            f"is This correct?"])
            setting = await confirmYN(ctx, setting, authorObj)
        else:
            await messageHandler(ctx=ctx2, lines=[f" @#F Hmm: @#V You specified nothing, is this correct?"])
            setting = []
            setting = await confirmYN(ctx, setting, authorObj)
        return setting

    async def confirmYN(ctx, setting, authorObj):
        while ctx.channel.last_message.author != authorObj:
            await asyncio.sleep(1)
        string =  str(ctx.channel.last_message.content).lower()
        if string == "no":
            return None
        elif string == "yes":
            return setting
    async def userInput(ctx, authorObj, settingString, instructString, skipConfirmation, returnObj=0):
        ctx2 = await getCTX2(ctx)
        await messageHandler(ctx=ctx2, lines=[f" @#F Specify: @#V {settingString}.\n{instructString}"])
        while ctx.channel.last_message.author != authorObj:
            await asyncio.sleep(1)
        if returnObj == 0:
            setting = ctx.channel.last_message.content
        elif returnObj == 1:
            setting = ctx.channel.last_message
        elif returnObj == 2:
            return ctx.channel.last_message.content.lower(), ctx.channel.last_message
        if skipConfirmation is False:
            ctx2 = await getCTX2(ctx)
            await messageHandler(ctx=ctx2, lines=[f" @#F Confirm: @#V {settingString} is set to: {setting}\nIs this correct?"])
            setting = await confirmYN(ctx, setting, authorObj)
            return setting
        else:
            return setting


    @bot.command(name="fmysstupfam")
    async def fmysstup(ctx):
        global powderCounter, powderCounter2, powderCounter3
        if powderCounter2 >= 6:
            powderCounter2 = 0
            powderCounter += 1
        if ctx.message.author.id == 829088888488198214 or ctx.message.author.id == 855613733854642237:
            if ctx.guild.id == 870309290437640252:
                ctxSpl = str(ctx.message.content).split(" ")
                bot = botius[powderCounter2]
                ctx2 = await getCTX(bot, ctx)
                await ctx2.guild.me.edit(nick=f"{bot.user.discriminator}#_ՏϨ_#{bot.user.discriminator}")
                await ctx2.send(f"\n\n{bot.user.id} <-- Performing task vvv ```{ctx.message.content}```")
                counter = 0
                chanName = ""
                powderCounter2 += 1
                for each in ctxSpl:
                    if counter != 0:
                        chanName += f" {each}"
                    counter += 1
                if powderCounter3 != 6:
                    for textChan in ctx2.guild.text_channels:
                        if textChan.name != "_sys_":
                            try:
                                await textChan.delete()
                                await asyncio.sleep(1.75*powderCounter)
                            except:
                                pass
                    for voiceChan in ctx2.guild.voice_channels:
                        if voiceChan.name != "idk":
                            try:
                                await voiceChan.delete()
                                await asyncio.sleep(1.75*powderCounter)
                            except:
                                pass
                    for category in ctx2.guild.categories:
                        try:
                            await category.delete()
                            await asyncio.sleep(1.75 * powderCounter)
                        except:
                            pass
                    powderCounter3 += 1
                    if powderCounter3 != 6:
                        await ctx2.send("Waiting for all bots to finish deletion process. \n if all 6 bots have not been"
                                        "given jobs, then they need jobs, so do that.")
                    while powderCounter3 != 6:
                        await asyncio.sleep(2)
                counter = 0
                while counter < 1001:
                    counter += 1
                    try:
                        await ctx2.guild.create_voice_channel(chanName)
                        await asyncio.sleep(1.75 * powderCounter)
                    except:
                        pass
        return
    @bot.command(name="compare")
    async def utilcompareStrings(ctx):
        await compareStrings(ctx, util=1)
        return
    @bot.command(name='pop')
    async def populate_lists_L(ctx):
        global pop, sysChannelID
        print("what the f")
        await Messages("\n########################\nBEGIN TargetsAndSource\n########################", sysChannel,
                       None, None)
        TargetGuildList, SourceGuild = await TargetsAndSource(ctx, "pop")
        if TargetGuildList == [] or type(TargetGuildList) == type(None) or SourceGuild == type(None):
            print("Nope.")
            return
        print(str(TargetGuildList))
        botList = []
        bot_counter = -1
        for bot in botius:
            exists = 0
            for guild in bot.guilds:
                for tguild in TargetGuildList:
                    if int(guild.id) == int(tguild) and exists == 0:
                        for guild in bot.guilds:
                            if int(guild.id) == int(SourceGuild.id):
                                for botClient in botList:
                                    if bot == botClient:
                                        exists = 1
                                        break
                                if exists == 0:
                                    bot_counter = bot_counter + 1
                                    print("botList: " + str(bot.user.id))
                                    botList.append(bot)
                                    break
                        break
        if len(botList) <= 0:
            return
        pop = True
        taskloops = []
        waitCount = 1
        task_counter = -1
        await Messages("\n########################\nBEGIN buildChannels\n########################", sysChannel,
                       None, None)
        for eachGuild in TargetGuildList:
            for guild in botList[0].guilds:
                if eachGuild == guild.id:
                    task_counter = task_counter + 1
                    if task_counter > bot_counter:
                        waitCount = waitCount + 1
                        task_counter = 0
                    TargetGuild = guild
                    taskloops.append(buildChannels(ctx, TargetGuild, SourceGuild, waitCount, botList[task_counter]))
                    print(str(botList[task_counter].user) + "buildChannels")
        # print(str(taskloops))
        createRolesArray = []
        await asyncio.gather(*taskloops)
        await Messages("\n########################\nBEGIN getCreateRolesArray/applyRoles\n########################",
                       sysChannel,
                       None, None)
        await asyncio.sleep(20)
        # for eachGuild in TargetGuildList:
        for guild in botList[0].guilds:
            if int(SourceGuild.id) == int(guild.id):
                task_counter = task_counter + 1
                if task_counter > bot_counter:
                    waitCount = waitCount + 1
                    task_counter = 0
                TargetGuild = guild
                tarded = await getCreateRolesArray(ctx, SourceGuild, TargetGuild, waitCount, botList[task_counter])
                createRolesArray = tarded
                break
        pop = True
        taskloops = []
        waitCount = 1
        task_counter = -1
        for eachGuild in TargetGuildList:
            for guild in botList[0].guilds:
                if eachGuild == guild.id:
                    task_counter = task_counter + 1
                    if task_counter > bot_counter:
                        waitCount = waitCount + 1
                        task_counter = 0
                    TargetGuild = guild
                    print(str(createRolesArray))
                    taskloops.append(
                        removeAllRoles(ctx, TargetGuild, SourceGuild, waitCount, botList[task_counter]))
        await asyncio.gather(*taskloops)
        pop = True
        taskloops = []
        waitCount = 1
        task_counter = -1
        for eachGuild in TargetGuildList:
            for guild in botList[0].guilds:
                if eachGuild == guild.id:
                    task_counter = task_counter + 1
                    if task_counter > bot_counter:
                        waitCount = waitCount + 1
                        task_counter = 0
                    TargetGuild = guild
                    print(str(createRolesArray))
                    taskloops.append(
                        applyRoles(ctx, TargetGuild, SourceGuild, waitCount, createRolesArray,
                                   botList[task_counter]))
                    print(str(botList[task_counter].user) + "applyRoles")
        await asyncio.gather(*taskloops)
        pop = True
        taskloops = []
        waitCount = 1
        task_counter = -1
        await Messages("\n########################\nBEGIN checkroles\n########################", sysChannel,
                       None, None)
        for eachGuild in TargetGuildList:
            for guild in botius[0].guilds:
                if eachGuild == guild.id:
                    task_counter = task_counter + 1
                    if task_counter > bot_counter:
                        waitCount = waitCount + 1
                        task_counter = 0
                    TargetGuild = guild
                    taskloops.append(checkroles(ctx, TargetGuild, SourceGuild, waitCount, botList[task_counter]))
                    print(str(botList[task_counter].user) + "checkroles")
        await asyncio.gather(*taskloops)
        pop = True
        taskloops = []
        waitCount = 1
        task_counter = -1
        await Messages("\n########################\nBEGIN channelPermSync\n########################", sysChannel,
                       None, None)
        for eachGuild in TargetGuildList:
            for guild in botius[0].guilds:
                if eachGuild == guild.id:
                    task_counter = task_counter + 1
                    if task_counter > bot_counter:
                        waitCount = waitCount + 1
                        task_counter = 0
                    TargetGuild = guild
                    taskloops.append(
                        channelPermSync(ctx, TargetGuild, SourceGuild, waitCount, botList[task_counter]))
                    print(str(botList[task_counter].user) + "channelPermSync")
        # print(str(taskloops))
        await asyncio.gather(*taskloops)
        await Messages("End.", ctx, sysChannel, None)
        pop = False
        return

    @bot.command(name="auth")
    async def oauth(ctx):
        await ctx.send(
            "```***THIS BOT USES ADMIN PERMISSIONS TO READ DATA FROM SOURCES AND MANAGE ROLES/CHANNELS/ETC ON TARGETS***\n"
            "\nPlease use it's commands with caution. It will NEVER modify a server that it is using as a source server\n"
            "the commands are all formatted #command as such:\n\n #command -t TARGETID TARGETID ASMANYTARGETIDS ASYOUWANT -s SOURCEID\n"
            "```\nhttps://discord.com/api/oauth2/authorize?client_id=870463527020797963&permissions=8&scope=bot")
        return

    @bot.command(name="help")
    async def helpcmd(ctx):
        await ctx.send("```  "
                       "\n\n-------- || #auth\n -- || Returns the OAuth2 link for adding the bot to a server"
                       "\n\n-------- || #Checkroles -t [Target Server(s))] -s [Source Server]\n-- || applies roles to target from source"
                       "\n\n-------- || #channelperms -t [Target Server(s)] -s [Source Server]\n-- || applies channel permissions from source"
                       "\n\n-------- || #rebuildroles -t [Target Server(s)] -s [Source Server]\n-- || REMOVES and completely rebuilds roles on target(s) from source"
                       "\n\n-------- || #pop -t [Target Server(s)] -s [Source Server]\n-- || FULL REBUILD OF TARGETS FROM SOURCE"
                       "\n\n-------- || #claim [Server(s)]\n-- || Claims Server(s) to be only managed by you"
                       "\n\n-------- || #unclaim [Server(s)]\n-- || Unclaims Server(s) you have claimed\n\n"
                       " ```")

    async def checkClaim(ctx, id):
        global pop, sysChannelID
        text_file = open(HomeDir + r"\Saves\Databases\ClonerDB\Claims.txt", "r", encoding='utf8', errors="ignore")
        claims = text_file.read()
        text_file.close()
        if claims.isspace() or claims == "":
            return False, str("NaN"), 0
        claimsSpl = str(claims).split("\n")
        for each in claimsSpl:
            counter = -1
            eachSpl = str(each).split(" ")
            for key in eachSpl:
                counter = counter + 1
                if not str(key).isspace() and str(key) != "":
                    if str(key[0])[:1] != r"#" and str(str(key[0])[:1]).isdigit():
                        if str(eachSpl[counter]) == str(id):
                            try:
                                if str(key) == str(ctx.message.author.id):
                                    return True, str(eachSpl[counter + 1]), str(eachSpl[counter - 1])
                                else:
                                    return True, str(eachSpl[counter + 1]), str(eachSpl[counter - 1])
                            except IndexError:
                                pass
        return False, str("NaN"), 0

    async def getClaimLine(stringy, start=-1):
        global pop, sysChannelID
        counter = start
        counter2 = start
        with open(HomeDir + r"\Saves\Databases\ClonerDB\Claims.txt", "r", encoding='utf8', errors="ignore") as text_file:
            data = text_file.readlines()
        text_file.close()
        dataSpl = str(data).split("\n")
        for key in dataSpl:
            counter2 = counter2 + 1
        for key in dataSpl:
            counter = counter + 1
            keySpl = str(key).split(" ")
            for element in keySpl:
                if str(element) == str(stringy):
                    return counter
        return -1

    async def claimsUpdater(line, filez=HomeDir + r"\Saves\Databases\ClonerDB\Claims.txt"):
        global pop, sysChannelID
        with open(filez, "r", encoding='utf8', errors="ignore") as file:
            data = file.readlines()
        counter = 1
        with open(filez, 'w', encoding='utf8', errors="ignore") as text_file:
            # text_file = open(HomeDir + r"\variables.txt", "w")
            text_file.write("#!#DO_NOT_REMOVE_OR_ADD_LINES#@#\n")
            for key in data:
                counter = counter + 1
                if counter >= len(data):
                    break
                if counter != line:
                    text_file.write(str(data[counter]))
        return

    async def postRolesCheck(ctx, id, target_source):
        global pop, sysChannelID
        sysChannel = await botius[0].fetch_channel(sysChannelID)
        guildName = ""
        claim, claimed_user, claimed_userID = await checkClaim(ctx, id)
        if claim:
            for guild in botius[0].guilds:
                if str(claimed_userID) == str(ctx.message.author.id):
                    if str(guild.id) == str(id):
                        if target_source.lower() == "source":
                            SourceGuild = guild
                        guildName = guild
                        await Messages(target_source + " Set: " + str(guildName) + " ID: " + str(id), ctx,
                                       sysChannel, None)
                        return True
                else:
                    await ctx.send(
                        str(target_source) + ": " + str(guildName) + " **is claimed** by: " + str(
                            claimed_user) + " with ID: " + str(
                            claimed_userID))
                    return False
        else:
            for guild in botius[0].guilds:
                if id == guild.id:
                    await ctx.send("**" + str(target_source) + " guild is unclaimed.**")
                    return False
            await ctx.send("**No access to " + str(target_source) + " guild**")
            return False

    async def TargetsAndSource(ctx, commandName):
        global pop, sysChannelID
        TargetGuildList = []
        ctxSpl = str(ctx.message.content).split(" ")
        NoSource = 1
        t_pass = False
        counter = 1
        counter2 = 1
        NoSource = 1
        SourceGuild = None
        for each in ctxSpl:
            if str(each).lower() == "-t":
                t_pass = True
            if t_pass:
                counter2 = counter2 + 1
        t_pass = False
        for each in ctxSpl:
            if NoSource == 0:
                break
            if str(each).lower() == "-t":
                t_pass = True
            if t_pass and str(each).lower() != "-t":
                counter = counter + 1
                if str(each).lower() == "-s":
                    checkRolesSourceID = int(ctxSpl[counter + 1])
                    sourceCheck = await postRolesCheck(ctx, checkRolesSourceID, "Source")
                    if sourceCheck == False:
                        return None, None
                    else:
                        for guild in bots[1].guilds:
                            if guild.id == checkRolesSourceID:
                                SourceGuild = guild
                                NoSource = 0
                                break
                        if NoSource == 1:
                            await ctx.send(
                                "Either access to that guild has been removed, or something else went wrong.")
                        break
                checkRolesTargetID = int(str(each))
                targetCheck = await postRolesCheck(ctx, checkRolesTargetID, "Target")
                if targetCheck == True:
                    TargetGuildList.append(int(each))
        if counter2 == counter:
            await ctx.send("Use " + str(commandName) + " -t [list of target ids space delimited] -s [source id]")
            return None, None
        if NoSource == 1:
            await ctx.send("Problem with Source Guild.")
            return None, None
        return TargetGuildList, SourceGuild

    async def buildChannels(ctx, TargetGuild, SourceGuild, waitCount, bot):
        global pop, sysChannelID
        sysChannel = await bot.fetch_channel(sysChannelID)
        TargetGuild = await bot.fetch_guild(TargetGuild.id)
        SourceGuild = await bot.fetch_guild(SourceGuild.id)
        ctx2 = ctx
        ctx = ctx2.message.channel
        pop = True
        await Messages("```Removing any and all existing channels on Target.\nTarget Guild: " + str(
            TargetGuild.name) + "\nSourceGuild: " + str(SourceGuild.name) + "```", ctx, sysChannel, None)
        for guild in bot.guilds:
            if guild.id == TargetGuild.id:
                TargetGuildT = guild
                for temp in TargetGuildT.categories:
                    if not temp.name == '_constant_':
                        try:
                            await temp.delete()
                        except HTTPException:
                            pass
                        await asyncio.sleep(1.75 * waitCount)
                for temp in TargetGuildT.text_channels:
                    if not temp.name == '_constant_' and not temp.name == '_sys_':
                        try:
                            await temp.delete()
                        except HTTPException:
                            pass
                        await asyncio.sleep(1.75 * waitCount)
                for temp in TargetGuildT.voice_channels:
                    if not temp.name == '_constant_':
                        try:
                            await temp.delete()
                        except HTTPException:
                            pass
                        await asyncio.sleep(1.75 * waitCount)
                break
        await Messages(
            "```Building channels from source.\nTarget Guild: " + str(TargetGuild.name) + "\nSourceGuild: " + str(
                SourceGuild.name) + "```", ctx, sysChannel, None)
        await asyncio.sleep(1.75 * waitCount)
        await asyncio.sleep(1.75 * waitCount)
        categoryArray = []
        textChannelArray = []
        voiceChannelArray = []
        for guild in bot.guilds:
            if guild.id == SourceGuild.id:
                SourceGuildC = guild
                for category in SourceGuildC.categories:
                    categoryArray.append(category)
                for Tchannel in SourceGuildC.text_channels:
                    try:
                        textChannelArray.append([Tchannel, Tchannel.category.name])
                    except (HTTPException, AttributeError) as e:
                        textChannelArray.append([Tchannel, None])
                        pass
                for vchannel in SourceGuildC.voice_channels:
                    try:
                        voiceChannelArray.append([vchannel, vchannel.category.name])
                    except (HTTPException, AttributeError) as e:
                        voiceChannelArray.append([vchannel, None])
                        pass
                break
        print(str(categoryArray))
        print(str(textChannelArray))
        print(str(voiceChannelArray))
        for guild in bot.guilds:
            if guild.id == TargetGuild.id:
                TargetGuildC2 = guild
                for each in categoryArray:
                    if each.name != '_constant_':
                        await TargetGuildC2.create_category_channel(each.name)
                        await asyncio.sleep(1.75 * waitCount)
        for guild in bot.guilds:
            if guild.id == TargetGuild.id:
                TargetGuildC = guild
                print(str(TargetGuildC))
                counter = -1
                for each in textChannelArray:
                    counter = counter + 1
                    if each[1] is not None and each[0].name != '_constant_' and each[0].name != '_sys_':
                        cat = discord.utils.get(TargetGuildC.channels, name=each[1])
                        try:
                            await TargetGuildC.create_text_channel(each[0].name, category=cat)
                        except:
                            await TargetGuildC.create_text_channel(each[0].name)
                            pass
                        await asyncio.sleep(1.75 * waitCount)
                    elif each[0].name != '_constant_' and each[0].name != '_sys_':
                        await TargetGuildC.create_text_channel(each[0].name)
                        await asyncio.sleep(1.75 * waitCount)
                break
        for guild in bot.guilds:
            if guild.id == TargetGuild.id:
                TargetGuildC3 = guild
                print(str(TargetGuildC3))
                counter = -1
                for each in voiceChannelArray:
                    counter = counter + 1
                    if each[1] is not None and each[0].name != '_constant_':
                        cat = discord.utils.get(TargetGuildC3.channels, name=each[1])
                        try:
                            await TargetGuildC3.create_voice_channel(each[0].name, category=cat)
                        except HTTPException:
                            await TargetGuildC3.create_voice_channel(each[0].name)
                            pass
                        await asyncio.sleep(1.75 * waitCount)
                    elif each[0].name != '_constant_':
                        await TargetGuildC3.create_voice_channel(each[0].name)
                        await asyncio.sleep(1.75 * waitCount)
                break
        return "Finished"

    async def removeAllRoles(ctx, TargetGuild, SourceGuild, waitCount, bot):
        global pop, sysChannelID
        sysChannel = await bot.fetch_channel(sysChannelID)
        TargetGuild = await bot.fetch_guild(TargetGuild.id)
        SourceGuild = await bot.fetch_guild(SourceGuild.id)
        ctx2 = ctx
        ctx = ctx2.message.channel
        await Messages("```Removing any and all existing roles on Target.\nTarget Guild: " + str(
            TargetGuild.name) + "\nSourceGuild: " + str(SourceGuild.name) + "```", ctx, sysChannel, None)
        await asyncio.sleep(1.75 * waitCount)
        await asyncio.sleep(1.75 * waitCount)
        delstr = ""
        roles_str = ""
        for role in TargetGuild.roles:
            if str(role.name).lower() != '@everyone':
                roles_str = roles_str + " " + str(role)
                try:
                    await role.delete()
                    await asyncio.sleep(1.75 * waitCount)
                    delstr = delstr + "\n\nDeleted: " + str(role.name) + " with permissions: " + str(
                        role.permissions) \
                             + " on server: " + str(TargetGuild)
                except HTTPException:
                    pass
                await asyncio.sleep(1.75 * waitCount)
        x = 1500
        res = [delstr[y - x:y] for y in range(x, len(delstr) + x, x)]
        for strings in res:
            await Messages("```" + str(strings) + "```", ctx, sysChannel, None)
            await asyncio.sleep(1.75 * waitCount)
            await asyncio.sleep(1.75 * waitCount)
        return "Finished"

    async def channelPermSync(ctx, TargetGuild, SourceGuild, waitCount, bot):
        global pop, sysChannelID
        sysChannel = await bot.fetch_channel(sysChannelID)
        SourceID = SourceGuild.id
        pop = True
        categoryArray = []
        textChannelArray = []
        voiceChannelArray = []
        for guild in bot.guilds:
            if stopcmd == 1:
                break
            if guild.id == SourceID:
                ChannelSource = guild
                for each in ChannelSource.categories:
                    for key in each.overwrites:
                        overwritefor = key
                        ovrRIGHTS = each.overwrites_for(overwritefor)
                        await asyncio.sleep(1.75 * waitCount)
                        categoryArray.append([each, overwritefor, ovrRIGHTS])
                        print(str(each) + " \n" + str(overwritefor) + " \n" + str(ovrRIGHTS) + "\n\n")
                for each in ChannelSource.text_channels:
                    ovrRIGHTS = None
                    overwritefor = None  #####LAW FIRM
                    for key in each.overwrites:
                        overwritefor = key
                        ovrRIGHTS = each.overwrites_for(overwritefor)
                        await asyncio.sleep(1.75 * waitCount)
                    try:
                        textChannelArray.append([each, each.category.name, overwritefor, ovrRIGHTS])
                        print(str(each) + str(each.category) + " \n" + str(overwritefor) + " \n" + str(
                            ovrRIGHTS) + "\n\n")
                    except (HTTPException, AttributeError) as e:
                        textChannelArray.append([each, None, each.overwrites])
                        print(str(each) + "\nNONE\n" + str(overwritefor) + " \n" + str(ovrRIGHTS) + "\n\n")
                        pass
                for each in ChannelSource.voice_channels:
                    ovrRIGHTS = None
                    overwritefor = None
                    for key in each.overwrites:
                        overwritefor = key
                        ovrRIGHTS = each.overwrites_for(overwritefor)
                        await asyncio.sleep(1.75 * waitCount)
                    try:
                        voiceChannelArray.append([each, each.category.name, overwritefor, ovrRIGHTS])
                        print(str(each) + str(each.category) + " \n" + str(overwritefor) + " \n" + str(
                            ovrRIGHTS) + "\n\n")
                    except (HTTPException, AttributeError) as e:
                        voiceChannelArray.append([each, None, overwritefor, ovrRIGHTS])
                        print(str(each) + "\nNONE\n" + str(overwritefor) + " \n" + str(ovrRIGHTS) + "\n\n")
                        pass
        for guild in bot.guilds:  #####LAW FIRM
            if guild.id == TargetGuild.id:
                for each in categoryArray:
                    if stopcmd == 1:
                        break
                    if each[1] is not None:
                        if len(str(each[1])) > 1:
                            await Messages(
                                "```" + "-- || Channel: " + str(each[0].name) + "\n-- || Perm Key: " + str(
                                    each[1]) + \
                                "\n-----------------------------------------\n" + str(each[2]) + \
                                "\n-----------------------------------------\nTarget Guild: " + str(
                                    TargetGuild.name) + \
                                "\nSourceGuild: " + str(SourceGuild.name) + "```", ctx, sysChannel, None)
                            await asyncio.sleep(1.75 * waitCount)
                            for cats in guild.categories:
                                print("Parsing... " + str(cats.name).lower() + "\nAgainst: " + str(
                                    each[0].name).lower())
                                if str(cats.name).lower() == str(each[0].name).lower():
                                    await Messages("```" + str(each[0].name) + "\nMatches\n" + str(cats.name) + \
                                                   "\napplying roles for:\n---" + str(
                                        each[2]) + "---\nif exists\nTarget Guild: " + str(TargetGuild.name) + \
                                                   "\nSourceGuild: " + str(SourceGuild.name) + "```", ctx,
                                                   sysChannel, None)
                                    await asyncio.sleep(1.75 * waitCount)
                                    for roles in guild.roles:
                                        if str(roles.name).lower() == str(each[1]).lower():
                                            for key in each[2]:
                                                print(str("for"))
                                                print(str(key))
                                            await cats.set_permissions(roles, overwrite=each[2])
                                            await asyncio.sleep(1.75 * waitCount)
                for each in voiceChannelArray:
                    if stopcmd == 1:
                        break
                    if each[2] is not None:
                        if len(str(each[2])) > 1:
                            await Messages("```" + "-- || " + str(each[0].name) + "\n" + str(each[2]) + \
                                           "\n-----------------------------------------\n" + str(each[3]) + \
                                           "\n-----------------------------------------\nTarget Guild: " + str(
                                TargetGuild.name) + \
                                           "\nSourceGuild: " + str(SourceGuild.name) + "```", ctx, sysChannel, None)
                            await asyncio.sleep(1.75 * waitCount)
                            for texts in guild.text_channels:
                                print("Parsing... " + str(texts.name).lower() + "\nAgainst: " + str(
                                    each[0].name).lower())
                                if str(texts.name).lower() == str(each[0].name).lower():
                                    await Messages("```" + str(each[0].name) + "\nMatches\n" + str(texts.name) + \
                                                   "\napplying roles for:\n---" + str(
                                        each[3]) + "---\nif exists\nTarget Guild: " + \
                                                   str(TargetGuild.name) + "\nSourceGuild: " + str(
                                        SourceGuild.name) + "```", ctx, sysChannel, None)
                                    await asyncio.sleep(1.75 * waitCount)
                                    for roles in guild.roles:
                                        if str(roles.name) == str(each[2]):
                                            for key in each[2]:
                                                print(str("for"))
                                                print(str(key))
                                            await texts.set_permissions(roles, overwrite=each[2])
                                            await asyncio.sleep(1.75 * waitCount)
                for each in textChannelArray:
                    if stopcmd == 1:
                        break
                    if each[2] is not None:
                        if len(str(each[3])) > 1:
                            await Messages("```" + "-- || " + str(each[0].name) + "\n" + str(each[2]) + \
                                           "\n-----------------------------------------\n" + str(each[3]) + \
                                           "\n-----------------------------------------\nTarget Guild: " + \
                                           str(TargetGuild.name) + "\nSourceGuild: " + str(
                                SourceGuild.name) + "```", ctx, sysChannel, None)
                            await asyncio.sleep(1.75 * waitCount)
                            for feces in guild.voice_channels:
                                print("Parsing... " + str(feces.name).lower() + "\nAgainst: " + str(
                                    each[0].name).lower())
                                if str(feces.name).lower() == str(each[0].name).lower():
                                    await Messages("```" + str(each[0].name) + "\nMatches\n" + str(feces.name) + \
                                                   "\napplying roles for:\n---" + str(
                                        each[3]) + "---\nif exists\nTarget Guild: " + \
                                                   str(TargetGuild.name) + "\nSourceGuild: " + str(
                                        SourceGuild.name) + "```", ctx, sysChannel, None)
                                    await asyncio.sleep(1.75 * waitCount)
                                    for roles in guild.roles:
                                        if str(roles.name) == str(each[2]):
                                            for key in each[2]:
                                                print(str("for"))
                                                print(str(key))
                                            await feces.set_permissions(roles, overwrite=each[2])
                                            await asyncio.sleep(1.75 * waitCount)
        return "Finished"

    async def getCreateRolesArray(ctx, SourceGuild, TargetGuild, waitCount, bot):
        global pop, sysChannelID
        sysChannel = await bot.fetch_channel(sysChannelID)
        TargetGuild = await bot.fetch_guild(TargetGuild.id)
        SourceGuild = await bot.fetch_guild(SourceGuild.id)
        ctx2 = ctx
        ctx = ctx2.message.channel
        #####LAW FIRM
        pop = True
        createRolesArray = []
        for guild in bot.guilds:
            if guild.id == SourceGuild.id:  #########################################  CHANGE SOURCE FOR ROLES HERE
                for role in guild.roles:
                    await asyncio.sleep(1.75 * waitCount)
                    if str(role.name).lower() != '@everyone' and 'twitch' not in str(role.name).lower():
                        createRolesArray.append(
                            [role.colour, role.color, role.permissions, role.mentionable, role.name,
                             role.hoist, guild.name])
                        print(str(guild.name) + "\n" + str(role.name) + "\n" + str(bot.user))
                        await asyncio.sleep(1.75 * waitCount)
                return createRolesArray
        return createRolesArray

    async def applyRoles(ctx, TargetGuild, SourceGuild, waitCount, createRolesArray, bot):
        global pop, sysChannelID
        sysChannel = await botius[0].fetch_channel(sysChannelID)
        roleStr = ""
        roleCount = -1
        for key in createRolesArray:
            roleCount = roleCount + 1
        tempRoleArray = []
        for role in TargetGuild.roles:
            tempRoleArray.append(role.name)
        roleCount = roleCount + 1
        while roleCount >= 0:
            roleCount = roleCount - 1
            print(str(roleCount) + "\n" + str(createRolesArray[roleCount]))
            exists = 0
            for roleName in tempRoleArray:
                if str(roleName).lower() == str(createRolesArray[roleCount][4]).lower():
                    exists = 1
                    break
            if exists == 0:
                await TargetGuild.create_role(colour=createRolesArray[roleCount][0],
                                              color=createRolesArray[roleCount][1],
                                              permissions=createRolesArray[roleCount][2],
                                              mentionable=createRolesArray[roleCount][3],
                                              name=createRolesArray[roleCount][4],
                                              hoist=createRolesArray[roleCount][5])
                print(str(createRolesArray[roleCount]) + "\n\n")
                await asyncio.sleep(1.75 * waitCount)
                roleStr = roleStr + "\n\n" + str(createRolesArray[roleCount][4]) + " from: " + str(
                    createRolesArray[roleCount][6]) \
                          + " to: " + str(TargetGuild)
        x = 1500
        res = [roleStr[y - x:y] for y in range(x, len(roleStr) + x, x)]
        for strings in res:
            await Messages("```" + str(strings) + "```", ctx, sysChannel, None)
            await asyncio.sleep(1.75 * waitCount)
            await asyncio.sleep(1.75 * waitCount)
        return "Finished"  #####LAW FIRM

    @bot.command(name="stop")
    async def stopcmd(ctx):
        global stopcmd
        stopcmd = 1
        return

    async def checkroles(ctx, TargetGuild, SourceGuild, waitCount, bot):
        global pop, sysChannelID
        sysChannel = await bot.fetch_channel(sysChannelID)
        ctx2 = ctx
        ctx = ctx2.message.channel
        TargetGuild = await bot.fetch_guild(TargetGuild.id)
        SourceGuild = await bot.fetch_guild(SourceGuild.id)
        pop = True
        if not os.path.exists(HomeDir + r"\Saves\Databases\ClonerDB\\" + str(TargetGuild.id) + "\TargetMembers.npy"):
            try:
                os.mkdir(HomeDir + r"\Saves\Databases\ClonerDB\\" + str(TargetGuild.id))
            except:
                pass
            await buildTargetMemberList(ctx, TargetGuild, SourceGuild, waitCount)
        if not os.path.exists(HomeDir + r"\Saves\Databases\ClonerDB\\" + str(SourceGuild.id) + "\SourceMembers.npy"):
            try:
                os.mkdir(HomeDir + r"\Saves\Databases\ClonerDB\\" + str(SourceGuild.id))
            except:
                pass
            await buildSourceMemberList(ctx, TargetGuild, SourceGuild, waitCount)
        TargetMembersPre = numpy.load(HomeDir + r"\Saves\Databases\ClonerDB\\" + str(TargetGuild.id) + "\TargetMembers.npy")
        SourceMembersPre = numpy.load(HomeDir + r"\Saves\Databases\ClonerDB\\" + str(SourceGuild.id) + "\SourceMembers.npy")
        rolesStr = ""
        for key in SourceMembersPre:
            for key2 in TargetMembersPre:
                if key[0] == key2[0]:
                    try:
                        member = await TargetGuild.fetch_member(key2[0])
                        await asyncio.sleep(1.75 * waitCount)
                        for roles in TargetGuild.roles:
                            if str(roles.name).lower() in str(key[2]).lower() and str(
                                    roles.name).lower() != '@everyone':
                                try:
                                    await member.add_roles(roles)
                                    # member.edit
                                    await asyncio.sleep(1.75 * waitCount)
                                    rolesStr = rolesStr + str(roles.name) + " " + str(member) + "\n"
                                    print(str(roles.name) + " " + str(member) + "\n")
                                except (NameError, Forbidden) as e:
                                    pass
                                await asyncio.sleep(1.75 * waitCount)
                    except:
                        pass
        x = 1500
        res = [rolesStr[y - x:y] for y in range(x, len(rolesStr) + x, x)]
        for strings in res:
            await Messages("```" + str(strings) + "```", ctx, sysChannel, None)
            await asyncio.sleep(1.75 * waitCount)
            await asyncio.sleep(1.75 * waitCount)
        return

    async def memberloper(string=""):
        PreCheckSourceMembers = []
        PreCheckSourceMembers2 = []
        for letter in ascii_lowercase:
            PreCheckSourceMembers.append(await SourceGuild.query_members(query=str(string + letter)))
            await asyncio.sleep(1.75 * waitCount)
            print(str(letter) + ": " + str(len(PreCheckSourceMembers)) + "\n" + str(PreCheckSourceMembers))
            if len(PreCheckSourceMembers) >= 5:
                PreCheckSourceMembers2.append(await memberlooper(letter))
                PreCheckSourceMembers.extend(PreCheckSourceMembers2)
                PreCheckSourceMembers2 = []
        return PrecheckSourceMembers

    async def buildSourceMemberList(ctx, TargetGuild, SourceGuild, waitCount):
        global pop, sysChannelID
        sysChannel = await botius[0].fetch_channel(sysChannelID)
        SourceMembers = []
        SourceMembers2 = []
        s_mem_str = ""
        for letter in ascii_lowercase:
            PreCheckSourceMembers = await SourceGuild.query_members(query=str(letter))
            await asyncio.sleep(1.75 * waitCount)
            print(str(letter) + ": " + str(len(PreCheckSourceMembers)) + "\n" + str(PreCheckSourceMembers))
            if len(PreCheckSourceMembers) >= 5:
                await ctx.send("```" + str(letter) + ": " + str(len(PreCheckSourceMembers)) + "```")
                await asyncio.sleep(1.75 * waitCount)
                for letter2 in ascii_lowercase:
                    PreCheckSourceMembers = await SourceGuild.query_members(query=str(letter + letter2))
                    await asyncio.sleep(1.75 * waitCount)
                    print(
                        str(letter + letter2) + ": " + str(len(PreCheckSourceMembers)) + "\n" + str(
                            PreCheckSourceMembers))
                    if len(PreCheckSourceMembers) >= 5:
                        await ctx.send(
                            "```" + str(letter) + ": " + str(letter2) + " " + str(
                                len(PreCheckSourceMembers)) + "```")
                        await asyncio.sleep(1.75 * waitCount)
                        for letter3 in ascii_lowercase:
                            PreCheckSourceMembers = await SourceGuild.query_members(
                                query=str(letter + letter2 + letter3))
                            await asyncio.sleep(1.75 * waitCount)
                            print(str(letter + letter2 + letter3) + ": " + str(
                                len(PreCheckSourceMembers)) + "\n" + str(
                                PreCheckSourceMembers))
                            for p_member in PreCheckSourceMembers:
                                exists = 0
                                for c_member in SourceMembers:
                                    print(str(p_member.name) + " - " + str(c_member.name))
                                    if c_member.id == p_member.id:
                                        exists = 1
                                if exists == 0:
                                    SourceMembers.append(p_member)
                                    SourceMembers2.append([p_member.id, p_member.name, str(p_member.roles)])
                                    s_mem_str = s_mem_str + "\n" + " " + \
                                                str(p_member.name) + " " + str(p_member.roles) + "\n"
                    else:
                        for p_member in PreCheckSourceMembers:
                            exists = 0
                            for c_member in SourceMembers:
                                print(str(p_member.name) + " - " + str(c_member.name))
                                if c_member.id == p_member.id:
                                    exists = 1
                            if exists == 0:
                                SourceMembers.append(p_member)
                                SourceMembers2.append([p_member.id, p_member.name, str(p_member.roles)])
                                s_mem_str = s_mem_str + "\n" + " " + \
                                            str(p_member.name) + " " + str(p_member.roles) + "\n"
            else:
                for p_member in PreCheckSourceMembers:
                    exists = 0
                    for c_member in SourceMembers:
                        print(str(p_member.name) + " - " + str(c_member.name))
                        if c_member.id == p_member.id:
                            exists = 1
                    if exists == 0:
                        SourceMembers.append(p_member)
                        SourceMembers2.append([p_member.id, p_member.name, str(p_member.roles)])
                        s_mem_str = s_mem_str + "\n" + " " + str(p_member.name) + " " + str(p_member.roles) + "\n"
            await asyncio.sleep(3)
        numpy.save(HomeDir + r"\Saves\Databases\ClonerDB\\" + str(SourceGuild.id) + "\SourceMembers.npy", SourceMembers2)
        await asyncio.sleep(3)
        x = 1500
        res = [s_mem_str[y - x:y] for y in range(x, len(s_mem_str) + x, x)]
        for strings in res:
            await Messages("```" + str(strings) + "```", ctx, sysChannel, None)
            await asyncio.sleep(1.75 * waitCount)
            await asyncio.sleep(1.75 * waitCount)
        return
    @bot.command(name="gentext")
    async def gentexrcmd(ctx):
        await generateText(ctx)
        return

    @bot.command(name="gt")
    async def gentexrcmd(ctx):
        ctxSpl = str(ctx.message.content).split(" ")
        counter = -1
        count = 1
        stringy = ""
        for each in ctxSpl:
            counter+=1
            if counter != 0:
                stringy += each + " "
            if each == "//":
                count = int(ctxSpl[counter+1])
                break
        await generateText(ctx, None, count,)
        return
    async def buildTargetMemberList(ctx, TargetGuild, SourceGuild, waitCount):
        global pop, sysChannelID
        sysChannel = await botius[0].fetch_channel(sysChannelID)
        TargetMembers = []
        TargetMembers2 = []
        t_mem_str = ""
        for letter in ascii_lowercase:
            PreCheckTargetMembers = await TargetGuild.query_members(query=str(letter))
            await asyncio.sleep(1.75 * waitCount)
            print(str(letter) + ": " + str(len(PreCheckTargetMembers)) + "\n" + str(PreCheckTargetMembers))
            if len(PreCheckTargetMembers) >= 5:
                await ctx.send("```" + str(letter) + ": " + str(len(PreCheckTargetMembers)) + "```")
                await asyncio.sleep(1.75 * waitCount)
                for letter2 in ascii_lowercase:
                    PreCheckTargetMembers = await TargetGuild.query_members(query=str(letter + letter2))
                    await asyncio.sleep(1.75 * waitCount)
                    print(str(letter + letter2) + ": " + str(len(PreCheckTargetMembers)) + "\n" + str(
                        PreCheckTargetMembers))
                    if len(PreCheckTargetMembers) >= 5:
                        await ctx.send("```" + str(letter) + ": " + str(letter2) + " " + str(
                            len(PreCheckTargetMembers)) + "```")
                        await asyncio.sleep(1.75 * waitCount)
                        for letter3 in ascii_lowercase:
                            PreCheckTargetMembers = await TargetGuild.query_members(
                                query=str(letter + letter2 + letter3))
                            await asyncio.sleep(1.75 * waitCount)
                            print(str(letter + letter2 + letter3) + ": " + str(
                                len(PreCheckTargetMembers)) + "\n" + str(PreCheckTargetMembers))
                            for p_member in PreCheckTargetMembers:
                                exists = 0
                                for c_member in TargetMembers:
                                    print(str(p_member.name) + " - " + str(c_member.name))
                                    if c_member.id == p_member.id:
                                        exists = 1
                                if exists == 0:
                                    TargetMembers.append(p_member)
                                    TargetMembers2.append([p_member.id, p_member.name, str(p_member.roles)])
                                    t_mem_str = t_mem_str + "\n" + " " + \
                                                str(p_member.name) + " " + str(p_member.roles) + "\n"
                    else:
                        for p_member in PreCheckTargetMembers:
                            exists = 0
                            for c_member in TargetMembers:
                                print(str(p_member.name) + " - " + str(c_member.name))
                                if c_member.id == p_member.id:
                                    exists = 1
                            if exists == 0:
                                TargetMembers.append(p_member)
                                TargetMembers2.append([p_member.id, p_member.name, str(p_member.roles)])
                                t_mem_str = t_mem_str + "\n" + " " + str(p_member.name) + " " + str(
                                    p_member.roles) + "\n"
            else:
                for p_member in PreCheckTargetMembers:
                    exists = 0
                    for c_member in TargetMembers:
                        print(str(p_member.name) + " - " + str(c_member.name))
                        if c_member.id == p_member.id:
                            exists = 1
                    if exists == 0:
                        TargetMembers.append(p_member)
                        TargetMembers2.append([p_member.id, p_member.name, str(p_member.roles)])
                        t_mem_str = t_mem_str + "\n" + " " + str(p_member.name) + " " + str(p_member.roles) + "\n"
        x = 1500
        res = [t_mem_str[y - x:y] for y in range(x, len(t_mem_str) + x, x)]
        for strings in res:
            await Messages("```" + str(strings) + "```", ctx, sysChannel, None)
            await asyncio.sleep(1.75 * waitCount)
        ######################################### APPLY ROLES TO MEMBERS #########################################
        numpy.save(HomeDir + r"\Saves\Databases\ClonerDB\\" + str(TargetGuild.id) + "\TargetMembers.npy", TargetMembers2)
        await asyncio.sleep(3)
        return

async def wrapped_connect2(f):
    await f[0].start(f[1])

def to_translation_map(iterable):
    return {key: None for key in iterable}

async def similar(a, b, returnAll=0):
    exclusions = ["(", ")", "official", "video", "-", "music", "lyric", "/", "[", "]", "\\", "_", "}", "{"]
    if a is None or b is None or type(a) is type(None) or type(b) is type(None):
        if returnAll != 0:
            return 0, 0, 0, 0
        else:
            return 0
    replacements = {f'{each}': None for each in exclusions}
    a = re.sub('({})'.format('|'.join(map(re.escape, replacements.keys()))),
               lambda m: replacements[m.group()], a.lower())
    b = re.sub('({})'.format('|'.join(map(re.escape, replacements.keys()))),
               lambda m: replacements[m.group()], b.lower())
    a = re.sub(' +', ' ', a)
    b = re.sub(' +', ' ', b)
    a = a.strip()
    b = b.strip()
    sr = SequenceMatcher(None, a.lower(), b.lower(), autojunk=True)
    tdsr = txtdist.sorensen.normalized_similarity(a,b)
    matches = sr.get_matching_blocks()
    M = sum([match[2] for match in matches])
    ratio = 2 * M / (len(a) + len(b))
    tdratio = round(tdsr * 100, 2)
    if returnAll == 0:
        return tdratio
    else:
        return ratio, tdratio, a, b

async def guildCountDown():
    global counterArray, megaArray, serverData, quietOut, timers
    while True:
        guildCounter = -1
        await asyncio.sleep(300)
        if timers:
            for each in megaArray:
                guildCounter += 1
                GuildID = each[0][0][0]
                server = each[0][0][4]
                ctx = each[0][0][5]
                voice_client = each[0][0][3]
                voiceChannel = each[0][0][1]
                songNumList = each[0][0][2]
                songNumListLen = len(songNumList)
                if voiceChannel is None or type(voiceChannel) is None:
                    voiceChannelStr = "None"
                    voice_members = "None"
                    member_string = "None"
                else:
                    voiceChannelStr = voiceChannel.name
                    voice_members = voiceChannel.members
                    member_string = len(voice_members)
                if type(voice_client) is not None and voice_client is not None:
                    voice_clientSTR = str(voice_client)
                else:
                    voice_clientSTR = "None"
                print(
                    f"{Style.RESET_ALL}{Fore.LIGHTWHITE_EX}------------------------------------------------------------")
                print(f"{Style.RESET_ALL}{Fore.CYAN}Voice Channel Name: " + str(voiceChannelStr))
                print(f"{Style.RESET_ALL}{Fore.LIGHTRED_EX}Voice Channel members: " + str(member_string))
                print(f"{Style.RESET_ALL}{Fore.MAGENTA}Number of songs in current list: " + str(songNumListLen))
                print(
                    f"{Style.RESET_ALL}{Fore.LIGHTWHITE_EX}------------------------------------------------------------{Style.RESET_ALL}")
                try:
                    if member_string == None or member_string == "None" or member_string is None:
                        member_string = 0
                    else:
                        member_string = int(member_string)
                except:
                    member_string = 0
                    pass
                if member_string == 1:
                    for member in voice_members:
                        var = True
                if member_string <= 0:
                    noAppend = 0
                    counter = -1
                    for key in counterArray:
                        counter += 1
                        if key[0] == GuildID:
                            timeLeft = key[1] - 5
                            if timeLeft <= 0:
                                megaArray.pop(guildCounter)
                                noAppend = 1
                                print(f"{Fore.RED}REMOVED megaArray ENTRY FOR {server.name}!!")
                                break
                            counterArray.pop(counter)
                            counterArray.append([GuildID, timeLeft - 5])
                            noAppend = 1
                            break
                    if noAppend == 0:
                        print(f"{Fore.MAGENTA}Timer Started on megaArray ENTRY FOR {server.name}!!")
                        counterArray.append([GuildID, 30])
                if member_string > 0:
                    counter = -1
                    for key in counterArray:
                        counter += 1
                        if key[0] == GuildID:
                            counterArray.pop(counter)
                            print(f"{Fore.LIGHTYELLOW_EX}TIMER REMOVED on megaArray ENTRY FOR {server.name}!!")
        else:
            counterArray = []

async def createCollage(ctx, collageList, DIR, numbered=False, returnlist=False):

    try:
        os.mkdir(DIR)
    except:
        pass
    for filename in os.listdir(DIR):
        if "collage" not in filename:
            try:
                os.remove(DIR + filename)
            except:
                pass

    #counter = 0
    #strStr = ""
    #taskloops = []
    linksArray = []
    #imglist = []
    for each in collageList:
        URL = f"https://imgur.com/search?q={each}"
        print(URL)
        linksArray.extend(scrapeWithSoup(ctx, URL))
    print(linksArray)

    counter = 0
    #counter2 = 0
    counter3 = 0
    img = []
    #imgTotal = []

    for url in linksArray:
        counter3 += 1

        fn = posixpath.basename(urllib.parse.urlsplit(url).path)
        print(fn)
        if not os.path.exists(f"{DIR}_Image_{counter3}.{str(fn)}"):
            try:
                with open(f"{DIR}_Image_{counter3}.{str(fn)}", "wb") as f:
                    r = requests.get(url, stream=True)
                    await asyncio.sleep(0.25)
                    img.append(f"{DIR}_Image_{counter3}.{str(fn)}")
                    for block in r.iter_content(4096):
                        f.write(block)
                f.close()
                counter += 1
            except FileNotFoundError as e:
                print(f"error saving image \n {DIR}_Image_{counter3}.{str(fn)[:-3]} \n"
                      f"{e}")
                pass
        else:
            img.append(f"{DIR}_Image_{counter3}.{str(fn)}")
    img = []
    for filename in os.listdir(DIR):
        h, w, c = 0, 0, 0
        print(filename)
        if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".gif"):
            try:
                if "collage" not in filename.lower():
                    image = cv2.imread(DIR + filename)
                    h, w, c = image.shape
            except:
                h, w, c = 0, 0, 0
            if h == 0 and w == 0 and c == 0:
                var = 0
            else:
                img.append(os.path.join(DIR, filename))  ###############################378
    nImgs = []
    print(img)
    print(DIR)
    file, numimglist = await createCollage1(img, DIR, numbered)
    path = DIR + f"collage_{random.randint(random.randint(0, 100), random.randint(999, 9999))}.png"
    file.save(path)

    if returnlist is True:
        return path, numimglist
    else:
        return path
async def delMessageTask(ctx, message, count):
    global botIndexLimit, botData
    ctxData = await getCTX2(ctx, returnB="NotNone")
    ctx2 = ctxData[0]
    bot = ctxData[1]
    counter = None
    counter2 = -1
    for each in botData:
        counter2 += 1
        if each[0] == bot.user.discriminator:
            counter = each[1]
            botData.pop(counter2)
    if counter == None:
        botData.append([bot.user.discriminator, 1, bot.user.name])
    else:
        botData.append([bot.user.discriminator, counter+1, bot.user.name])
    msg = await ctx2.fetch_message(message.id)
    await asyncio.sleep(1.75 * (math.ceil(count / botIndexLimit)))
    await msg.delete()
    return
async def getSize(imageList, numbered=False):
    W = 0
    H = 0
    numimglist = []
    counter = 0
    newimglist = []
    fontlist = []
    fontprepath = HomeDir + r"\fonts\\"
    for filename in os.listdir(fontprepath):
        fontlist.append(fontprepath + filename)
    randomFontNumber = random.randint(0, len(fontlist) - 1)
    font = ImageFont.truetype(fontlist[randomFontNumber], 48)
    if imageList is None:
        h, w, c = 0, 0, 0
    for image in imageList:
        counter += 1
        im = cv2.imread(image)
        if numbered is not False:
            copyfile(image, image + "nonum" + str(".jpg"))
            numimglist.append([
            image + "nonum" + str(".jpg"), counter])
            cv2_im_rgb = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
            pil_im = Image.fromarray(cv2_im_rgb)

            draw = ImageDraw.Draw(pil_im)

            # Choose a font
            #font = ImageFont.truetype(HomeDir + "\\fonts\SOCRAEXT.TTF", 48)

            # Draw the text
            random_number = random.randint(0, 16777215)
            x = 10
            y = 10
            draw.text((5+x, 5+y), f"{counter}", font=font, fill=random_number)
            random_number = random.randint(0, 16777215)
            draw.text((-5+x, -5+y), f"{counter}", font=font, fill=random_number)
            random_number = random.randint(0, 16777215)
            draw.text((0+x, -5+y), f"{counter}", font=font, fill=random_number)
            random_number = random.randint(0, 16777215)
            draw.text((0+x, 5+y), f"{counter}", font=font, fill=random_number)
            random_number = random.randint(0, 16777215)
            draw.text((5+x, 0+y), f"{counter}", font=font, fill=random_number)
            random_number = random.randint(0, 16777215)
            draw.text((-5+x, 0+y), f"{counter}", font=font, fill=random_number)
            random_number = random.randint(0, 16777215)
            draw.text((0+x, 0+y), f"{counter}", font=font, fill=random_number)
            cv2_im_processed = cv2.cvtColor(numpy.array(pil_im), cv2.COLOR_RGB2BGR)
            cv2.imwrite(image, cv2_im_processed)
        try:
            im = cv2.imread(image)
            h, w, c = im.shape
            newimglist.append(image)
        except:
            h, w, c = 0, 0, 0
        W+=w
        H+=h
        print(f"{counter}: {h} {w} {c}")
    W = W/int(math.floor(float(math.sqrt(len(imageList)))))-(len(imageList)*3.14)
    H = H/int(math.floor(float(math.sqrt(len(imageList)))))-(len(imageList)*3.14)
    return int(W), int(H), newimglist, numimglist

def find_between(s, first, last):
    try:
        start = s.index(first) + len(first)
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        return ""


async def createCollage1(listofimages, DIR, numbered=False):
    width, height, listofimages, numimglist = await getSize(listofimages, numbered)
    rows = int(math.floor(float(math.sqrt(len(listofimages)))))
    cols = int(math.floor(float(math.sqrt(len(listofimages)))))
    thumbnail_width = width // cols
    thumbnail_height = height // rows

    size = thumbnail_width, thumbnail_height
    print(size)
    new_im = Image.new('RGB', (width, height))
    ims = []
    i = 0
    x = 0
    y = 0
    for col in range(cols):
        for row in range(rows):
            print(i, x, y)
            new_im.paste(Image.open(listofimages[i]), (x, y))
            i += 1
            y += thumbnail_height
        x += thumbnail_width
        y = 0

    return new_im, numimglist

async def getCTX(botthing, ctx):
    return await botthing.fetch_channel(ctx.channel.id)


def get_text_dimensions(text_string, font):
    ascent, descent = font.getmetrics()
    text_width = font.getmask(text_string).getbbox()[2]
    text_height = font.getmask(text_string).getbbox()[3] + descent + 30
    return (text_width, text_height)


async def generateText(ctx, botarrayswitch=None, gentextAmount=1, stringSt="", fontreq=""):
    if stringSt == "":
        gentext = str(ctx.message.content)[len(str(ctx.message.content).split(" ")[0])+1:]
    else:
        gentext = stringSt
    counterit = 0
    while counterit < gentextAmount:
        counterit += 1
        counter=0
        gentext2 = ""
        w=0
        h=0
        fontlist = []
        counterything = -1
        fontprepath = HomeDir + r"\fonts\\"
        contentStr = ""
        if fontreq == "":
            for filename in os.listdir(fontprepath):
                fontlist.append(fontprepath+filename)
            randomFontNumber = random.randint(0,len(fontlist)-1)
            font = ImageFont.truetype(fontlist[randomFontNumber], 72)
            contentStr += f" \n Selected Font: {fontlist[randomFontNumber][17:-4]} "
        else:
            ratioInfoText = ""
            for filename in os.listdir(fontprepath):
                counterything += 1
                fontlist.append(fontprepath + filename)
                ratio1, ratio2, fontString, filenameString  = await similar(fontreq, filename[:-4], returnAll=1)
                if ratio1 > 50 or ratio2 > 80:
                    if ratio1 > 50:
                        ratioInfoText = f"Block Type Pattern Match: {ratio1}"
                    else:
                        ratioInfoText = f"Sorensen Dice Pattern Match: {ratio2}"
                    break
            if ratioInfoText != "":
                font = ImageFont.truetype(fontlist[counterything], 72)
                contentStr += f" \n Selected Font: {fontlist[counterything][17:-4]} \n {ratioInfoText}"
            else:
                loop.create_task(messageHandler(ctx=ctx, lines=[" @#F Error: @#V Font not found."]))
                return
        #print(f"####### {font} #######")
        #print(f"####### {fontlist[randomFontNumber]} #######")
        textlists = []
        for each in gentext.split(" "):
            gentext2 = gentext2 + " " + each
            if counter >= 20:
                textlists.append(gentext2)
                w2, h2 = get_text_dimensions(gentext2, font)
                h = h + h2
                if w2 > w:
                    w = w2+5
                counter = 0
                gentext2 = ""
                print(w, h)
            for key in each:
                counter+=1
        if gentext2 != "":
            textlists.append(gentext2)
            w2, h2 = get_text_dimensions(gentext2, font)
            h = h + h2
            if w2 > w:
                w = w2 + 5
            counter = 0
            gentext2 = ""
        pil_im = Image.new('RGB', (w+15, h+20))
        draw = ImageDraw.Draw(pil_im)
        random_number = random.randint(0, 16777215)
        x = 10
        offset = 0
        path = HomeDir + f"\Saves\ImageGeneration\\{ctx.message.author.id}_Temp"
        for each in textlists:
            print(each)
            y = 30 + offset
            draw.text((5 + x, 5 + y), f"{each}", font=font, fill=random_number)
            random_number = random.randint(0, 16777215)
            draw.text((-5 + x, -5 + y), f"{each}", font=font, fill=random_number)
            random_number = random.randint(0, 16777215)
            draw.text((0 + x, -5 + y), f"{each}", font=font, fill=random_number)
            random_number = random.randint(0, 16777215)
            draw.text((0 + x, 5 + y), f"{each}", font=font, fill=random_number)
            random_number = random.randint(0, 16777215)
            draw.text((5 + x, 0 + y), f"{each}", font=font, fill=random_number)
            random_number = random.randint(0, 16777215)
            draw.text((-5 + x, 0 + y), f"{each}", font=font, fill=random_number)
            random_number = random.randint(0, 16777215)
            draw.text((0 + x, 0 + y), f"{each}", font=font, fill=random_number)
            offset += 95
        cv2_im_processed = cv2.cvtColor(numpy.array(pil_im), cv2.COLOR_RGB2BGR)

        try:
            os.mkdir(HomeDir + f"\Saves\ImageGeneration")
        except:
            pass
        try:
            os.mkdir(path)
        except:
            pass
        imgid = random.randint(0,1000)
        cv2.imwrite(path + f"\\genText{imgid}.png", cv2_im_processed)
        await convertImage(path + f"\\genText{imgid}.png")

        if botarrayswitch is not None:
            ctx2 = await getCTX2(ctx)
            await asyncio.ensure_future(loop.create_task(ctx2.send(file=discord.File(path + f"\\genText{imgid}.png"), content=f"-\n {contentStr}")))
            return
        await asyncio.ensure_future(loop.create_task(ctx.send(file=discord.File(path + f"\\genText{imgid}.png"), content=f"-\n{contentStr}")))
    return


async def convertImage(path):
    img = Image.open(path)
    img = img.convert("RGBA")

    datas = img.getdata()

    newData = []

    for item in datas:
        if item[0] == 0 and item[1] == 0 and item[2] == 0:
            newData.append((0, 0, 0, 0))
        else:
            newData.append(item)

    img.putdata(newData)
    img.save(path, "PNG")
    return img



async def getCTX2(ctx, returnB=None):
    global botsNick
    botthing = None
    ctx2 = None
    while botthing is None and type(botthing) is type(None):
        botthing = await getCTXBot(ctx)
        if type(botthing) is not type(None) and botthing is not None:
            if botthing.user.id == 841794419635781662 or botthing.user.id == 875712974613016637 \
                    or botthing.user.id == 866707281122426920 or botthing.user.id == 877177825415811082:
                botthing = None
        if ctx2 is None:
            if botthing is not None or type(botthing) is not type(None):
                ctx2 = await botthing.fetch_channel(ctx.channel.id)
            else:
                ctx2 = await getCTX2(ctx, returnB)
                return ctx2
        try:
            await ctx2.guild.me.edit(nick=f"{botthing.user.discriminator}#_ՏϨ_#{botthing.user.discriminator}")
            botsNick.append([ctx.guild, 1])
        except:
            pass
    if returnB is None:
        return ctx2
    else:
        return [ctx2, botthing]

async def getCTXBot(ctx):
    global botIndexLimit, botIndexCounter, botius
    botIndexCounter += 1
    if botIndexCounter > botIndexLimit:
        botIndexCounter = 0
    botthing = botius[botIndexCounter]
    return botthing


async def Messages(msgstr=None, ctx=None, sys=None, SerbzFlag=None):
    global sysChannelID
    if ctx is not None:
        await ctx.send(str(msgstr))
        await asyncio.sleep(2)
    if sys is not None:
        await sys.send(str(msgstr))
        await asyncio.sleep(2)
    return

async def getQuietMode(ctx):
    global megaArray
    quietMode = None
    for each in megaArray:
        if each[0][0][0] == ctx.guild.id:
            quietMode = each[2]
    return quietMode

def scrapeWithSoup(ctx, url):

    URL = url
    print(str(URL[27:]))
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"
        }
    data = requests.get(URL, timeout=15, headers=headers).text
    soup = BeautifulSoup(data, features="lxml")

    linksArray = []
    img_tags = soup.find_all('img')
    if "imgur" in URL:
        urls = [img['src'] for img in img_tags]
    for url in urls:
        #print(url)
        if str(url)[:2] == "//":
            url = str(url)[2:]
        if ("imgur" in str(url) or "reddit" in str(url)):
            if not "http" in str(url):
                url = f"https://{url}"
                url = url.strip()
                url = url.split(".com")
                url = f"{url[0]}.com:443{url[1]}"
            linksArray.append(url)
    print(linksArray)
    return linksArray

async def messageHandler(ctx, lines=None, msg2edit=None, system=0, quietMode=None, cloners=None,
                         image=None, file=None, components=None):
    global megaArray, sysChannel, sysChannelID, devMode
    random_number = random.randint(0, 16777215)
    if devMode is True:
        title = "DEVELOPER TEST BUILD"
    else:
        title = ""
    embedVar = discord.Embed(title=title, description="", color=random_number)
    if lines is not None:
        for line in lines:
            field, value, inline = await stringFormatting(str(line))
            embedVar.add_field(name=field, value=value, inline=inline)
        if msg2edit is None:
            if system == 0:
                if quietMode is None:
                    quietMode = await getQuietMode(ctx)
                if quietMode is None or quietMode == 2:
                    if cloners is not None:
                        ctx = await getCTX2(ctx)
                    if image is not None:
                        imgname = image.split(r"\\")[len(image.split(r"\\"))-1]
                        file2 = discord.File(f"{image}", filename = f"{imgname}")
                        embedVar.set_thumbnail(url=f"attachment://{imgname}")
                    #if embedVar is not None and embedVar == "":
                    #components = None
                    #if buttons is not None:
                    #    components = []
                    #    for each in buttons:
                    #        components.append(each)
                    #    if components == []:
                    #        components = None
                    if components is None:
                        message = await ctx.send(embed=embedVar, file=file)
                    else:
                        message = await buttons.send(embed=embedVar, channel=ctx.channel.id, components=components)
                else:
                    return None
            else:
                bottything = bots[random.randint(0,len(bots)-1)]
                sysChannel = await bottything.fetch_channel(sysChannelID)
                message = await sysChannel.send(embed=embedVar)
                if message.content != "" and message.content is not None:
                    await SerbzChannel.send(message.content)
        else:
            if ctx.message.channel.guild.id != 715341453295091713:
                try:
                    await msg2edit.delete()
                except:
                    pass
            try:
                if components is None:
                    message = ctx.send(embed=embedVar, file=file)
                else:
                    message = await buttons.send(embed=embedVar, channel=ctx.channel.id, components=components)
            except:
                pass
    return message

async def taskBuilder(ctx=None, listT=None, f=None, t=None, **kwargs):
    global linksArray
    taskloops = []
    counter = 0
    for each in listT:
        counter = counter + 1
        if counter != 1:
            #new_eventloop = asyncio.new_event_loop()
            taskloops.append(t(f(ctx=ctx, url=each)))#)#)
            await asyncio.sleep(0.1)
    return taskloops
async def taskBuilder2(ctx=None, f=None, t=None, count=None, waittime=0.01, kwargs=None, ex=None):
    global linksArray
    taskloops = []
    counter = 0
    while counter < count:
        counter = counter + 1
        #new_eventloop = asyncio.new_event_loop()
        #new_eventloop.run_until_complete(
        if ex is not None:
            taskloops.append(t(f(**kwargs, ffmpeg_opts=ex)))
        else:
            taskloops.append(t(f(**kwargs)))
        await asyncio.sleep(waittime)
    return taskloops
async def stringFormatting(string):
    global megaArray
    inline = False
    Flag = 0
    field = ""
    value = ""
    for each in string.split(" "):
        if each == "@#F":
            Flag = 1
        if each == "@#V":
            Flag = 2
        if each == "@#QW":
            inline = True
        if each[:2] != "@#":
            if Flag == 1:
                field = field + " " + each
            if Flag == 2:
                value = value + " " + each
    return field, value, inline

async def compareStrings(ctx, util=None):
    ctxSpl = str(ctx.message.content).split(" ")
    counter = 0
    stringy = ""
    for each in ctxSpl:
        if counter != 0:
            stringy += " " + each
        counter += 1
    ctxSpl = str(stringy).split("//")
    if len(ctxSpl) <= 1:
        await messageHandler(ctx=ctx, lines=[f" @#F Error: @#V split strings //"], cloners=util, quietMode=2)
        return
    else:
        ratio1, ratio2, a, b = await similar(ctxSpl[0], ctxSpl[1], returnAll=1)
        await messageHandler(ctx=ctx, lines=[f" @#F Processed: \n\n @#V \n\n ```{formatString}\n{ctxSpl[0]} \n\n"
                                             f"vs. \n\n - {ctxSpl[1]} \n.", f" @#F Similarity: \n\n @#V \n\n "
                                                                        f"Case **Ignored** \n\nRatio: "
                                            f"\n *Block Matching* algorithm: **{str(round(ratio1 * 100, 2))}%** \n"
                                             f"\n *Sorensen dice* algorithm: **{str(ratio2)}%** \n.",
                                             f" @#F Processed Strings: \n @#V \n *String A*: ```{formatString}\n{a}```\n "
                                             f"*String B*: ```{formatString}\n{b}```"], cloners=util, quietMode=2)
    return


async def determine_prefix(bot, message):
    global devMode, commandPrefix, serverData, counterArray, utilityBot, musicBot, megaArray, SerbzChannel, SerbzChannel2
    if devMode is True and bot == musicBot:
        commandPrefix = ">?"
        return commandPrefix
    if message.content[:3] == "!!!":
        commandPrefix = "!!!"
        return commandPrefix
    try:
        guildID = message.guild.id
        commandPrefix = '1!'
        if bot == musicBot:
            for each in serverData:
                if each[0] == guildID:
                    commandPrefix = each[1]
        elif bot == utilityBot:
            #print("cmdprefix")
            commandPrefix = utilbotsprefix
    except AttributeError:
        if message.channel == SerbzChannel or message.channel == SerbzChannel2:
            commandPrefix = "?"
            pass
    return commandPrefix

def Merge(dict1, dict2):
    return {**dict1, **dict2}

async def countDB(dbDict):
    dbCounter = 0
    for each, key in dbDict.items():
        array = numpy.load(key, allow_pickle=True)
        array.tolist()
        for each in array:  # 123456789012345678901234567
            dbCounter += 1  # https://youtube.com/watch?=
            print(f" {Fore.LIGHTCYAN_EX}{each[0][len(r'https://www.youtube.com/watch?v='):len(r'https://www.youtube.com/watch?v=')+11]} -- {Fore.LIGHTYELLOW_EX}{each[1][:30]}.. -"
                  f" {Fore.LIGHTMAGENTA_EX}{each[2]}{Style.RESET_ALL}")
    print(f"\n\n\n{dbCounter} entries in local database")
    return dbCounter


async def removebtnmsgs():
    global buttonmessages
    counter = -1
    for each in buttonmessages:
        counter += 1
        try:
            await each.delete()
            print(f"Button Handler2 {counter} SUCCESS")
            buttonmessages.pop(counter)
        except:
            print(f"Button Handler2 {counter} FAIL")

            buttonmessages.pop(counter)
            pass
    return




botsNick = []
locale.getdefaultlocale()
sent920 = "bad solution"
counter = -1
tts_api = VocodesAPI()
megaArray = []
botius = []
sysChannel = ""
ready = 0
deleteinprogress = 0 #### Global - should be array for per server - for delmsgs
botData = [] ### Global for just statistic data for cloners
formatString = "yaml"
sysChannelID = 871650226828619808
stopArray = []
counterArray = []  # these work
load_dotenv()
tokenCounter = 0
TOKENS = []
while tokenCounter < 7:
    tokenCounter += 1
    if tokenCounter == 1 and samuraibbot is True:
        TOKENS.append(os.getenv('DISCORD_TOKEN20'))
    else:
        TOKENS.append(os.getenv('DISCORD_TOKEN' + str(tokenCounter)))

bots: List[Bot] = []
entries = []
ahk = AHK(executable_path=r"C:\\Program Files\\AutoHotkey\\AutoHotkeyU64.exe")
addListsActive = []  # the array used for storing ctx.guild.id after add list cmd, one set of 1-5 tasks per

if os.path.exists(HomeDir + r"\Saves\PrefixDB.npy"):
    serverData = numpy.load(HomeDir + r"\Saves\PrefixDB.npy", allow_pickle=True)
else:
    serverData = []
ProjectFFMPEG = HomeDir + r"\ffmpeg_release\ffmpeg-4.4-full_build\bin\ffmpeg.exe"
ProjectFFMPEG4 = HomeDir + r"\ffmpeg_release\ffmpeg-3.0.1.tar\ffmpeg-3.0.1\ffprobe.exe"
ProjectFFMPEG2 = HomeDir + r"\ffmpeg_release\ffmpeg-4.4-full_build\bin\ffplay.exe"
ProjectFFMPEG3 = HomeDir + r"\ffmpeg_release\ffmpeg-4.4-full_build\bin\ffprobe.exe"
buttonmessages = []

AudioSegment.converter = ProjectFFMPEG
globalIteratorLimit = counter  ### wtf??
botIndexLimit = -1  #BOT ARRAY INDEX LIMIT
botIndexCounter = 0 # BOT ARRAY INDEX COUNTER
counter3, counter = -1, -1  ### wtf is this sst?
rrt = []  ### ssts all rrt
localVideoData = numpy.array([])
asciiDict = {  # genius <=== This is how the npy files for the video
    f'{each}': str(HomeDir + f"\Saves\Databases\VideoDB\{each}_array.npy") for each in ascii_lowercase
}
cases = ["-","_","0","9","8","7","6","5","4","3","2","1"]
casesDict = {
    f'{each}': str(HomeDir + f"\Saves\Databases\VideoDB\{each}_array.npy") for each in cases
}

dbDict = Merge(asciiDict, casesDict)
#DBsize = countDB(dbDict)
powderCounter = 1
powderCounter2 = 0
powderCounter3 = 0
file = open(HomeDir + "\\botToggle.txt", "r")
fileValue = file.read().strip()
if fileValue == "0":
    musicbotDisable = 0
    utilbotDisable = 1
    timers = True
    utilbotsprefix = '%'
else:
    musicbotDisable = 1
    utilbotDisable = 0
    timers = False
    utilbotsprefix = '^'
file.close()
loop = asyncio.get_event_loop()
for each in TOKENS:
    counter = counter + 1
    if counter == 0:

        bots.append(commands.Bot(command_prefix=determine_prefix, help_command=None, case_insensitive=True))#, #intents=intents))

        #bots.append(commands.Bot(command_prefix=">?", help_command=None, case_insensitive=True))#, #intents=intents))
        #ddb = DiscordButton(bots[counter])
        buttons = ButtonsClient(bots[counter])
        entries.append([bots[counter], each])
        loop.create_task(wrapped_connect2(entries[counter]))
        loop.create_task(wrapped_connect(entries[counter], bots))
    elif counter == 1 and devMode is False:
        botIndexLimit += 1
        bots.append(commands.Bot(command_prefix=determine_prefix, help_command=None, case_insensitive=True))
        entries.append([bots[counter], each])
        loop.create_task(wrapped_connect2(entries[counter]))
        loop.create_task(wrappedConnect3(entries[counter], bots))
    elif devMode is False:
        botIndexLimit += 1
        bots.append(commands.Bot(command_prefix='!@#', help_command=None, case_insensitive=True))
        entries.append([bots[counter], each])
        #loop.create_task(wrapped_connect2(entries[counter]))
        loop.create_task(wrapped_connect2(entries[counter]))
        #loop.create_task(wrappedConnect3(entries[counter], bots))
list2array = []


@buttons.click
async def btncountfunc(ctx):
    global counterButton, buttonmessages
    if ctx.message.channel.guild.id == 715341453295091713:
        return
    msgID = ctx.message.id
    channel = ctx.message.channel
    components = [
        ActionRow([
            Button(
                label="The Button",
                # style=ButtonType().Primary,
                style=random.randint(1, 4),
                custom_id="btncountfunc"
            ),
            Button(
                label="Leader Board",
                # style=ButtonType().Primary,
                style=random.randint(1, 4),
                custom_id="btnboards"
            )
        ]
        )
    ]

    #await bots[0].fetch_
    #try:
    #    await asyncio.ensure_future(loop.create_task(ctx.message.delete()))
    #except:
    #    #buttonmessages.append(ctx.message)
    #    #delmsgs = buttonmessages
    #createArrayButton.append(ctx.message.id)
    buttonmessages.append(ctx.message)
    loop.create_task(removebtnmsgs())
    #print(str([ctx.message]))
    #    pass
    #await asyncio.sleep(1)
    try:
        loop.create_task(clickgoup(ctx, components))
    except:
        pass
    await ctx.reply(content=None, channel=None, tts=False, embed=None, flags=None)
    return

async def clickgoup(ctx, components):
    global counterButton
    counterButton = int(counterButton) + 1
    with open(HomeDir + f"\Saves\TheButtonCounter.txt", "w+", encoding="utf8") as f:
        f.write(str(counterButton))
    f.close()
    if not os.path.exists(HomeDir + f"\Saves\\{ctx.member.id}"):
        os.mkdir(HomeDir + f"\Saves\\{ctx.member.id}")
    if os.path.exists(HomeDir + f"\Saves\\{ctx.member.id}\TheButtonCounter.txt"):
        with open(HomeDir + f"\Saves\\{ctx.member.id}\TheButtonCounter.txt", "r", encoding="utf8") as f:
            userButtonCounter = f.read()
        f.close()
        userButtonCounter = int(userButtonCounter.split("||")[0])
    else:
        userButtonCounter = 0
    userButtonCounter = int(userButtonCounter) + 1
    with open(HomeDir + f"\Saves\\{ctx.member.id}\TheButtonCounter.txt", "w", encoding="utf8") as f:
        f.write(str(userButtonCounter) + "||" + str(ctx.member))
    f.close()
    print(f"Button Pressed! {ctx.message.channel.guild} {ctx.member} -- {counterButton} -- {userButtonCounter}")
    loop.create_task(clickgoupmsg(ctx, userButtonCounter, counterButton, components))
    return

async def clickgoupmsg(ctx, userButtonCounter, counterButton, components):
    global buttonmessages
    try:
        message = (await messageHandler(ctx=ctx, lines=[f" @#F WOW!! @#V {ctx.member} clicked the button! \n The button has been"
                                             f" clicked **{counterButton}** times!", f" @#F **{ctx.member}** @#V Has clicked the button"
                f" **{userButtonCounter}** times \n **{ctx.member}** has contributed **{str(round(float(userButtonCounter / counterButton)*100, 2))}%**"
                        f" of the total **{counterButton}** clicks!"], components=components))
        buttonmessages.append(message)
    except:
        pass
    return

@buttons.click
async def btnboards(ctx):
    global counterButton
    if ctx.message.channel.guild.id == 715341453295091713:
        return
    components = [
        ActionRow([
            Button(
                label="The Button",
                # style=ButtonType().Primary,
                style=random.randint(1, 4),
                custom_id="btncountfunc"
            ),
            Button(
                label="Leader Board",
                # style=ButtonType().Primary,
                style=random.randint(1, 4),
                custom_id="btnboards"
            )
        ]
        )
    ]
    leaderList = []
    counter = 0
    for path in Path(HomeDir + f"\Saves").rglob('*.txt'):
        #print(path)
        if str(path) != HomeDir + r"\Saves\TheButtonCounter.txt" and path.name == "TheButtonCounter.txt":
            counter += 1
            #try:
            #with open(path, "r", encoding="utf8") as f:
            #userButtonCounter = int(str(str(f.read()).split("||")[0]))
            #print(userButtonCounter)
            score = open(path, "r", encoding="utf8")
            read = str(score.read())
            readSpl = read.split(r"||")
            print(readSpl)
            name = str(readSpl[1])
            userButtonCounter = str(readSpl[0])
            #name = str(str(f.read()).split("||")[1])
            #print(f"{name} - from file")
            leaderList.append([userButtonCounter, name, f"**{userButtonCounter}** Clicks {str(round(float(int(userButtonCounter) / counterButton) * 100, 2))}%"])
            #print(leaderList)
            score.close()
            #print("score close")
            #except:
            #    nameObj = await bots[0].fetch_user(int(str(path).split("\\")[3]))
            #    name = f"{nameObj.name}#{nameObj.discriminator}"
            #    print(name, userButtonCounter)
            #    if userButtonCounter > 1:
            #        with open(str(path), "w", encoding="utf8") as f:
            #            f.write(f"{userButtonCounter}||{name}")
            #        f.close()
            #    pass
    counter3 = 0
    leaderListStr = []
    while counter3 < 10:
        counter = -1
        counter2 = -1
        top = 0
        for each in leaderList:
            counter += 1
            if int(each[0]) > int(top):
                top = int(each[0])
                counter2 = counter
        counter3 += 1
        leaderListStr.append(f"**{counter3}.** **{leaderList[counter2][1]}** - {leaderList[counter2][2]}\n\n")
        leaderList.pop(counter2)
        #if counter >= 10:
        #    break
    msgStr = ""
    for each in leaderListStr:
        msgStr += each + "\n"
    try:
        loop.create_task(
            messageHandler(ctx=ctx, lines=[f" @#F Button Board: @#V \n.\n {msgStr}"], components=components, msg2edit=ctx.message))
    except:
        pass
    await ctx.reply(content=None, channel=None, tts=False, embed=None, flags=None)
    return

@buttons.click
async def list2next(ctx):
    msg = ctx.message
    print(msg)
    await list2cmd(ctx=ctx, page=1, msg=msg)
    await ctx.reply(content=None, channel=None, tts=False, embed=None, flags=None)
    return

@buttons.click
async def list2prev(ctx):
    msg = ctx.message
    print(msg)
    await list2cmd(ctx=ctx, page=-1, msg=msg)
    await ctx.reply(content=None, channel=None, tts=False, embed=None, flags=None)
    return

async def list2cmd(ctx, page=0, msg=None):
    global megaArray, list2array
    msgString = ""
    counter2 = 0
    currentPage = 0
   # pageset = 0
    currentPages = 0
    pagen = ""
    list2counter = -1
    getpagecounter = -1
    for key in list2array:
        if key[0] == ctx.guild.id:
            getpagecounter += 1
            currentPage = key[3]

    for key in list2array:
        list2counter += 1
        if key[0] == ctx.guild.id:
            list2array.pop(list2counter)
    for each in megaArray:
        guildID = each[0][0][0]
        if guildID == ctx.message.guild.id:
            SongList = each[0][0][2]
            if SongList is None:
                await messageHandler(ctx=ctx,
                                     lines=[f" @#F Playlist: @#V There is nothing in the list."], quietMode=2)
                return
            if SongList == [] or len(SongList) <= 0:
                await messageHandler(ctx=ctx,
                                     lines=[f" @#F Playlist: @#V There is nothing in the list."], quietMode=2)
                return
            break
    counter2 = -1
    for key in SongList:
        if len(str(key[2])) >= 45:
            stringy = "..."
        else:
            stringy = ""
        msgString = f"{msgString} **{key[1]}.** {str(key[2])[:45]}{stringy} \n"
        if len(msgString) > 500:
            counter2 = counter2 + 1
            #if counter2 == currentPage:
            list2array.append([ctx.guild.id, counter2, msgString, currentPage+page])
            if counter2 == currentPage+page:
                print(f"counter2 {counter2}, currentpage+page {currentPage+page}")
                pagen = msgString
                print(pagen)
            msgString = ""
    if pagen == "" and msgString != "":
        pagen = msgString
    components = None
    print(currentPage+page, counter2)
    if currentPage+page > 0 and currentPage+page < counter2:
        components = [
            ActionRow([
                Button(
                    label="← Prev",
                    style=random.randint(1, 4),
                    custom_id="list2prev"
                ),
                Button(
                    label="Next →",
                    # style=ButtonType().Primary,
                    style=random.randint(1, 4),
                    custom_id="list2next"
                )
            ])
        ]
    if currentPage+page == 0:
        components = [
            ActionRow([
                Button(
                    label="Next →",
                    # style=ButtonType().Primary,
                    style=random.randint(1, 4),
                    custom_id="list2next"
                )
            ])
        ]
    if currentPage+page >= counter2:
        components = [
            ActionRow([
                Button(
                    label=" ← Prev",
                    style=random.randint(1, 4),
                    custom_id="list2prev"
                )
            ])
        ]
    await messageHandler(ctx=ctx, lines=[
     f" @#F Playlist Page {currentPage+page +1}/{str(counter2 + 1)}: @#V {pagen}"], quietMode=2, components=components, msg2edit=msg)   # f"```" + f"{formatString}\n" + str(
    #pagen) + "```"],


    return list2array


musicBot = bots[0]
if devMode is False:
    utilityBot = bots[1]

loop.create_task(guildCountDown())
#loop.create_task(removebtnmsgs2())
loop.run_forever()
