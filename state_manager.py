import discord
from discord.ext import commands
import asyncio
import numpy
from typing import List
import time
import math
import os
from colorama import Fore, Style

# Import config for paths
import config

# --- BOT & LOOP ---
loop: asyncio.AbstractEventLoop = None
bots: List[commands.Bot] = []
musicBot: commands.Bot = None
buttons = None  # This will be set to the ButtonView instance in main.py
ahk = None  # AHK instance
serverData = [] # This will be populated by database_manager.get_all_prefixes() in main.py

# --- USER OBJECTS ---
Serbz = None
Bones = None
Serbz2 = None
SerbzChannel = None
SerbzChannel2 = None
BonesChannel = None

# --- MUTABLE STATE ARRAYS ---
megaArray = []
sysChannel = None # Will be fetched in on_ready
ready = 0
deleteinprogress = 0  # Global - should be array for per server - for delmsgs
botData = []  # Global for just statistic data for cloners
stopArray = []
counterArray = []  # these work
playingEpoch = []
yt2mp3Array = []
addListsActive = []
buttonmessages = [] # This is for the *old* button plugin, can likely be removed if new one is stable
botsNick = []
dumbFix = []
localVideoData = numpy.array([]) # This appears unused, but left for safety
list2array = [] # This holds pagination data for the /list command

# --- COUNTERS ---
counterButton = 0 # This will be loaded from file in main.py

# --- STATE MANAGEMENT FUNCTIONS ---

async def arrayBuilder(ctx,
                       audio=None, playingSongNum=None, voice_client=None, clip2=None, songList=None,
                       listArray=None, shuffle=None, videoDuration=None, video_title=None, isPlaying=None,
                       quietMode=None):
    """Builds or updates the megaArray entry for a specific guild."""
    global megaArray
    # Late import to avoid circular dependency
    from helper_utils import referenceDB, getVideoTitle 
    
    # Determine guild_id and author from ctx (can be Context or Interaction)
    guild_id = None
    author = None
    guild = None

    if isinstance(ctx, discord.Interaction):
        guild_id = ctx.guild_id
        guild = ctx.guild
        author = ctx.user
    elif hasattr(ctx, 'guild'):
        guild_id = ctx.guild.id
        guild = ctx.guild
        if hasattr(ctx, 'message'):
            author = ctx.message.author
    
    if guild_id is None:
        print("arrayBuilder: Could not determine guild ID from context.")
        return megaArray

    megaCounter = -1
    megaEntry = None
    for i, each in enumerate(megaArray):
        if each[0][0][0] == guild_id:
            megaCounter = i
            megaEntry = each
            break

    # --- Set defaults from existing entry or create new ---
    if megaEntry:
        guildID = megaEntry[0][0][0]
        voiceChannel = megaEntry[0][0][1]
        server = megaEntry[0][0][4]
        ctx_obj = megaEntry[0][0][5]
        
        if quietMode is None: # Only update quietMode if not passed
            quietMode = megaEntry[2]
        if videoDuration is None:
            videoDuration = megaEntry[0][7]
        if isPlaying is None:
            isPlaying = megaEntry[1]
        if voice_client is None:
            voice_client = megaEntry[0][0][3]
        if shuffle is None:
            shuffle = megaEntry[0][2]
        if listArray is None:
            listArray = megaEntry[0][1]
        if audio is None:
            audio = megaEntry[0][3]
        if playingSongNum is None:
            playingSongNum = megaEntry[0][4]
        if songList is None:
            songNumList = megaEntry[0][0][2]
        else:
            songNumList = songList # Overwrite with new list
        if clip2 is None:
            clip2 = megaEntry[0][5]
        if video_title is None:
             video_title = megaEntry[0][6]
             
    else:
        # --- Create new entry ---
        guildID = guild_id
        server = guild
        ctx_obj = ctx # Store the context/interaction
        voiceChannel = None
        if author and hasattr(author, 'voice') and author.voice:
            voiceChannel = author.voice.channel
            
        songNumList = []
        # listArray, shuffle, audio, playingSongNum, clip2, video_title, videoDuration, isPlaying, quietMode
        # are all set by passed args or remain None
    
    # --- Data Validation ---
    if videoDuration is None and clip2 is not None:
        # Don't await here, call it and let it run
        localVideoData = await referenceDB(clip2, None, None, "load")
        if localVideoData is not None:
            videoDuration = localVideoData[2]
            if video_title is None:
                video_title = localVideoData[1]
        else:
            # This is a network call, might be slow
            vt, vd = await getVideoTitle(clip2=clip2, returnB="notNone")
            if video_title is None:
                video_title = vt
            videoDuration = vd
            
    if not songNumList and clip2 is not None and video_title is not None:
        if videoDuration is None:
             vt, videoDuration = await getVideoTitle(clip2=clip2, returnB="notNone")
             if video_title is None: video_title = vt
        songNumList = [[str(clip2), 1, str(video_title), str(videoDuration)]]
    
    # --- Remove old entry and add new one ---
    if megaCounter > -1:
        megaArray.pop(megaCounter)
        
    megaArray.append(
        [[[guildID, voiceChannel, songNumList, voice_client, server, ctx_obj], 
          listArray, shuffle, audio, playingSongNum, clip2, video_title, videoDuration], 
         isPlaying, quietMode]
    )
    
    return megaArray


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
        
    for each in megaArray:
        if each[0][0][0] == guild_id:
            quietMode = each[2]
            break
    return quietMode


async def clearStopArray(guildID):
    """Removes all entries for a guildID from the stopArray."""
    global stopArray
    
    # Rebuild the list *without* the guildID
    stopArray = [item for item in stopArray if item != guildID]
    return stopArray


async def guildCountDown():
    """Background task to monitor voice channel activity and leave empty channels."""
    global counterArray, megaArray
    await asyncio.sleep(15) # Wait for bot to be ready
    
    while True:
        await asyncio.sleep(300)  # Check every 5 minutes
        if not config.timers:
            counterArray = [] # Clear timers if disabled
            continue

        guilds_to_remove = [] # Store guilds to remove
        
        for i, each in enumerate(megaArray):
            guildID = each[0][0][0]
            server = each[0][0][4]
            ctx = each[0][0][5]
            voice_client = each[0][0][3]
            voiceChannel = each[0][0][1]
            
            real_members = 0
            
            # Check if bot is connected
            if voice_client is not None and voice_client.is_connected():
                # Re-fetch the channel object in case bot was moved
                try:
                    current_vc = sm.musicBot.get_guild(guildID).voice_client
                    if current_vc:
                         voiceChannel = current_vc.channel
                         # Update the megaArray entry
                         each[0][0][1] = voiceChannel 
                    else:
                        # Bot is not in VC, but megaArray entry exists. Mark for removal.
                        print(f"{Fore.YELLOW}Stale VC entry for {server.name}. Marking for removal.{Style.RESET_ALL}")
                        guilds_to_remove.append(guildID)
                        continue
                except Exception as e:
                    print(f"Error checking VC status for {server.name}: {e}")
                    guilds_to_remove.append(guildID)
                    continue

                # Count non-bot members
                if voiceChannel:
                    for member in voiceChannel.members:
                        if not member.bot:
                            real_members += 1

            # --- Timer Logic ---
            if real_members <= 0:
                # --- Start or update timer ---
                timer_found = False
                for j, key in enumerate(counterArray):
                    if key[0] == guildID:
                        timeLeft = key[1] - 5 # Subtract 5 minutes
                        if timeLeft <= 0:
                            # --- Timer expired ---
                            print(f"{Fore.RED}Timer expired for {server.name}. Disconnecting.{Style.RESET_ALL}")
                            if voice_client is not None and voice_client.is_connected():
                                await voice_client.disconnect()
                            guilds_to_remove.append(guildID)
                            counterArray.pop(j)
                        else:
                            # Update timer
                            counterArray[j] = [guildID, timeLeft]
                        timer_found = True
                        break
                
                if not timer_found and guildID not in guilds_to_remove:
                    # Start a new timer (30 minutes)
                    print(f"{Fore.MAGENTA}Timer Started on megaArray ENTRY FOR {server.name}!!{Style.RESET_ALL}")
                    counterArray.append([guildID, 30])
            
            elif real_members > 0:
                # --- Members are present, remove any timer ---
                for j, key in enumerate(counterArray):
                    if key[0] == guildID:
                        counterArray.pop(j)
                        print(f"{Fore.LIGHTYELLOW_EX}TIMER REMOVED on megaArray ENTRY FOR {server.name}!! (Members present){Style.RESET_ALL}")
                        break

        # --- Cleanup ---
        if guilds_to_remove:
            # Rebuild megaArray, removing disconnected guilds
            megaArray = [entry for entry in megaArray if entry[0][0][0] not in guilds_to_remove]


async def backupCurrentServerData():
    """Saves the current state of megaArray to the DB."""
    # This is being replaced by a proper session manager in database_manager.py
    print("WARNING: backupCurrentServerData is deprecated. Use database_manager.save_session instead.")
    for each in megaArray:
        try:
            guild_id = each[0][0][0]
            # database_manager.save_session(guild_id, each) # This is the new way
        except Exception as e:
            print(f"Error during session save: {e}")
    return


async def loadCurrentServerData(bot):
    """Loads megaArray state from DB on startup."""
    # This is a complex task because discord objects are not serializable
    # and must be re-fetched by ID.
    print("Loading sessions from database...")
    from database_manager import load_session # Late import
    from pafy import new # Late import
    
    sessions = load_session(bot)
    if not sessions:
        print("No sessions found in database.")
        return

    global megaArray
    megaArray = []
    
    for guild_id_str, session_data in sessions.items():
        try:
            guild_id = int(guild_id_str)
            guild = bot.get_guild(guild_id)
            if not guild:
                print(f"Bot is no longer in guild {guild_id}, skipping session load.")
                continue

            # Reconstruct the megaArray entry
            # [[(0)guildID, (1)voiceChan, (2)songNumList, (3)voice_client, (4)server, (5)ctx], 
            #  (1)listArray, (2)shuffle, (3)audio, (4)playingSongNum, (5)clip2, (6)video_title, (7)videoDuration], 
            # (1)isPlaying, (2)quietMode]
            
            entry_data = session_data[0]
            
            # Fetch Discord objects
            vc_id = entry_data[0][1]
            voiceChannel = bot.get_channel(int(vc_id)) if vc_id else None
            
            ctx_id = entry_data[0][5] # This was a bad idea to save, we'll just use the guild
            
            # Rebuild
            new_entry = [
                [
                    [
                        guild_id, 
                        voiceChannel, 
                        entry_data[0][2], # songNumList
                        None, # voice_client (always None on start)
                        guild, # server
                        guild # Use guild as a fallback ctx
                    ],
                    entry_data[1], # listArray
                    entry_data[2], # shuffle
                    entry_data[3], # audio
                    entry_data[4], # playingSongNum
                    entry_data[5], # clip2
                    entry_data[6], # video_title
                    entry_data[7]  # videoDuration
                ],
                session_data[1], # isPlaying
                session_data[2]  # quietMode
            ]
            
            # If bot was playing, try to reconnect
            if new_entry[1] == 1 and voiceChannel is not None:
                try:
                    print(f"Reconnecting to {voiceChannel.name} in {guild.name}...")
                    vc = await voiceChannel.connect()
                    new_entry[0][0][3] = vc # Set voice_client
                    
                    # Need to re-instance the playing loop, this is complex
                    # For now, we'll just reconnect and let user type !play
                    new_entry[1] = 0 # Set isPlaying to false
                    
                except Exception as e:
                    print(f"Failed to reconnect to {voiceChannel.name}: {e}")
                    new_entry[0][0][1] = None # Clear VC
                    new_entry[1] = 0 # Set isPlaying to false

            megaArray.append(new_entry)
            print(f"Successfully loaded session for {guild.name}")

        except Exception as e:
            print(f"Error loading session for guild {guild_id_str}: {e}")
            traceback.print_exc()
            
    return