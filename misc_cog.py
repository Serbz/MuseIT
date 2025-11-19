import discord
from discord.ext import commands
import asyncio
import os
import sys
import random
import time
import traceback
import psutil
import requests
import cv2
import math
import posixpath
import urllib
from bs4 import BeautifulSoup
from shutil import copyfile
from PIL import Image, ImageDraw, ImageFont
from colorama import Fore, Style

# Import new discord.ui components
from discord.ui import View, Button, button
from discord import ButtonStyle

# Import refactored files
import config
import state_manager as sm
import database_manager as db
from helper_utils import (
    messageHandler, nameHandler, splitStrMsgLen, similar,
    commandSplitter, generateText, SF_getSeed, SF_seedVal, SF_someFunction
)
from state_manager import arrayBuilder

# -----------------------------------------------------------------
# View Classes (Misc Specific)
# -----------------------------------------------------------------

class ButtonView(View):
    """A persistent view for 'The Button'."""
    def __init__(self, misc_cog_instance):
        super().__init__(timeout=None) # Persistent
        self.misc_cog = misc_cog_instance

    @button(label="The Button", style=ButtonStyle.primary, custom_id="btncountfunc")
    async def button_callback(self, interaction: discord.Interaction, button: Button):
        # Change button color on click
        button.style = random.choice([ButtonStyle.primary, ButtonStyle.secondary, ButtonStyle.green, ButtonStyle.red])
        await interaction.response.edit_message(view=self)
        
        # Call the cog's logic
        await self.misc_cog.handle_button_click(interaction)

    @button(label="Leader Board", style=ButtonStyle.secondary, custom_id="btnboards")
    async def leaderboard_callback(self, interaction: discord.Interaction, button: Button):
        # Call the cog's logic
        await self.misc_cog.handle_leaderboard_click(interaction)


# -----------------------------------------------------------------
# Misc Cog
# -----------------------------------------------------------------

class MiscCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # --- BUTTON HANDLER LOGIC ---
    
    async def handle_button_click(self, interaction: discord.Interaction):
        """Logic for when 'The Button' is clicked. (Called by ButtonView)"""
        if interaction.guild_id == 715341453295091713:
            return
        
        # --- Logic from old clickgoup ---
        sm.counterButton = int(sm.counterButton) + 1
        with open(config.HomeDir + f"/Saves/TheButtonCounter.txt", "w+", encoding="utf8") as f:
            f.write(str(sm.counterButton))
        
        member = interaction.user
        user_file = config.HomeDir + f"/Saves/{member.id}/TheButtonCounter.txt"
        os.makedirs(os.path.dirname(user_file), exist_ok=True)
        
        userButtonCounter = 0
        if os.path.exists(user_file):
            try:
                with open(user_file, "r", encoding="utf8") as f:
                    userButtonCounter = f.read()
                userButtonCounter = int(userButtonCounter.split("||")[0])
            except (IOError, IndexError, ValueError):
                userButtonCounter = 0
        
        userButtonCounter += 1
        with open(user_file, "w", encoding="utf8") as f:
            f.write(str(userButtonCounter) + "||" + str(member))
        
        print(f"Button Pressed! {interaction.guild} {member} -- {sm.counterButton} -- {userButtonCounter}")

        # --- Logic from old clickgoupmsg ---
        lines = [
            f" @#F WOW!! @#V {member.mention} clicked the button! \n The button has been clicked **{sm.counterButton}** times!",
            f" @#F **{member.display_name}** @#V Has clicked the button **{userButtonCounter}** times \n **{member.display_name}** has contributed **{str(round(float(userButtonCounter / sm.counterButton) * 100, 2))}%**"
            f" of the total **{sm.counterButton}** clicks!"
        ]
        
        try:
            # Send as a new message.
            embed = await messageHandler(ctx=None, lines=lines, return_embed=True)
            new_view = ButtonView(self) # Send a new set of buttons
            await interaction.channel.send(embed=embed, view=new_view)
        except Exception as e:
            print(f"Error sending button followup: {e}")
        return


    async def handle_leaderboard_click(self, interaction: discord.Interaction):
        """Logic for when 'Leader Board' button is clicked. (Called by ButtonView)"""
        if interaction.guild_id == 715341453295091713:
            await interaction.response.send_message("Not here!", ephemeral=True)
            return

        leaderList = []
        counter = 0
        total_clicks = sm.counterButton
        
        save_dir = os.path.join(config.HomeDir, "Saves")
        for user_id_dir in os.listdir(save_dir):
            user_file = os.path.join(save_dir, user_id_dir, "TheButtonCounter.txt")
            
            if os.path.isfile(user_file):
                counter += 1
                try:
                    with open(user_file, "r", encoding="utf8") as score:
                        read = str(score.read())
                    readSpl = read.split(r"||")
                    if len(readSpl) >= 2:
                        name = str(readSpl[1])
                        userButtonCounter = int(readSpl[0])
                        percentage = (float(userButtonCounter) / total_clicks) * 100 if total_clicks > 0 else 0
                        leaderList.append([userButtonCounter, name,
                                           f"**{userButtonCounter}** Clicks ({str(round(percentage, 2))}%)"])
                except Exception as e:
                    print(f"Error reading leaderboard file {user_file}: {e}")
        
        leaderList.sort(key=lambda x: x[0], reverse=True) # Sort by score
        
        leaderListStr = []
        for i, each in enumerate(leaderList[:10]): # Get top 10
            leaderListStr.append(f"**{i + 1}.** **{each[1]}** - {each[2]}")

        msgStr = "\n\n".join(leaderListStr)
        if not msgStr:
            msgStr = "No one has clicked the button yet!"
            
        try:
            # Send the leaderboard as a response
            embed = await messageHandler(ctx=None, lines=[f" @#F Button Board (Top 10): @#V \n----------------\n {msgStr}"], return_embed=True)
            await interaction.response.send_message(embed=embed, ephemeral=True) # Ephemeral: only user sees it
        except Exception as e:
            print(f"Error sending leaderboard: {e}")
        return

    # --- MISC COMMANDS ---

    @commands.command(name="u")
    @commands.is_owner() # Restrict to bot owner
    async def idkCommand(self, ctx):
        """Undocumented 'u' command."""
        Cases = ["-", "_", "0", "9", "8", "7", "6", "5", "4", "3", "2", "1"]
        AsciiDict = {f'{each}' for each in config.ascii_lowercase}
        DICKSHUNARY, SF_SeedVar = None, None
        seedTime2 = time.time()
        seedTime = str(round(seedTime2))
        SF_SeedVar = SF_getSeed(Cases, AsciiDict)
        if SF_SeedVar == "":
            SF_SeedVar = SF_getSeed(Cases, AsciiDict)
        smolCount, bigCount = SF_seedVal(SF_SeedVar, Cases)
        SF_fourDigitStr = str(bigCount)[1:]
        returnStr = SF_someFunction(SF_SeedVar, SF_fourDigitStr, seedTime, bigCount)
        if sm.SerbzChannel:
            await messageHandler(ctx=sm.SerbzChannel, lines=[f" @#F Complete: @#V . \n {returnStr}"])
        if sm.SerbzChannel2:
            await messageHandler(ctx=sm.SerbzChannel2, lines=[f" @#F Complete: @#V . \n {returnStr}"])
        return

    @commands.command(name="button")
    async def discpycomp(self, ctx):
        """Spawns 'The Button'."""
        # This command now sends the persistent view
        view = ButtonView(self)
        await ctx.send(content="Here is a button!", view=view)
        return

    @commands.command(name="inv")
    @commands.is_owner()
    async def invite(self, ctx):
        """Generates a server invite. (Owner DM only)"""
        commandPrefix = await self.bot.get_prefix(ctx.message)
        if isinstance(ctx.channel, discord.DMChannel):
            if "inv" in ctx.message.content.lower() and len(ctx.message.content) > len(commandPrefix)+4:
                servername = str(ctx.message.content).split(f"inv")[1].strip()
                print(f"{Fore.RED}Owner DM - inv[1] = {servername}")
                guild_found = None
                for guild in self.bot.guilds:
                    if servername.lower().strip() in guild.name.lower().strip() or \
                       servername.strip() == str(guild.id):
                        guild_found = guild
                        break
                
                if guild_found:
                    print(f"{Fore.RED}{servername}{Fore.LIGHTWHITE_EX} == {Fore.LIGHTGREEN_EX}{guild_found.name}")
                    for textChan in guild_found.text_channels:
                        if textChan.permissions_for(guild_found.me).create_instant_invite:
                            try:
                                invite = await textChan.create_invite(max_uses=1, unique=True, max_age=300)
                                await ctx.send(f"Invite for **{guild_found.name}**:\n{invite}")
                                return
                            except Exception as e:
                                print(f"Failed to create invite in {textChan.name}: {e}")
                    await ctx.send(f"Could not create an invite for {guild_found.name}. No channels with perms found.")
                else:
                    await ctx.send(f"Could not find a guild matching '{servername}'.")

            elif len(ctx.message.content) == len(commandPrefix)+3:
                guildString = ""
                for guild in sm.musicBot.guilds:
                    guildString += f"{guild.name} ({guild.id})\n"
                await splitStrMsgLen("\n" + guildString, send=True, channel=ctx.channel, title="Guilds: ")
        return

    @commands.command(name="compare")
    async def musicCompareStrings(self, ctx):
        """Compares two strings for similarity."""
        ctxSpl = str(ctx.message.content).split(" ")
        counter = 0
        stringy = ""
        for each in ctxSpl:
            if counter != 0:
                stringy += " " + each
            counter += 1
        ctxSpl = str(stringy).split("//")
        if len(ctxSpl) <= 1:
            await messageHandler(ctx=ctx, lines=[f" @#F Error: @#V split strings //"], cloners=None, quietMode=2)
            return
        else:
            ratio1, ratio2, a, b = await similar(ctxSpl[0], ctxSpl[1], returnAll=1)
            await messageHandler(ctx=ctx, lines=[f" @#F Processed: \n\n @#V \n\n{ctxSpl[0]} \n\n"
                                                 f"vs. \n\n - {ctxSpl[1]} \n.", f" @#F Similarity: \n\n @#V \n\n "
                                                                                f"Case **Ignored** \n\nRatio: "
                                                                                f"\n *Block Matching* algorithm: **{str(round(ratio1 * 100, 2))}%** \n"
                                                                                f"\n *Sorensen dice* algorithm: **{str(ratio2)}%** \n.",
                                                 f" @#F Processed Strings: \n @#V \n *String A*: ```{config.formatString}\n{a}```\n "
                                                 f"*String B*: ```{config.formatString}\n{b}```"], cloners=None, quietMode=2)
        return

    @commands.command(name="quiet")
    async def quiet(self, ctx):
        """Toggles quiet mode for the bot in the current guild."""
        quietMode = None
        for each in sm.megaArray:
            if each[0][0][0] == ctx.guild.id:
                quietMode = each[2]
                break
        
        if quietMode is None or quietMode == 0:
            quietMode = 1
            stringy = "active"
        else:
            quietMode = None
            stringy = "inactive"
            
        sm.loop.create_task(messageHandler(ctx=ctx,
                                        lines=[f" @#F Quiet Mode: @#V Toggled - {stringy}"], quietMode=2))
        sm.loop.create_task(arrayBuilder(ctx, quietMode=quietMode))
        return

    @commands.command(name="cf")
    @commands.is_owner()
    async def changeformat(self, ctx):
        """Changes the format string (Owner only)."""
        config.formatString = str(ctx.message.content).split(" ")[1]
        await ctx.send(f"Format string set to: {config.formatString}")
        return

    @commands.command(name="fixnames")
    @commands.is_owner()
    async def fixnames(self, ctx):
        """Fixes bot nicknames in all guilds (Owner only)."""
        await nameHandler(None, clear=1)
        await ctx.send("Fixnames task initiated.")
        return

    @commands.command(name="cf2")
    @commands.is_owner()
    async def changeformat2(self, ctx):
        """Sends a multi-line message (Owner only)."""
        lines = []
        for each in str(ctx.message.content)[5:].split("||"):
            lines.append(each)
        sm.loop.create_task(messageHandler(ctx, lines, quietMode=2))
        return

    @commands.command(name=r"m")
    @commands.is_owner()
    async def restart(self, ctx):
        """Restarts the bot (Owner only)."""
        print(f"{Fore.RED}RESTARTING{Fore.LIGHTWHITE_EX}")
        if sm.sysChannel:
            await messageHandler(ctx=sm.sysChannel, lines=[f" @#F Restarting: @#V ;)"])
        
        sm.loop.create_task(messageHandler(ctx=ctx, lines=[
            "@#F RESTART INITIATED: @#V disconnecting voice clients..."], system=1))
        
        for each in sm.megaArray:
            voiceClient = each[0][0][3]
            if voiceClient:
                print(f"{Fore.MAGENTA}Disconnecting voice client in {each[0][0][0]}")
                try:
                    await voiceClient.disconnect()
                except:
                    pass
        
        # Save sessions before restart (optional)
        # for each in sm.megaArray:
        #     db.save_session(each[0][0][0], each)
            
        with open(config.HomeDir + r"/botToggle.txt", "w", encoding='utf8',
                  errors="ignore") as text_file:
            text_file.write("0")
        
        os.execv(sys.executable, ['python'] + sys.argv)
        SystemExit()
        sys.exit()
        
    @commands.command(name=r"cmd")
    @commands.is_owner()
    async def cmdCmd(self, ctx):
        """Executes a command line script (Owner only)."""
        if sm.ahk is None:
            await ctx.send("AHK is not initialized. Command disabled.")
            return

        cmd = ctx.message.content
        commandPrefix = await self.bot.get_prefix(ctx.message)
        cmd = cmd[len(commandPrefix)+len("cmd "):len(cmd)]
        
        log_file = config.HomeDir + "cmdOut.log"
        
        try:
            sm.ahk.run_script(fr"Run, cmd.exe /c del /f /q {log_file}", blocking=True)
            await asyncio.sleep(0.5)
            sm.ahk.run_script(fr"Run, powershell.exe -c touch {log_file}", blocking=True)
            await asyncio.sleep(0.5)
            sm.ahk.run_script(fr"Run, powershell.exe -c {cmd} >> {log_file}, , Min", blocking=False)
            await asyncio.sleep(0.5)
            
            counter = 1
            O_counter = 0
            T_counter = 0
            while (counter != O_counter and T_counter <= 40) or (not os.path.exists(log_file) and T_counter <= 3):
                if os.path.exists(log_file):
                    O_counter = counter
                    try:
                        counter = os.stat(log_file).st_size
                    except FileNotFoundError:
                        counter = O_counter # File deleted mid-check
                await asyncio.sleep(1)
                T_counter+=1
            
            with open(log_file, "r") as f:
                out = str(f.read())

            out_list = out.split(" ")
            out2 = " ".join(each for each in out_list if each.strip() and len(each) > 1)
            
            print(out2)
            x = 1000
            res = [out2[y - x:y] for y in range(x, len(out2) + x, x)]
            for strings in res:
                if strings.startswith("ÿþ"):
                    strings = strings[2:]
                await messageHandler(ctx=ctx, lines=[f" @#F Output: @#V ```yaml\n" + str(strings) + "```"])
                await asyncio.sleep(2)
        except Exception as e:
            await messageHandler(ctx=ctx, lines=[f" @#F Error: @#V ```yaml\n{e}```"])
        return
    
    @commands.command(name="announce")
    @commands.is_owner()
    async def announce(self, ctx):
        """Sends an announcement to all guilds (Owner only)."""
        commandPrefix = await self.bot.get_prefix(ctx.message)
        a_msg = ctx.message.content[len(commandPrefix)+len("announce "):len(ctx.message.content)]
        
        uselist = True
        listFile = []
        try:
            with open(config.HomeDir + r"announcelist.txt", "r") as f:
                listFile = f.read().split("\n")
        except FileNotFoundError:
            uselist = False
            
        if not listFile or listFile == ['']:
            uselist = False
            
        logmsg = "Announcement Sent: \n "
        logerrmsg = "403 Forbidden: \n "
        
        for guild in sm.musicBot.guilds:
            passvar = 1 # 1 = skip, 0 = send
            
            if uselist:
                for each in listFile:
                    try:
                        eachint = int(each)
                        if eachint == guild.id:
                            passvar = 0
                            break
                    except ValueError:
                        pass # Ignore non-integer lines in list
            else:
                passvar = 0 # Send to all if no list
            
            if passvar == 0:
                sent_to_guild = False
                for text_chan in guild.text_channels:
                    tn = text_chan.name.lower()
                    if ("spam" in tn or "command" in tn or "general" in tn or "bot" in tn):
                        # Check perms
                        if not text_chan.permissions_for(guild.me).send_messages:
                            continue
                            
                        for strings in (await splitStrMsgLen(a_msg, 1000)):   
                            try:
                                await messageHandler(ctx=text_chan, lines=[f" @#F Announcement: @#V {strings}"])
                                logmsg = logmsg + f"{guild.name} - {tn}\n"
                                sent_to_guild = True
                                print(f"{guild.name} - {tn} - {a_msg}")
                                await asyncio.sleep(2)
                                break # Move to next guild
                            except discord.errors.Forbidden as e:
                                logerrmsg = logerrmsg + f"{guild.name} - {tn}\n"
                                await asyncio.sleep(1)
                                break # Stop trying this guild if forbidden
                            except Exception as e:
                                print(f"Error sending to {guild.name} - {tn}: {e}")
                                await asyncio.sleep(1)
                                
                    if sent_to_guild:
                        break # Already sent to this guild
                        
        await splitStrMsgLen(string=logmsg, send=True, channel=ctx.channel, title="Announcement Log: ")
        await splitStrMsgLen(string=logerrmsg, send=True, channel=ctx.channel, title="Announcement Log: ")
        return
    
    @commands.command(name='oauth')
    async def oauth(self, ctx):
        """Sends the bot's OAuth2 invite link."""
        sm.loop.create_task(messageHandler(ctx=ctx, lines=[" @#F Oauth2 Link: @#V "
                                                        "<https://discord.com/api/oauth2/authorize?client_id=866707281122426920&permissions=137543667393&scope=bot>"
                                                        f"```{config.formatString}\nAdd me to your server :) ```"],
                                        quietMode=2))
        return

    @commands.command(name="sys")
    @commands.is_owner()
    async def syssettings(self, ctx):
        """Displays system settings (Owner only)."""
        message2del = await ctx.send("Please Wait..")
        
        # dbCount = 0 # await countDB(config.dbDict) # This function was very slow, disabling for now
        
        await message2del.delete()
        sm.loop.create_task(messageHandler(ctx=ctx, lines=[f" @#F System Settings: @#V "
                                                        f"Servers: {len(self.bot.guilds)}\n"
                                                        f"Latency: {round(self.bot.latency * 1000, 2)}ms\n"
                                                        f"Memory Usage: {str(round(psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2, 2))}mb\n"
                                                        f"quietOut: {config.quietOut}\n"
                                                        f"accTimers: {config.accTimers}\n"
                                                        f"timers: {config.timers}\n"
                                                        f"musicBotDisable: {config.musicbotDisable}\n"
                                                        f"current active timers: {len(sm.counterArray)} \n"
                                                        f"current entries in megaArray: {len(sm.megaArray)} \n"
                                                        f"DB Path: {config.DB_PATH}"], quietMode=2))
        return

    @commands.command(name="timers")
    @commands.is_owner()
    async def toggletimers(self, ctx):
        """Toggles the voice channel activity timer (Owner only)."""
        config.timers = not config.timers
        await ctx.send(f"Timers set to: {config.timers}")
        return

    @commands.command(name="accurate-timers")
    @commands.is_owner()
    async def accuratetimers(self, ctx):
        """Toggles accurate timers setting (Owner only)."""
        config.accTimers = not config.accTimers
        await ctx.send(f"Accurate timers set to: {config.accTimers}")
        return

    @commands.command(name="quietout")
    @commands.is_owner()
    async def quietMode(self, ctx):
        """Toggles quiet output setting (Owner only)."""
        config.quietOut = not config.quietOut
        await ctx.send(f"Quiet output set to: {config.quietOut}")
        return
        
    @commands.command(name="collage")
    async def collagecmd(self, ctx):
        """Creates a collage of images from Imgur based on search terms."""
        if len(str(ctx.message.content).split(" ")) > 1:
            search_terms = str(ctx.message.content)[len(ctx.invoked_with)+2:].split(",")
            alisst = [term.replace(" ", "+") for term in search_terms if term.strip()]
            
            if not alisst:
                await ctx.send("Please provide search terms, separated by commas.")
                return

            await ctx.send("Creating collage, please wait...")
            DIR = os.path.join(config.HomeDir, "Saves", "ImageGeneration", f"{ctx.message.author.id}_temp")
            os.makedirs(DIR, exist_ok=True)
            
            try:
                image_path = await self.createCollage(ctx, alisst, DIR, numbered=True)
                await ctx.send(file=discord.File(image_path), content="")
            except Exception as e:
                await ctx.send(f"Failed to create collage: {e}")
                traceback.print_exc()
            
            # Clean up temp folder
            try:
                for f in os.listdir(DIR):
                    os.remove(os.path.join(DIR, f))
                os.rmdir(DIR)
            except Exception as e:
                print(f"Error cleaning up collage dir: {e}")
            return

    @commands.command(name="prefix")
    async def changeprefix(self, ctx):
        """Changes the command prefix for the current guild."""
        if not ctx.guild:
            await ctx.send("This command can only be used in a server.")
            return

        if ctx.message.author.guild_permissions.manage_roles or await self.bot.is_owner(ctx.message.author):
            try:
                prefix = str(str(ctx.message.content).split(" ")[1])
            except IndexError:
                await messageHandler(ctx=ctx, lines=["@#F Error: @#V Please provide a new prefix."], quietMode=2)
                return

            if not prefix:
                await messageHandler(ctx=ctx, lines=["@#F Error: @#V Prefix cannot be empty."], quietMode=2)
                return
            
            if len(prefix) > 5:
                 await messageHandler(ctx=ctx, lines=["@#F Error: @#V Prefix must be 5 characters or less."], quietMode=2)
                 return

            # Save to DB
            db.set_prefix(ctx.guild.id, prefix)
            
            # Update loaded serverData
            guild_found = False
            for i, each in enumerate(sm.serverData):
                if each[0] == str(ctx.guild.id):
                    sm.serverData[i] = [str(ctx.guild.id), prefix, None, None]
                    guild_found = True
                    break
            if not guild_found:
                sm.serverData.append([str(ctx.guild.id), prefix, None, None])

            await messageHandler(ctx=ctx, lines=[
                f"@#F Prefix Set: @#V {prefix} will now be used as this servers command prefix"], quietMode=2)
            
            try:
                await nameHandler(ctx=ctx, commandPrefix=prefix)
            except:
                pass
        else:
            await messageHandler(ctx=ctx,
                                 lines=[" @#F Permission Denied: @#V User must have **Manage Roles** permission."])
        return

    @commands.command(name="gt", aliases=["gentext", "text"])
    async def gentexrcmd(self, ctx):
        """Generates an image with text."""
        stringy, gentextAmount, font, arg3 = await commandSplitter(ctx=ctx, command="gt", cmdSelString="!@#")
        gentextAmount = int(gentextAmount)
        stringy = str(stringy)
        font = str(font.strip())
        await generateText(ctx=ctx, gentextAmount=gentextAmount,
                           stringSt=stringy, fontreq=font)
        return

    @commands.command(name="cls")
    @commands.is_owner()
    async def clscmd(self, ctx):
        """Clears the console (Owner only)."""
        os.system('cls' if os.name == 'nt' else 'clear')
        return

    @commands.command(name='help')
    async def help(self, ctx):
        """Displays the help message."""
        commandPrefix = await self.bot.get_prefix(ctx.message)
        
        help_part_1 = [
            f"@#F Commands: @#V .", f" @#F "
                                    f"{commandPrefix}Play / p: @#V \n Description: \n "
                                    f"  -   With URL/Query: Adds song and plays if idle.\n"
                                    f"  -   Without URL/Query: Resumes paused music or starts queue.\n"
                                    f"Syntax: {commandPrefix}p [string/Youtube URL/blank]",
            f" @#F {commandPrefix}Leave: @#V "
            f"Description: \n Leaves the voice channel and clears queue.",
            f" @#F {commandPrefix}Pause: @#V \n "
            f"Description: \n Pauses the currently playing audio.",
            f" @#F {commandPrefix}Next / n: @#V \n "
            f"Description: \n Plays the next song in the queue.",
            f" @#F {commandPrefix}prev: @#V \n "
            f"Description: \n Plays the previous song (disabled in shuffle).",
            f" @#F {commandPrefix}Shuffle: @#V \n "
            f"Description: \n Toggles shuffle mode on or off.",
            f" @#F {commandPrefix}Seek: @#V \n"
            f"Description: \n Seeks to time in currently playing audio. \n"
            f"Syntax: {commandPrefix}seek [MM:SS or HH:MM:SS]",
            f" @#F {commandPrefix}Skipto / skip: @#V \n "
            f"Description: \n Skips to a specific song number in the list. \n"
            f"Syntax: {commandPrefix}skipto [Song Number]",
            f" @#F {commandPrefix}Addlist: @#V \n "
            f"Description: \n Adds songs from a YouTube or Spotify playlist. \n"
            f"Syntax: {commandPrefix}addlist [youtube/spotify playlist URL]",
        ]
        
        help_part_2 = [
            f" @#F {commandPrefix}Add / a: @#V \n "
            f"Description: \n Adds a song to the queue without playing. \n"
            f"syntax: {commandPrefix}add [string/Youtube URL]",
            f" @#F {commandPrefix}Remove / r: @#V \n "
            f"Description: \n Removes item(s) by number from the list. \n"
            f"Syntax: {commandPrefix}remove [number or range (ie. 3, or 3-10)]",
            f" @#F {commandPrefix}List / q / queue: @#V \n "
            f"Description: Displays the currently playing list (paginated).",
            f" @#F {commandPrefix}Clear: @#V \n "
            f"Description: clears the currently playing list of all songs.",
            f" @#F {commandPrefix}Delsave: @#V \n "
            f"Description: \n Deletes a saved playlist. \n"
            f"Syntax: {commandPrefix}delsave [Playlist Number]",
            f" @#F {commandPrefix}Load: @#V \n "
            f"Description: \n Loads a saved playlist into the queue. \n"
            f"Syntax: {commandPrefix}load [Playlist Number]",
            f" @#F {commandPrefix}Save: @#V \n "
            f"Description: \n Saves the current list (max 5). \n"
            f"Syntax: {commandPrefix}save [PlaylistName (alphanumeric)]",
            f" @#F {commandPrefix}Prefix: @#V \n "
            f"Description: \n Changes the command prefix for this server. \n"
            f"Syntax: {commandPrefix}prefix [NewPrefix]",
            f" @#F {commandPrefix}quiet: @#V \n"
            f"Description: \n Toggles most bot messages on/off.",
            f" @#F {commandPrefix}Gentext / text / gt: @#V \n "
            f"Description: \n Generates text as an image.\n"
            f"Syntax: {commandPrefix}gt [Some Text]",
            f" @#F {commandPrefix}Tts: @#V \n "
            f"Description: \n Uses Text-to-Speech in the voice channel.\n"
            f"Syntax: {commandPrefix}tts [Some text to say]",
            f" @#F {commandPrefix}Button: @#V \n "
            f"Description: \n Spawns 'The Button'.",
            f" @#F {commandPrefix}Oauth: @#V \n "
            f"Description: \n Shows the bot's invite link.",
            f" @#F {commandPrefix}Collage: @#V \n "
            f"Description: \n Creates an image collage from search terms.\n"
            f"Syntax: {commandPrefix}collage [term1, term2, ...]",
            "\n @#F Enjoy :) @#V ~Serbz"
        ]
        
        # Split help message to avoid Discord limit
        await messageHandler(ctx=ctx, lines=help_part_1, quietMode=2)
        await asyncio.sleep(1) # Small delay
        await messageHandler(ctx=ctx, lines=help_part_2, quietMode=2)
        return

    # --- COLLAGE FUNCTIONS ---
    
    def scrapeWithSoup0(self, ctx, url):
        """Scrapes Imgur for collage images."""
        URL = url
        print(f"Scraping collage URL: {URL}")
        headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
        }
        try:
            data = requests.get(URL, timeout=15, headers=headers).text
        except Exception as e:
            print(f"Error fetching collage page: {e}")
            return []
            
        soup = BeautifulSoup(data, features="lxml")

        linksArray = []
        img_tags = soup.find_all('img')
        urls = [img['src'] for img in img_tags if 'src' in img.attrs]
        
        for url in urls:
            if str(url).startswith("//"):
                url = f"https:{url}"
            if "imgur.com" in str(url) and str(url).endswith(('.jpg', '.png', '.gif')):
                linksArray.append(url)
        return linksArray


    async def getSize(self, imageList, numbered=False):
        """Calculates size and numbers images for collage."""
        W = 0
        H = 0
        numimglist = []
        counter = 0
        newimglist = []
        fontlist = []
        fontprepath = os.path.join(config.HomeDir, "fonts")
        
        try:
            for filename in os.listdir(fontprepath):
                if filename.endswith(('.ttf', '.otf')):
                    fontlist.append(os.path.join(fontprepath, filename))
        except FileNotFoundError:
            pass # Handled below
                
        if not fontlist:
            print("Collage: No fonts found, numbering disabled.")
            numbered = False
            font = ImageFont.load_default()
        else:
            randomFontNumber = random.randint(0, len(fontlist) - 1)
            font = ImageFont.truetype(fontlist[randomFontNumber], 48)

        if not imageList:
            return 0, 0, [], []

        for image in imageList:
            counter += 1
            try:
                im = cv2.imread(image)
                if im is None: continue
            except Exception as e:
                print(f"Error reading image {image}: {e}")
                continue
                
            if numbered:
                num_image_path = image + "nonum.jpg"
                copyfile(image, num_image_path)
                numimglist.append([num_image_path, counter])
                
                cv2_im_rgb = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
                pil_im = Image.fromarray(cv2_im_rgb)
                draw = ImageDraw.Draw(pil_im)
                
                x, y = 10, 10
                # Draw outline
                draw.text((x-2, y-2), f"{counter}", font=font, fill=(0,0,0))
                draw.text((x+2, y-2), f"{counter}", font=font, fill=(0,0,0))
                draw.text((x-2, y+2), f"{counter}", font=font, fill=(0,0,0))
                draw.text((x+2, y+2), f"{counter}", font=font, fill=(0,0,0))
                # Draw text
                draw.text((x, y), f"{counter}", font=font, fill=(255,255,255))
                
                cv2_im_processed = cv2.cvtColor(numpy.array(pil_im), cv2.COLOR_RGB2BGR)
                cv2.imwrite(image, cv2_im_processed) # Overwrite original with numbered
            
            try:
                h, w, c = im.shape
                newimglist.append(image)
                W += w
                H += h
            except Exception as e:
                print(f"Error processing image shape {image}: {e}")

        if not newimglist:
             return 0, 0, [], []
             
        num_images = len(newimglist)
        grid_size = int(math.ceil(math.sqrt(num_images)))
        
        avg_W = W / num_images
        avg_H = H / num_images
        
        total_W = int(avg_W * grid_size)
        total_H = int(avg_H * grid_size)

        return total_W, total_H, newimglist, numimglist

    async def createCollage1(self, listofimages, DIR, numbered=False):
        """Arranges images into a collage."""
        width, height, listofimages, numimglist = await self.getSize(listofimages, numbered)
        
        if not listofimages:
            raise ValueError("No valid images found to create collage.")
            
        num_images = len(listofimages)
        rows = int(math.ceil(math.sqrt(num_images)))
        cols = rows
        
        if rows == 0 or cols == 0:
            raise ValueError("Cannot create a grid with 0 rows or cols.")

        thumbnail_width = width // cols
        thumbnail_height = height // rows
        size = (thumbnail_width, thumbnail_height)
        
        if thumbnail_width == 0 or thumbnail_height == 0:
            raise ValueError(f"Calculated thumbnail size is zero: {size}")

        new_im = Image.new('RGB', (width, height))
        i = 0
        x = 0
        y = 0
        
        for col in range(cols):
            for row in range(rows):
                if i < len(listofimages):
                    try:
                        im = Image.open(listofimages[i])
                        im.thumbnail(size) # Resize image to fit slot
                        new_im.paste(im, (x, y))
                        i += 1
                    except Exception as e:
                        print(f"Error pasting image {listofimages[i]}: {e}")
                        i += 1 # Skip broken image
                y += thumbnail_height
            x += thumbnail_width
            y = 0

        return new_im, numimglist

    async def createCollage(self, ctx, collageList, DIR, numbered=False, returnlist=False):
        """Main function to create a collage from search terms."""
        # Clean directory
        for filename in os.listdir(DIR):
            if "collage" not in filename:
                try:
                    os.remove(os.path.join(DIR, filename))
                except:
                    pass
                    
        linksArray = []
        for each in collageList:
            URL = f"https://imgur.com/search/score?q={each}" # Search by score
            linksArray.extend(self.scrapeWithSoup0(ctx, URL))
        
        # Get unique links
        linksArray = list(dict.fromkeys(linksArray))[:25] # Limit to 25 images
        
        if not linksArray:
            raise ValueError(f"No images found on Imgur for: {collageList}")
            
        img_paths = []
        for i, url in enumerate(linksArray):
            try:
                fn = posixpath.basename(urllib.parse.urlsplit(url).path)
                img_path = os.path.join(DIR, f"_Image_{i}{fn}")
                with open(img_path, "wb") as f:
                    r = requests.get(url, stream=True)
                    for block in r.iter_content(4096):
                        f.write(block)
                img_paths.append(img_path)
            except Exception as e:
                print(f"Error downloading image {url}: {e}")

        file, numimglist = await self.createCollage1(img_paths, DIR, numbered)
        
        path = os.path.join(DIR, f"collage_{random.randint(1000, 9999)}.png")
        file.save(path)

        if returnlist:
            return path, numimglist
        else:
            return path