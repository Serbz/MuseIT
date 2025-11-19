import discord
from discord.ext import commands
import asyncio
import os
import numpy
import random
import math
import time
import re
import urllib
import traceback
from pafy import new
from yt_dlp import YoutubeDL, DownloadError
from vocodes_api import VocodesAPI
import spotipy
import spotipy.oauth2 as oauth2
from googleapiclient.discovery import build
from urllib.parse import parse_qs, urlparse
from pathlib import Path
from colorama import Fore, Style
import psutil
from difflib import SequenceMatcher
import textdistance as txtdist
from PIL import ImageFont, ImageDraw, Image
import cv2
from os.path import join, getsize
import posixpath
from shutil import copyfile
import datetime
import requests
from bs4 import BeautifulSoup

# Import refactored files
import config
import state_manager as sm
import database_manager as db

# --- STRING & FORMATTING ---

async def messageHandler(ctx, lines=None, msg2edit=None, system=0, quietMode=None, cloners=None,
                         image=None, file=None, view: discord.ui.View = None, return_embed=False):
    """Handles sending or editing embedded messages."""
    random_number = random.randint(0, 16777215)
    title = "Test.." if config.devMode else ""
    
    message = None
    embedVar = discord.Embed(title=title, description="", color=random_number)
    
    if lines is not None:
        for line in lines:
            field, value, inline = await stringFormatting(str(line))
            embedVar.add_field(name=field, value=value, inline=inline)
    
    if return_embed:
        return embedVar

    # Determine target context/channel
    target_ctx = ctx
    if system == 1:
        target_ctx = sm.sysChannel
    if cloners is not None:
        # This logic was for utilbots, might be unused
        pass 
    
    if target_ctx is None:
        if system == 1:
             print("messageHandler: Error, sm.sysChannel is not set.")
        else:
             print("messageHandler: Error, ctx is None.")
        return None

    # Handle file/image
    file_to_send = file
    if image is not None:
        try:
            imgname = os.path.basename(image)
            file2 = discord.File(f"{image}", filename=f"{imgname}")
            embedVar.set_thumbnail(url=f"attachment://{imgname}")
            file_to_send = file2 # Send image file
        except Exception as e:
            print(f"Error attaching image to embed: {e}")
            
    # Send or Edit
    try:
        if msg2edit is None:
            # --- Send new message ---
            if system == 0:
                if quietMode is None:
                    # 'ctx' can be a Channel, Context, or Interaction
                    if isinstance(ctx, (discord.TextChannel, discord.DMChannel, discord.VoiceChannel)):
                         pass # Cannot get quiet mode from channel, assume default (None = send)
                    elif isinstance(ctx, discord.Interaction):
                         quietMode = await getQuietMode(ctx)
                    elif hasattr(ctx, 'guild'):
                         quietMode = await getQuietMode(ctx)
                
                if quietMode is None or quietMode == 2:
                    message = await target_ctx.send(embed=embedVar, file=file_to_send, view=view)
            else:
                # --- Send to system channel ---
                message = await sm.sysChannel.send(embed=embedVar, file=file_to_send, view=view)
                if sm.SerbzChannel and message and message.content:
                    await sm.SerbzChannel.send(message.content)
        else:
            # --- Edit existing message ---
            # Clear attachments when editing, as they can't be updated
            message = await msg2edit.edit(embed=embedVar, view=view, attachments=[])
            
    except discord.errors.Forbidden:
        guild_name = "DM"
        channel_name = "DM"
        if hasattr(ctx, 'guild') and ctx.guild:
            guild_name = ctx.guild.name
        if hasattr(ctx, 'channel') and ctx.channel:
            channel_name = ctx.channel.name
            
        print(f"Missing permissions to send/edit message in {guild_name} / {channel_name}")
    except discord.errors.NotFound:
        pass # Original message was deleted
    except Exception as e:
        print(f"Error in messageHandler: {e}")
        traceback.print_exc()
                
    return message


async def stringFormatting(string):
    """Parses custom formatted strings for messageHandler."""
    inline = False
    Flag = 0
    field = ""
    value = ""
    for each in string.split(" "):
        if each == "@#F":
            Flag = 1
        elif each == "@#V":
            Flag = 2
        elif each == "@#QW":
            inline = True
        elif each[:2] != "@#":
            if Flag == 1:
                field = field + " " + each
            if Flag == 2:
                value = value + " " + each
    return field.strip(), value.strip() if value else "\u200b", inline


async def printMessage(message):
    """Prints a formatted message to the console."""
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
    return


async def splitStrMsgLen(string, size=1000, send=False, channel=None, title="title"):
    """Splits a long string into multiple messages."""
    if channel is None:
        channel = sm.sysChannel
    x = size
    res = [string[y - x:y] for y in range(x, len(string) + x, x)]
    listStrs = []
    for strings in res:
        if strings.startswith("ÿþ"):
            strings = strings[2:]
        if send and channel:
            try:
                await messageHandler(ctx=channel, lines=[f" @#F {title} @#V {strings}"])
                await asyncio.sleep(2)
            except Exception as e:
                print(f"Error in splitStrMsgLen send: {e}")
        listStrs.append(strings)
    return listStrs


def lessOrMore(someInteger):
    """Pads a number with a leading zero if it's less than 10."""
    someString = str(someInteger)
    if someInteger < 10:
        someString = "0" + str(someInteger)
    return someString


async def similar(a, b, returnAll=0):
    """Compares two strings and returns a similarity ratio."""
    exclusions = ["(", ")", "official", "video", "-", "music", "lyric", "/", "[", "]", "\\", "_", "}", "{"]
    if a is None or b is None:
        return 0 if returnAll == 0 else (0, 0, a, b)
        
    replacements = {f'{each}': ' ' for each in exclusions} # Replace with space
    
    a_proc = a.lower()
    b_proc = b.lower()
    
    a_proc = re.sub('({})'.format('|'.join(map(re.escape, replacements.keys()))),
               lambda m: replacements[m.group()], a_proc)
    b_proc = re.sub('({})'.format('|'.join(map(re.escape, replacements.keys()))),
               lambda m: replacements[m.group()], b_proc)
               
    a_proc = re.sub(' +', ' ', a_proc).strip()
    b_proc = re.sub(' +', ' ', b_proc).strip()
    
    if not a_proc or not b_proc:
        return 0 if returnAll == 0 else (0, 0, a_proc, b_proc)

    sr = SequenceMatcher(None, a_proc, b_proc, autojunk=True)
    tdsr = txtdist.sorensen.normalized_similarity(a_proc, b_proc)
    
    matches = sr.get_matching_blocks()
    M = sum([match[2] for match in matches])
    ratio = (2 * M / (len(a_proc) + len(b_proc))) if (len(a_proc) + len(b_proc)) > 0 else 0
    tdratio = round(tdsr * 100, 2)
    
    if returnAll == 0:
        return tdratio
    else:
        return ratio, tdratio, a_proc, b_proc


# --- BOT & GUILD UTILS ---

async def getQuietMode(ctx):
    """Fetches the quietMode setting for the guild from megaArray."""
    global megaArray
    quietMode = None
    
    guild_id = None
    if isinstance(ctx, discord.Interaction):
        guild_id = ctx.guild_id
    elif hasattr(ctx, 'guild') and ctx.guild:
        guild_id = ctx.guild.id
    
    if not guild_id:
        return None # Not in a guild (e.g., DM)
        
    for each in sm.megaArray:
        if each[0][0][0] == guild_id:
            quietMode = each[2]
            break
    return quietMode

async def getChannel(ctx):
    """Gets the voice channel of the command author."""
    channel = None
    author = None
    
    # ctx can be Context or Interaction
    if isinstance(ctx, discord.Interaction):
        author = ctx.user
    elif hasattr(ctx, 'message'):
        author = ctx.message.author
    elif hasattr(ctx, 'author'):
        author = ctx.author

    if author and hasattr(author, 'voice') and author.voice:
        channel = author.voice.channel
        
    return channel


async def getVoice(ctx, channel):
    """Gets or creates a voice client for the guild in the specified channel."""
    if channel is None:
        return None
    
    # ctx can be Context or Interaction
    guild = ctx.guild
    if guild is None and isinstance(ctx, discord.Interaction):
        guild = ctx.guild
    if guild is None and hasattr(ctx, 'message'):
        guild = ctx.message.guild
        
    if guild is None:
        return None
        
    voice_client = discord.utils.get(sm.musicBot.voice_clients, guild=guild)
    
    if voice_client is None:
        try:
            voice_client = await channel.connect()
        except discord.errors.ClientException as e:
            print(f"Error connecting to voice: {e}. Bot might be in a disconnecting state.")
            await asyncio.sleep(2) # Wait and retry
            try:
                voice_client = await channel.connect()
            except Exception as e2:
                print(f"Retry connection failed: {e2}")
                return None
        except Exception as e:
            print(f"Other error connecting to voice: {e}")
            return None
    elif voice_client.channel != channel:
        try:
            await voice_client.move_to(channel)
        except Exception as e:
            print(f"Error moving voice channel: {e}")
            pass
            
    # Update megaArray with the new voice_client
    if not isinstance(ctx, (discord.TextChannel, discord.DMChannel, discord.VoiceChannel)):
         await sm.arrayBuilder(ctx, voice_client=voice_client)
    
    return voice_client


async def nameHandler(ctx, commandPrefix=None, specialCharacter=None, guildObject=None, clear=0, p_guild=None):
    """Updates the bot's nickname to show prefix and status."""
    if clear == 1:
        # --- Clear/Set all guilds ---
        for guild in sm.musicBot.guilds:
            commandPrefix = '1!'
            guildID = guild.id
            for key in sm.serverData:
                if key[0] == str(guildID): # Compare as strings
                    commandPrefix = key[1]
                    break
            
            specialCharacter = "" # Reset special char for each guild
            for each in sm.megaArray:
                if each[0][0][0] == guild.id:
                    if each[0][2] == 1: # Check shuffle
                        specialCharacter = "🔀"
                    break

            try:
                await guild.me.edit(nick=f"Muse{specialCharacter}IT ({commandPrefix})")
            except Exception as e:
                print(f"{Style.RESET_ALL}{Fore.LIGHTRED_EX}Unable to set nick for"
                      f" {Style.RESET_ALL}{Fore.YELLOW} {guild.name}: {e}")
            await asyncio.sleep(1) # Rate limit
        print(f"{Style.RESET_ALL}{Fore.LIGHTGREEN_EX}Nick handler finished processing all guilds.{Style.RESET_ALL}")
        return

    # --- Set for a single guild (ctx) ---
    if guildObject is None:
        if not hasattr(ctx, 'guild'): return # Cannot proceed without guild
        guildObject = ctx.guild
        
    if commandPrefix is None:
        if not hasattr(ctx, 'message'): return # Cannot get prefix without message
        commandPrefix = await sm.musicBot.get_prefix(ctx.message)

    if specialCharacter is None:
        specialCharacter = ""
        
    for each in sm.megaArray:
        if each[0][0][0] == guildObject.id:
            shuffle = each[0][2]
            if shuffle == 1:
                specialCharacter = "🔀"
            else:
                specialCharacter = "" # Ensure it's cleared if shuffle is off
            break # Found guild, stop searching
            
    try:
        await guildObject.me.edit(nick=f"Muse{specialCharacter}IT ({commandPrefix})")
    except Exception as e:
        print(f"Failed to set nick in {guildObject.name}: {e}")
    return


# --- YOUTUBE & MUSIC UTILS ---

async def getClip(stringy):
    """Searches YouTube and returns the URL of the first result."""
    music_name = stringy
    query_string = urllib.parse.urlencode({"search_query": music_name})
    try:
        with urllib.request.urlopen("https://www.youtube.com/results?" + query_string) as formatUrl:
            search_results = re.findall(r"watch\?v=(\S{11})", formatUrl.read().decode())
        if search_results:
            clip2 = "https://www.youtube.com/watch?v=" + "{}".format(search_results[0])
            return clip2
    except Exception as e:
        print(f"Error searching YouTube: {e}")
        return None
    return None


async def getVideoTitle(clip2, returnB=None, nocheck=0, video_title=None, mode="load", spopifoo=None):
    """Gets video title and duration from cache (referenceDB) or YouTube."""
    if nocheck == 0:
        videoData = await referenceDB(clip2, video_title, None, mode, spopifoo)
        if videoData is not None and videoData[1] is not None and videoData[1] != "None":
            if mode != "loadmatch" and mode != "spopify":
                print(
                    f"{Style.RESET_ALL}{Fore.LIGHTGREEN_EX}Found data for {Fore.YELLOW}{videoData[1]}{Fore.LIGHTGREEN_EX} in local database!")
            if returnB is None:
                return videoData[1]
            elif returnB == "clip2" and (mode == "loadmatch" or mode == "spopify"):
                return videoData[0], videoData[1], videoData[2], videoData[3] # clip, title, duration, matchInfo
            elif returnB == "clip2" or mode == "load" and returnB != "notNone":
                return videoData[0], videoData[1], videoData[2] # clip, title, duration
            else:
                return videoData[1], videoData[2] # title, duration

    if clip2 is None and video_title is not None:
        clip2 = await getClip(video_title)
        if clip2 is None: # Search failed
            return "error 298", "" if returnB else "error 298"

    with YoutubeDL(config.ydl_opts) as ydl:
        try:
            info_dict = ydl.extract_info(clip2, download=False)
            video_title_out = info_dict.get('title', None)
            video_duration_out = info_dict.get('duration', None)
            video_id = info_dict.get('id', None)
            
            if video_id: # Use the proper video ID
                clip2 = f"https://www.youtube.com/watch?v={video_id}"
            
            sm.loop.create_task(referenceDB(clip2, video_title_out, video_duration_out, "save"))
            if returnB is None:
                return video_title_out
            else:
                return video_title_out, video_duration_out
        except DownloadError as e:
            print(f"YTDL DownloadError: {e}")
            if returnB is None:
                return "error 298"
            else:
                return "error 298", ""
        except Exception as e:
            print(f"YTDL generic error: {e}")
            if returnB is None:
                return "error 298"
            else:
                return "error 298", ""


async def referenceDB(clip2, video_title, video_duration, mode, spopifoo=None):
    """Caches and retrieves video metadata from the SQLite database."""
    
    # --- Mode 1: clip2 is provided (Save or Load) ---
    if clip2 is not None:
        video_id = None
        if "watch?v=" in clip2:
            video_id = clip2.split("watch?v=")[1][:11]
        
        if not video_id:
            return None # Invalid clip URL

        if mode == "load":
            return db.get_video_cache(video_id) # Returns [clip_url, title, duration] or None
        
        if mode == "save":
            db.set_video_cache(video_id, clip2, video_title, video_duration)
            return # Save and exit
        
        if mode == "spopify" and spopifoo:
            # This mode seems to be for saving a spotify search result
            db.set_spotify_cache(spopifoo, clip2, video_title, video_duration, video_id)
            return

    # --- Mode 2: video_title is provided (Search) ---
    elif (clip2 is None and video_title is not None) or mode == "loadmatch":
        if not video_title: return None
        
        # This mode is for finding a video by title.
        # The old .npy implementation searched all cached titles.
        # This is very inefficient with SQL.
        # We will instead search Spotify cache first, then YouTube.
        
        # 1. Check Spotify cache first (if mode is spopify or loadmatch)
        cached_spotify_result = db.get_spotify_cache(video_title)
        if cached_spotify_result:
            # [clip_url, title, duration, video_id]
            match_info = f"Matched Spotify Cache: {cached_spotify_result[1][:20]}.."
            return [cached_spotify_result[0], cached_spotify_result[1], cached_spotify_result[2], match_info]

        # 2. If not found, search YouTube (this is what getClip does)
        # The old logic for title matching the DB is removed as it's slow
        # and inefficient. We will just search YouTube directly.
        
        # This function should just be for *caching*, not searching.
        # The search logic is now in getVideoTitle.
        # If we're here, it means it wasn't in the cache.
        
        if mode == "loadmatch" and spopifoo:
             # This is a spotify search, we'll cache the result *after* getClip/getVideoTitle
             pass

    return None # No match found in cache


# --- TEXT & IMAGE GENERATION ---

async def commandSplitter(ctx, command="", cmdSelString="!@#", mode=0):
    """Parses arguments for commands like 'gt'."""
    stringy = ""
    arg1 = 1      # e.g., count
    arg2 = ""      # e.g., font
    arg3 = None    # e.g., None
    
    if ctx is not None:
        ctxSpl = str(ctx.message.content).split(" ")
        selective = 0
        skipNext = 0
        text_parts = []
        
        for i, each in enumerate(ctxSpl):
            if i == 0: continue # Skip command name
            
            if skipNext:
                skipNext = 0
                continue
            
            # Check for flags
            if each.startswith("-") or each.startswith(cmdSelString):
                selective = 1
                if each == "-c" or each == "--count":
                    try:
                        arg1 = int(ctxSpl[i + 1])
                        if arg1 > 10: arg1 = 10 # Limit
                        skipNext = 1
                    except:
                        pass # Ignore invalid count
                elif each == "-f" or each == "--font":
                    try:
                        arg2 = ctxSpl[i + 1]
                        skipNext = 1
                    except:
                        pass # Ignore invalid font
                continue # Skip the flag itself from being added to stringy
            
            # If not a flag, add to text
            text_parts.append(each)

        stringy = " ".join(text_parts).strip()
                
    return stringy, arg1, arg2, arg3


async def generateText(ctx, botarrayswitch=None, gentextAmount=1, stringSt="", fontreq=""):
    """Generates an image with styled text."""
    if stringSt == "":
        gentext = " ".join(ctx.message.content.split(" ")[1:])
    else:
        gentext = stringSt
        
    if not gentext:
        # Re-parse arguments if stringSt was empty
        gentext, gentextAmount, fontreq, _ = await commandSplitter(ctx, command="gt", cmdSelString="!@#")
        
    if not gentext:
        await messageHandler(ctx=ctx, lines=[" @#F Error: @#V No text provided."])
        return

    counterit = 0
    while counterit < gentextAmount:
        counterit += 1
        
        fontprepath = os.path.join(config.HomeDir, "fonts")
        fontlist = []
        try:
            fontlist = [os.path.join(fontprepath, f) for f in os.listdir(fontprepath) if f.endswith(('.ttf', '.otf'))]
        except FileNotFoundError:
            print(f"Fonts directory not found at {fontprepath}")
            pass # Handled below
        
        if not fontlist:
            await messageHandler(ctx=ctx, lines=[" @#F Error: @#V No fonts found in fonts directory."])
            return
            
        selected_font_path = ""
        contentStr = ""
        
        if fontreq == "":
            selected_font_path = random.choice(fontlist)
            font_name = os.path.basename(selected_font_path)
            contentStr += f" \n Selected Font: {font_name} "
        else:
            best_match_ratio = 0
            best_match_font = ""
            for font_path in fontlist:
                filename = os.path.basename(font_path)
                ratio1, ratio2, _, _ = await similar(fontreq, filename.rsplit('.', 1)[0], returnAll=1)
                
                current_ratio = max(ratio1, ratio2)
                if current_ratio > best_match_ratio:
                    best_match_ratio = current_ratio
                    best_match_font = font_path
                if best_match_ratio > 95:
                    break
                    
            if best_match_ratio > 50: # 50% similarity threshold
                selected_font_path = best_match_font
                font_name = os.path.basename(selected_font_path)
                contentStr += f" \n Selected Font: {font_name} (Match: {best_match_ratio}%)"
            else:
                await messageHandler(ctx=ctx, lines=[f" @#F Error: @#V Font '{fontreq}' not found. Using random."])
                selected_font_path = random.choice(fontlist)

        try:
            font = ImageFont.truetype(selected_font_path, 72)
        except Exception as e:
            print(f"Error loading font {selected_font_path}: {e}")
            await messageHandler(ctx=ctx, lines=[" @#F Error: @#V Could not load font. Using default."])
            font = ImageFont.load_default()

        # --- Calculate Image Size ---
        words = gentext.split()
        lines = []
        line = ""
        max_w = 0
        total_h = 0
        
        for word in words:
            # Check width of line with new word
            temp_line = f"{line} {word}" if line else word
            try:
                line_w, line_h = get_text_dimensions(temp_line, font)
            except:
                line_w, line_h = len(temp_line) * 30, 70 # Estimate
            
            if line_w > 800 and line: # Max 800px width, and line must not be empty
                lines.append(line) # Add the line *before* the word
                line = word # Start new line
            else:
                line = temp_line # Add word to current line
                
        lines.append(line) # Add the last line

        for line in lines:
            try:
                w, h = get_text_dimensions(line, font)
                if w > max_w: max_w = w
                total_h += (h + 10) # Add 10px spacing
            except:
                total_h += 80 # Estimate

        if max_w == 0: max_w = 300
        if total_h == 0: total_h = 100
        
        pil_im = Image.new('RGB', (max_w + 30, total_h + 20), (0,0,0)) # Black background
        draw = ImageDraw.Draw(pil_im)
        
        x = 15 # Padding
        y = 10 # Padding
        
        for line in lines:
            try:
                # --- Draw text with outline ---
                draw.text((x-2, y-2), line, font=font, fill=(255,255,255))
                draw.text((x+2, y-2), line, font=font, fill=(255,255,255))
                draw.text((x-2, y+2), line, font=font, fill=(255,255,255))
                draw.text((x+2, y+2), line, font=font, fill=(255,255,255))
                
                # --- Draw colored text ---
                random_color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
                draw.text((x, y), line, font=font, fill=random_color)
                
                _, h = get_text_dimensions(line, font)
                y += (h + 10) # Add 10px spacing
            except:
                y += 80 # Default line height

        cv2_im_processed = cv2.cvtColor(numpy.array(pil_im), cv2.COLOR_RGB2BGR)

        path_dir = config.HomeDir + f"/Saves/ImageGeneration/{ctx.message.author.id}_Temp"
        os.makedirs(path_dir, exist_ok=True)
        
        imgid = random.randint(0, 1000)
        img_path = os.path.join(path_dir, f"genText{imgid}.png")
        
        cv2.imwrite(img_path, cv2_im_processed)
        await convertImage(img_path) # Make transparent

        try:
            await ctx.send(file=discord.File(img_path), content=f"-\n{contentStr}")
            os.remove(img_path)
        except Exception as e:
            print(f"Error sending generated text: {e}")
    return


def get_text_dimensions(text_string, font):
    """Calculates width and height of a text string given a font."""
    try:
        # Use textbbox for more accurate size
        bbox = font.getbbox(text_string)
        text_width = bbox[2] - bbox[0] # right - left
        text_height = bbox[3] - bbox[1] # bottom - top
        return (text_width, text_height + 10) # Add padding
    except Exception:
        # Fallback for older PIL/Pillow
        ascent, descent = font.getmetrics()
        text_width = font.getmask(text_string).getbbox()[2]
        text_height = font.getmask(text_string).getbbox()[3] + descent + 30
        return (text_width, text_height)


async def convertImage(path):
    """Converts the black background of an image to transparent."""
    try:
        img = Image.open(path)
        img = img.convert("RGBA")
        datas = img.getdata()
        newData = []
        for item in datas:
            if item[0] == 0 and item[1] == 0 and item[2] == 0:
                newData.append((0, 0, 0, 0)) # Transparent
            else:
                newData.append(item)
        img.putdata(newData)
        img.save(path, "PNG")
        return img
    except Exception as e:
        print(f"Error converting image to transparent: {e}")
        return None

# --- SECRET 'u' COMMAND UTILS ---

def SF_outputOrWhatever(SF_SeedVar, seedTime, pinQMark, bigCount, mult, floater):
    """Logs output for the 'u' command."""
    seedLogPath = r"C:\ProgramData\Tree.log" # This path is hardcoded
    try:
        with open(seedLogPath, "a") as f:
            f.write(
                f"Time: {seedTime} - Seed: {SF_SeedVar}\n{str(pinQMark)} = ( {str(bigCount)[1:]} * {floater} )[len-4:len]\n\n")
    except Exception as e:
        print(f"Error writing to Tree.log: {e}")
    return


def SF_someFunction(SF_SeedVar, SF_fourDigitStr, seedTime, bigCount):
    """Core logic for the 'u' command."""
    if str(SF_fourDigitStr).startswith("0"):
        SF_fourDigitStr = int("1" + str(SF_fourDigitStr)[1:])
        
    floater = round(float(seedTime) * int(SF_fourDigitStr))
    mult = str(int(str(floater)) * int(str(bigCount)))
    pinQMark = str(mult)[len(mult) - 4:len(mult)]
    
    SF_outputOrWhatever(SF_SeedVar, seedTime, pinQMark, bigCount, mult, floater)
    
    return str( f"{floater} {bigCount} {mult} {pinQMark} \n\n"
        f"Time: {seedTime} - Seed: {SF_SeedVar}\n{str(pinQMark)} = "
        f"( {str(bigCount)[1:]} * {floater} )[len-4:len]\n\n"
    )


def SF_getSeed(Cases, AsciiDict):
    """Generates a seed for the 'u' command."""
    DICKSHUNARY = {*AsciiDict, *Cases}
    eyes = list(DICKSHUNARY)
    nose = []
    for _ in range(len(eyes)): # Scramble
        ran = random.randint(0, len(eyes) - 1)
        nose.append(eyes[ran])
        
    noseString = re.sub(r'[\[\]\{\}\,\s\']', "", str(nose))
    
    try:
        with open(config.HomeDir + r"seed.log", "w") as fILe:
            fILe.write(noseString)
    except Exception as e:
        print(f"Error writing seed.log: {e}")
        
    return noseString


def SF_seedVal(SF_SeedVar, Cases):
    """Calculates seed value for 'u' command."""
    smolCount = 0
    bigCount = 0
    nonIterable = list(config.ascii_lowercase) + Cases
    
    for each in nonIterable:
        for eacha in SF_SeedVar:
            smolCount += 1
            if each == eacha:
                bigCount += smolCount
                break
    return smolCount, bigCount