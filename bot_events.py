import discord
from discord.ext import commands
from discord.errors import Forbidden, HTTPException, NotFound
from discord.ext.commands import CommandNotFound
import traceback
import asyncio
from colorama import Fore, Style
import datetime
import os

# Import refactored files
import config
import state_manager as sm
from helper_utils import (
    messageHandler, nameHandler, getQuietMode, 
    printMessage
)
from state_manager import arrayBuilder

class BotEventsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        """Event handler for when the bot joins a new guild."""
        if config.musicbotDisable == 0 and not config.devMode:
            print(f"{Fore.RED}J{Fore.LIGHTWHITE_EX}O{Fore.LIGHTCYAN_EX}I{Fore.LIGHTMAGENTA_EX}N"
                  f"{Fore.LIGHTGREEN_EX}E{Fore.LIGHTBLUE_EX}D "
                  f"{Fore.LIGHTYELLOW_EX}G{Fore.LIGHTRED_EX}U{Fore.YELLOW}I{Fore.LIGHTWHITE_EX}"
                  f"L{Fore.LIGHTGREEN_EX}D{Fore.LIGHTYELLOW_EX}!{Fore.LIGHTGREEN_EX}! "
                  f"{Fore.RED}{guild.name}{Fore.LIGHTWHITE_EX}")
            await asyncio.sleep(2)
            for textChan in guild.text_channels:
                if "general" in str(textChan.name).lower() or "bot" in str(textChan.name).lower() \
                        or "commands" in str(textChan.name).lower():
                    try:
                        sm.loop.create_task(
                            messageHandler(ctx=textChan, lines=[f" @#F Hi! @#V My default command prefix is 1! \n"
                                                                f"You might want to change this!\n"
                                                                f"just simply use the 1!prefix command\n"
                                                                f"(ie. 1!prefix ! would change the prefix to !)\n"
                                                                f"please refer to 1!help if you like as well\n",
                                                                f" @#F Problems? Questions? @#V Feel free to add/message\n"
                                                                f"Serbz#0001 or Serbz#0002, any and all questions and feedback"
                                                                f"are welcome!\n enjoy."], quietMode=2))
                        break # Send to first valid channel
                    except Exception as e:
                        print(f"Error sending welcome message to {guild.name}: {e}")
        return

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        """Event handler for when the bot leaves a guild."""
        if config.musicbotDisable == 0 and not config.devMode and sm.ready == 1:
            print(f"{Fore.RED}L{Fore.LIGHTWHITE_EX}E{Fore.LIGHTCYAN_EX}F{Fore.LIGHTMAGENTA_EX}T "
                  f"{Fore.LIGHTYELLOW_EX}G{Fore.LIGHTRED_EX}U{Fore.YELLOW}I{Fore.LIGHTWHITE_EX}"
                  f"L{Fore.LIGHTGREEN_EX}D{Fore.LIGHTYELLOW_EX}!{Fore.LIGHTGREEN_EX}! "
                  f"{Fore.RED}{guild.name}{Fore.LIGHTWHITE_EX}")
        
        # Remove guild's data from state
        sm.megaArray = [entry for entry in sm.megaArray if entry[0][0][0] != guild.id]
        sm.counterArray = [entry for entry in sm.counterArray if entry[0] != guild.id]
        sm.list2array = [entry for entry in sm.list2array if entry[0] != guild.id]
        
        return

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        """Event handler for command errors."""
        # Late import to prevent circular dependency
        from music_cog import MusicCog 
        
        if config.musicbotDisable == 0:
            if isinstance(ctx.message.channel, discord.channel.DMChannel):
                return
            if isinstance(error, NotFound):
                return
                
            quietMode = await getQuietMode(ctx)
            
            if isinstance(error, CommandNotFound):
                if quietMode is None or quietMode == 2: # Only send if not in quiet mode
                    try:
                        prefix = '1!' # fallback
                        for each in sm.serverData:
                           if each[0] == str(ctx.guild.id):
                                prefix = each[1]
                                break
                    except:
                        prefix = '1!' # fallback
                    sm.loop.create_task(messageHandler(ctx=ctx,
                                                    lines=[" @#F Error: @#V command " + str(
                                                        str(ctx.message.content).split(" ")[0]) + \
                                                           f" not found.\nYou can change the command prefix if "
                                                           f"need be with {prefix}prefix [NewPrefixHere]"]))
                return
            if isinstance(error, (KeyError, UnboundLocalError)):
                print(f"Handled Error in {ctx.command}: {error}")
                return
                
            if isinstance(error, OSError):
                # Assuming 'next' is a function in MusicCog
                music_cog_instance = self.bot.get_cog("MusicCog")
                if music_cog_instance:
                    print(f"OSError caught in {ctx.command}, calling next().")
                    await music_cog_instance.next(ctx)
                return
            
            # Catch check failures (e.g., cog_check)
            if isinstance(error, commands.CheckFailure):
                print(f"CheckFailure: {ctx.author} failed check for {ctx.command}")
                return
            
            # Catch permission errors
            if isinstance(error, (commands.MissingPermissions, discord.errors.Forbidden)):
                print(f"Permissions Error in {ctx.command}: {error}")
                await messageHandler(ctx=ctx, lines=[f" @#F Error: @#V I don't have permission to do that."])
                return

            # Default error handler
            var2 = traceback.format_exc()
            print(f"Unhandled Error in command {ctx.command}:\n{var2}")
            sm.loop.create_task(messageHandler(ctx=ctx, lines=[" @#F Error: @#V " + \
                                                            f"```{config.formatString}\n" + str(error) + f"\n\n{var2}```"],
                                            system=1)) # Send full traceback to system channel
            await messageHandler(ctx=ctx, lines=[f" @#F Error: @#V An unexpected error occurred. The developer has been notified."])
            return

    @commands.Cog.listener()
    async def on_ready(self):
        """Event handler for when the bot is ready."""
        if sm.ready == 1:
            print("Already ready, skipping on_ready logic (reconnect).")
            return
            
        try:
            sm.sysChannel = await sm.musicBot.fetch_channel(config.sysChannelID)
        except Exception as e:
            print(f"CRITICAL: Could not fetch sysChannel (ID: {config.sysChannelID}). Error: {e}")
            sm.sysChannel = None # Set to None so system messages don't crash
        
        # Fetch user/channel objects
        try:
            sm.Bones = await self.bot.fetch_user(210914635136630784)
            sm.BonesChannel = await sm.Bones.create_dm()
        except Exception as e:
            print(f"Failed to fetch Bones user/DM: {e}")

        try:
            sm.Serbz = await self.bot.fetch_user(246892047284436992)
            sm.SerbzChannel = await sm.Serbz.create_dm()
        except Exception as e:
            print(f"Failed to fetch Serbz user/DM: {e}")

        try:
            sm.Serbz2 = await self.bot.fetch_user(210914635136630784) # Note: This ID is same as Bones
            sm.SerbzChannel2 = await sm.Serbz2.create_dm()
        except Exception as e:
            print(f"Failed to fetch Serbz2 user/DM: {e}")

        
        print(f"{sm.musicBot.user.id} || {sm.musicBot.user.name}#{sm.musicBot.user.discriminator} is ready.")
        sm.ready = 1
        
        if sm.sysChannel:
            await messageHandler(ctx=sm.sysChannel, lines=[f" @#F Ready: @#V {str(sm.musicBot.user)}"])
        
        await nameHandler(None, clear=1) # Set all guild names
        
        return

    @commands.Cog.listener()
    async def on_message(self, message):
        """Event handler for incoming messages."""
        if sm.ready == 0 or config.musicbotDisable == 1 or message.author.bot:
            return
            
        # Forward mentions to Serbz
        if ("serbz" in message.content.lower() or "246892047284436992" in message.content or "210914635136630784" in message.content):
            if sm.SerbzChannel and not isinstance(message.channel, discord.DMChannel):
                try:
                    await sm.SerbzChannel.send(
                        f"\n.\n{message.author.name}#{message.author.discriminator} - {message.author.id}" + \
                        f"\n{message.channel.guild.name} - {message.channel.name}```{message.content}```")
                except Exception as e:
                    print(f"Failed to send mention DM to Serbz: {e}")

        # Handle DM messages
        if isinstance(message.channel, discord.DMChannel):
            if message.author.id == 246892047284436992: # Serbz ID
                prefix = "?"
                if config.devMode:
                    prefix = ">?"
                
                if str(message.content.lower()).startswith(prefix):
                    # Process DM commands
                    ctx = await self.bot.get_context(message)
                    if ctx.command:
                        await self.bot.invoke(ctx)
                        
            print(f"{Style.RESET_ALL}{Fore.YELLOW}" + str(message.author.name) + " DIRECT MESSAGED: " + str(
                message.content))
            return

        # --- Guild Message Logic ---

        # Sneks logic (image saving)
        if not config.devMode and (message.channel.guild.id in [859964575310282763, 856922937541394482]):
            loadedPotatoes = config.HomeDir + f"/Saves/Sneks/{message.channel.guild.name}-{message.channel.guild.id}/"
            os.makedirs(loadedPotatoes, exist_ok=True) # Ensure dir exists
            
            for attachment in message.attachments:
                image_types = ["png", "jpeg", "gif", "jpg", "mp4", "webm"]
                if any(attachment.filename.lower().endswith(ext) for ext in image_types):
                    filename2 = fr"{attachment.filename.lower()}"
                    await attachment.save(os.path.join(loadedPotatoes, filename2))
                    contX = message.author.name + "#" + message.author.discriminator + "\n" \
                            + str(message.author.id) + "\n\n>" + message.content + f"\n\n"
                    try:
                        if sm.SerbzChannel:
                            await sm.SerbzChannel.send(file=discord.File(os.path.join(loadedPotatoes, filename2)),
                                                    content=contX + f"{message.jump_url}")
                        if sm.BonesChannel:
                            await sm.BonesChannel.send(file=discord.File(os.path.join(loadedPotatoes, filename2)), content=contX+f"{message.jump_url}")
                    except HTTPException:
                        pass
                    print(
                        f"{Style.RESET_ALL}{Fore.LIGHTMAGENTA_EX}Sneky{Fore.RED} SNEKS! {filename2}")
            
            if "http" in message.content and "discord" in message.content:
                if sm.SerbzChannel:
                    await sm.SerbzChannel.send(f"{message.author.name}#{message.author.discriminator}\n{message.author.id}"
                                        f"\n\n >{message.content} \n\n {message.jump_url}")
                if sm.BonesChannel:
                    await sm.BonesChannel.send(f"{message.content} \n\n {message.jump_url}")
                print(f"{Style.RESET_ALL}{Fore.LIGHTMAGENTA_EX}Sneky{Fore.RED} SNEKS! (Discord Attachment Link)")
                # Do not return, allow commands to process

        # Print message to console
        if (str(message.content) != "" and not config.quietOut) and not config.devMode:
            sm.loop.create_task(printMessage(message))

        # --- Process Commands (FIXED: Removed manual process_commands call) ---
        prefix = await self.bot.get_prefix(message)
        
        # Check for bad prefix (e.g., "! play")
        if str(message.content).startswith(prefix + " "):
            if len(message.content) > len(str(prefix + " ")):
                string2 = f"try {prefix}{str(message.content)[len(prefix) + 1:]}"
            else:
                string2 = "Check your command."
            await messageHandler(ctx=message.channel, lines=[
                f" @#F Command error: @#V There should never be a space after the command prefix. \n\n"
                f"{string2}"])
            return
        
        # Check if it's a command
        if str(message.content).startswith(prefix):
            if prefix == '':
                return
            
            # Check for content after prefix
            if len(message.content.strip()) <= len(prefix):
                return

            # Log command
            messageContent = str(message.content).lower()
            stringFuck = f"{Style.RESET_ALL}{Fore.LIGHTMAGENTA_EX}Command: " + \
            f"{Style.RESET_ALL}{Fore.LIGHTWHITE_EX}{str(messageContent).split(r' ')[0]}" + \
            f" {Style.RESET_ALL}{Fore.LIGHTYELLOW_EX}Used by: " + \
            f"{Style.RESET_ALL}{Fore.LIGHTWHITE_EX}{message.author.name}"         
            print(stringFuck)
            
            # FIXED: Do NOT call await self.bot.process_commands(message) here.
            # It is already called by the default on_message handler in the bot instance.

        return