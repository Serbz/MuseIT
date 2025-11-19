import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
from discord.errors import Forbidden
import asyncio
import os
import sys
import numpy 
import random
import math
import time
import re
import urllib
import traceback
from yt_dlp import YoutubeDL, DownloadError
from vocodes_api import VocodesAPI
import spotipy
import spotipy.oauth2 as oauth2
from googleapiclient.discovery import build
from urllib.parse import parse_qs, urlparse
from colorama import Fore, Style

# Import new discord.ui components
from discord.ui import View, Button
from discord import ButtonStyle

# Import refactored files
import config
import state_manager as sm
import database_manager as db
from helper_utils import (
    messageHandler, nameHandler, getQuietMode, 
    getChannel, getVoice, getClip, getVideoTitle, lessOrMore,
    referenceDB, similar, commandSplitter
)
from state_manager import arrayBuilder

# -----------------------------------------------------------------
# View Classes (Music Specific)
# -----------------------------------------------------------------

class ListView(View):
    """A view for the paginated list command."""
    def __init__(self, music_cog_instance, current_page: int, total_pages: int, timeout=180):
        super().__init__(timeout=timeout)
        self.music_cog = music_cog_instance
        self.current_page = current_page

        # Add/disable buttons based on page
        prev_button = Button(label="← Prev", style=ButtonStyle.grey, custom_id="list2prev", disabled=(current_page == 0))
        next_button = Button(label="Next →", style=ButtonStyle.grey, custom_id="list2next", disabled=(current_page >= total_pages))

        prev_button.callback = self.prev_callback
        next_button.callback = self.next_callback
        
        self.add_item(prev_button)
        self.add_item(next_button)

    async def prev_callback(self, interaction: discord.Interaction):
        await interaction.response.defer() # Acknowledge click
        await self.music_cog.list2cmd(ctx=interaction, page=-1, msg=interaction.message)

    async def next_callback(self, interaction: discord.Interaction):
        await interaction.response.defer() # Acknowledge click
        await self.music_cog.list2cmd(ctx=interaction, page=+1, msg=interaction.message)


# -----------------------------------------------------------------
# Music Cog
# -----------------------------------------------------------------

class MusicCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.tts_api = VocodesAPI()

    async def cog_check(self, ctx):
        # Disable all commands if musicbotDisable is on
        return config.musicbotDisable == 0

    async def bal_error(self, ctx, error):
        """Error handler for bal command (if it's part of this cog)"""
        if isinstance(error, discord.errors.NotFound):
            return
        else:
            raise error

    # --- HELPER FOR AUDIO EXTRACTION ---
    async def get_audio_url(self, clip_url):
        """Extracts the best audio URL using yt-dlp directly."""
        # Use settings from config to maintain silence
        ydl_opts = {
            'format': 'bestaudio/best',
            'quiet': True,
            'noplaylist': True,
            'geo_bypass': True,
            'logger': config.YTDLLogger(), # Use the silencer
            'extractor_args': config.ydl_opts.get('extractor_args', {})
        }
        try:
            with YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(clip_url, download=False)
                return info['url']
        except Exception as e:
            print(f"Error extracting audio from {clip_url}: {e}")
            return None

    # --- MUSIC COMMANDS ---

    @commands.command(name="n")
    async def next3(self, ctx):
        """Alias for 'next' command."""
        sm.loop.create_task(self.next(ctx))
        return

    @commands.command(name="r")
    async def remove22(self, ctx):
        """Alias for 'remove' command."""
        sm.loop.create_task(self.remove(ctx))
        return

    @commands.command(name="p")
    async def shorthandplay_p(self, ctx):
        """Alias for 'play' command."""
        await self.play2(ctx)
        return

    @commands.command(name='add')
    async def add(self, ctx):
        """Adds a song to the queue without playing."""
        sm.loop.create_task(self.add2(ctx, nosend="NotNaN"))
        return

    @commands.command(name="stop")
    async def stopfuck(self, ctx):
        """Stops playing and leaves the voice channel."""
        await self.stopplaying(ctx, nosend="notNaN")
        await self.leave(ctx)
        return

    @commands.command(name="skip")
    async def skipfuck(self, ctx):
        """Skips to the next song or a specific song number."""
        if len((ctx.message.content).split(" ")) <= 1:
            sm.loop.create_task(self.next(ctx))
        else:
            sm.loop.create_task(self.skipto(ctx))
        return

    @commands.command(name="np", aliases=["playing", "nowplaying"])
    async def nowplayingfuck(self, ctx):
        """Displays the currently playing song."""
        video_title = None
        songDuration = None
        clip2 = None
        songNumber = None

        for each in sm.megaArray:
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
                        video_title, songDuration = await getVideoTitle(clip2=clip2, returnB="notNone")
                break
        
        if not video_title:
             await messageHandler(ctx=ctx, lines=[" @#F Error: @#V Nothing is playing."])
             return

        if songNumber is not None:
            stringy = str(songNumber)
        else:
            stringy = ""
            
        commandPrefix = await self.bot.get_prefix(ctx.message)
        
        try:
            songDuration = int(songDuration)
            duration_str = (
                f"{str(lessOrMore(int(math.floor(float(int(songDuration) / 60)))))}:"
                f"{str(lessOrMore(int(songDuration % 60)))}"
            )
        except:
            songDuration = 0
            duration_str = "00:00"
            pass
            
        sm.loop.create_task(messageHandler(ctx=ctx, lines=[
            " @#F Now Playing: " +
            f" @#V {stringy}. - [" + str(video_title) + f"]({clip2})",
            f" @#F Duration: @#V {duration_str}"
            f" ({commandPrefix}seek 00:00-{duration_str})"
        ]))
        return

    @commands.command(name="a")
    async def shorthandadd2_q(self, ctx):
        """Alias for 'add' command."""
        sm.loop.create_task(self.add2(ctx))
        return

    @commands.command(name='leave')
    async def leave(self, ctx, nosend="NaN"):
        """Disconnects the bot from the voice channel."""
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
                
        sm.loop.create_task(self.stopplaying(ctx, nosend="no"))
        sm.loop.create_task(arrayBuilder(ctx, isPlaying=0, songList=[], clip2=None, audio=None)) # Clear queue
        
        if voice is not None and voice.is_connected():
            await voice.disconnect()
        
        # Remove from megaArray
        sm.megaArray = [entry for entry in sm.megaArray if entry[0][0][0] != ctx.guild.id]
        return

    @commands.command(name='pause')
    async def stopplaying(self, ctx, nosend="NaN"):
        """Pauses the currently playing audio."""
        server = ctx.message.guild
        voice = None
        for each in sm.megaArray:
            if each[0][0][0] == server.id:
                voice = each[0][0][3]
                break
                
        if voice is not None and voice.is_playing():
            voice.pause()
            
        sm.loop.create_task(arrayBuilder(ctx, isPlaying=0))
        
        if nosend == "NaN":
            commandPrefix = await self.bot.get_prefix(ctx.message)
            sm.loop.create_task(messageHandler(ctx=ctx, lines=[
                f"@#F Audio Paused: @#V play with {commandPrefix}play or clear the list with {commandPrefix}clear"]))
        return

    @commands.command(name="seek")
    async def seek(self, ctx):
        """Seeks to a specific timestamp in the current song."""
        try:
            msgSpl = str(str(ctx.message.content).split(" ")[1]).split(":")
            offset = 0
            if len(msgSpl) > 2:
                hour = int(msgSpl[0])
                offset = 1
                minute = int(msgSpl[1])
                second = int(msgSpl[2])
            else:
                hour = 0
                minute = int(msgSpl[0])
                second = int(msgSpl[1])
            
            total_seconds = (hour * 3600) + (minute * 60) + second
            seek_time_str = f"{hour:02d}:{minute:02d}:{second:02d}"

        except (TypeError, AttributeError, IndexError, NameError, ValueError) as e:
            commandPrefix = await self.bot.get_prefix(ctx.message)
            sm.loop.create_task(messageHandler(ctx=ctx,
                                            lines=[f"@#F Error: @#V Correct usage is: {commandPrefix}seek HH:MM:SS or "
                                                   f"MM:SS where HH, MM, and SS represent double digit integer values (ie. {commandPrefix}seek 00:48 "
                                                   f"would seek the currently playing or queued to play audio source to 48 seconds."],
                                            quietMode=2))
            return

        found = False
        for each in sm.megaArray:
            if each[0][0][0] == ctx.guild.id:
                voiceChannel = each[0][0][1]
                voice_client = each[0][0][3]
                
                if voice_client is None or not voice_client.is_connected():
                    await messageHandler(ctx=ctx, lines=[f"@#F Error: @#V Bot is not in a voice channel."])
                    return
                        
                playingSongNum = each[0][4]
                audio = each[0][3]
                clip2 = each[0][5]
                songDuration = each[0][7]
                video_title = each[0][6]
                
                if video_title is None:
                    video_title, songDuration = await getVideoTitle(clip2, returnB="notNone")
                
                # Check if seek time is valid
                if songDuration and total_seconds > int(songDuration):
                     await messageHandler(ctx=ctx, lines=[f"@#F Error: @#V Seek time ({seek_time_str}) is longer than the song duration."])
                     return
                
                try:
                    voice_client.pause()
                except:
                    pass
                    
                seekffmpeg_opts = {
                    'before_options': f'-ss {seek_time_str}.00 -reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
                    'options': '-vn'}
                    
                sm.stopArray.append(ctx.guild.id)
                await asyncio.sleep(1)
                
                sm.loop.create_task(self.playingLoop(ctx, voice_client, ctx.guild, config.ProjectFFMPEG, audio,
                                             clip2, video_title, playingSongNum, songDuration, skipMessage="notNone",
                                             ffmpeg_opts=seekffmpeg_opts))
                
                await sm.clearStopArray(ctx.guild.id)
                
                sm.loop.create_task(messageHandler(ctx=ctx, lines=[
                    f"@#F Seeking: @#V Skipped to: timestamp {seek_time_str} for currently playing audio source"]))
                found = True
                break
                
        if not found:
            sm.loop.create_task(messageHandler(ctx=ctx, lines=[
                f"@#F Error: @#V Nothing is currently playing."]))
        return

    @commands.command(name="skipto")
    async def skipto(self, ctx, lotus=-1, direct=None):
        """Skips to a specific song number in the queue."""
        if ctx.guild.id in sm.stopArray and direct is None:
            return
            
        sm.stopArray.append(ctx.guild.id)
        
        clip2 = None
        video_title = None
        songDuration = None
        songNumber = None

        if direct is None:
            try:
                songNumber = int(str(ctx.message.content).split(" ")[1])
            except (IndexError, ValueError):
                commandPrefix = await self.bot.get_prefix(ctx.message)
                await messageHandler(ctx=ctx, lines=[f" @#F Error: @#V You must specify a song "
                                                     f"number to skip to\nRefer to {commandPrefix}list for a song number to skip to."],
                                     quietMode=2)
                await sm.clearStopArray(ctx.guild.id)
                return

            megaEntry = next((each for each in sm.megaArray if each[0][0][0] == ctx.message.guild.id), None)
            
            if megaEntry is None:
                await ctx.send("There is nothing to skip to.")
                await sm.clearStopArray(ctx.guild.id)
                return

            songNumList = megaEntry[0][0][2]
            voice_client = megaEntry[0][0][3]
            server = megaEntry[0][0][4]

            if not songNumList:
                await ctx.send("The playlist is empty.")
                await sm.clearStopArray(ctx.guild.id)
                return
            
            song_to_play = next((song for song in songNumList if song[1] == songNumber), None)

            if song_to_play is None:
                await messageHandler(ctx=ctx, lines=[
                    f" @#F Error: @#V There are not that many songs on the play list.\n there are " + str(
                        len(songNumList)) + " entries in the current playlist"], quietMode=2)
                await sm.clearStopArray(ctx.guild.id)
                return
                
            clip2, video_title, songDuration = song_to_play[0], song_to_play[2], song_to_play[3]

        else: # direct call
            clip2, video_title, songDuration, songNumber = direct[0], direct[1], direct[2], direct[3]
            megaEntry = next((each for each in sm.megaArray if each[0][0][0] == ctx.guild.id), None)
            voice_client = megaEntry[0][0][3] if megaEntry else None
            server = megaEntry[0][0][4] if megaEntry else ctx.guild


        if clip2:
            audio = await self.get_audio_url(clip2)
            
            if not audio:
                await messageHandler(ctx=ctx, lines=[
                    f" @#F Error: @#V Unsure why, but this video seems unavailable. :("])
                await sm.clearStopArray(ctx.guild.id)
                await self.next(ctx)
                return
            
            if voice_client is None:
                channel = await getChannel(ctx)
                if not channel:
                    await messageHandler(ctx=ctx, lines=[f"@#F Error: @#V You must be in a voice channel to use this command."])
                    await sm.clearStopArray(ctx.guild.id)
                    return
                voice_client = await getVoice(ctx, channel)

            await arrayBuilder(ctx, voice_client=voice_client, audio=audio, playingSongNum=songNumber,
                               videoDuration=songDuration, clip2=clip2, video_title=video_title)
            
            await sm.clearStopArray(ctx.guild.id)
            
            await self.playingLoop(ctx, voice_client, server, config.ProjectFFMPEG, audio, clip2, video_title, songNumber,
                              songDuration, skipMessage=None)
        return

    @commands.command(name="m4a", aliases=["mp3", "download", "dl"])
    async def yt2mp3(self, ctx):
        """Downloads a YouTube video as an M4A/MP3 file."""
        if ctx.guild.id in sm.yt2mp3Array:
            await messageHandler(ctx=ctx, lines=[
                " @#F Error: @#V Only one of these commands can run per server. \n Please wait."])
            return
            
        sm.yt2mp3Array.append(ctx.guild.id)
        
        clipStr = " ".join(ctx.message.content.split(" ")[1:])
        video_title1 = None
        clip2 = None

        if "http" in clipStr.lower() and "youtube.com" in clipStr.lower() and "://" in clipStr.lower():
            if "watch?v=" in clipStr:
                clipStr2 = clipStr.split("watch?v=")
                if len(clipStr2) > 1:
                    f_clip = "http://www.youtube.com/watch?v=" + clipStr2[1][:11]
                    video_title1, video_duration = await getVideoTitle(clip2=f_clip, returnB="notNone")
                    clip2 = f_clip
        
        if clip2 is None:
            if not clipStr:
                await messageHandler(ctx=ctx, lines=[f" @#F Error: @#V Please provide a search term or YouTube URL."])
                sm.yt2mp3Array.remove(ctx.guild.id)
                return
            music_name = clipStr
            query_string = urllib.parse.urlencode({"search_query": music_name})
            try:
                with urllib.request.urlopen("https://www.youtube.com/results?" + query_string) as formatUrl:
                    search_results = re.findall(r"watch\?v=(\S{11})", formatUrl.read().decode())
                if search_results:
                    clip2 = "https://www.youtube.com/watch?v=" + "{}".format(search_results[0])
                else:
                    await messageHandler(ctx=ctx, lines=[f" @#F Error: @#V Could not find any video for '{clipStr}'."])
                    sm.yt2mp3Array.remove(ctx.guild.id)
                    return
            except Exception as e:
                await messageHandler(ctx=ctx, lines=[f" @#F Error: @#V YouTube search failed: {e}"])
                sm.yt2mp3Array.remove(ctx.guild.id)
                return

        author_dir = f'{config.HomeDir}/Saves/YTMP3/{ctx.message.author.id}'
        os.makedirs(author_dir, exist_ok=True)

        try:
            # Use updated logger settings
            ytdl_download_opts = {
                'format': 'bestaudio[ext=m4a]/bestaudio',
                'outtmpl': f'{author_dir}/%(title)s.%(ext)s',
                'noplaylist': True,
                'writethumbnail': True,
                'quiet': True,
                'no_warnings': True,
                'logger': config.YTDLLogger(), # Suppress warnings
                'extractor_args': config.ydl_opts.get('extractor_args', {})
            }
            
            with YoutubeDL(ytdl_download_opts) as ydl:
                info_dict = ydl.extract_info(clip2, download=True)
                video_title1 = info_dict.get('title', 'Unknown Title')
                ext = info_dict.get('ext', 'm4a')
                # Sanitize title for file path
                safe_title = re.sub(r'[\\/*?:"<>|]', "", video_title1)
                file_path = f'{author_dir}/{safe_title}.{ext}'
                
                # Find thumbnail
                thumb_path_jpg = f'{author_dir}/{safe_title}.jpg'
                thumb_path_webp = f'{author_dir}/{safe_title}.webp'
                
                image_path = None
                if os.path.exists(thumb_path_jpg):
                    image_path = thumb_path_jpg
                elif os.path.exists(thumb_path_webp):
                    image_path = thumb_path_webp

            if os.path.exists(file_path):
                await messageHandler(ctx=ctx, lines=[f" @#F Complete! @#V ** {video_title1} **\n"],
                                     image=image_path, file=discord.File(file_path))
            else:
                await messageHandler(ctx=ctx, lines=[f" @#F Error: @#V Downloaded file not found."])

        except Exception as e:
            print(traceback.format_exc())
            await messageHandler(ctx=ctx, lines=[f" @#F Error: @#V Download failed. \n```{e}```"])
        
        finally:
            if ctx.guild.id in sm.yt2mp3Array:
                sm.yt2mp3Array.remove(ctx.guild.id)
        return

    @commands.command(name='list', aliases=["q", "queue"])
    async def list2list(self, ctx):
        """Displays the song queue in a paginated way."""
        # This command just starts the list process
        await self.list2cmd(ctx, page=0, msg=None)
        return

    @commands.command(name='shuffle')
    async def shuffle(self, ctx):
        """Toggles shuffle mode for the queue."""
        shuffle = "unset"
        for each in sm.megaArray:
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
            
        commandPrefix = await self.bot.get_prefix(ctx.message)
        await nameHandler(ctx=ctx, commandPrefix=commandPrefix)
        return

    @commands.command(name='save')
    async def save(self, ctx):
        """Saves the current queue as a playlist."""
        commandPrefix = await self.bot.get_prefix(ctx.message)
        try:
            playListName = str(ctx.message.content.split(" ")[1]).lower()
        except IndexError:
            await messageHandler(ctx=ctx, lines=[
                f"@#F Error! @#V Please specify a playlist name. \n ({commandPrefix}save PlayListName)"],
                                 quietMode=2)
            return

        user_playlists = db.get_user_playlists(ctx.message.author.id)
        
        if len(user_playlists) >= 5:
            await messageHandler(ctx=ctx, lines=[
                f"@#F Error! @#V You have too many saves already (Max 5). \n Use {commandPrefix}delsave to remove one."], quietMode=2)
            return
        
        if len(playListName) > 25 or not playListName.isalnum():
            await messageHandler(ctx=ctx,
                                 lines=[f"@#F Error! @#V Playlist name must be 1-25 characters and alphanumeric."], quietMode=2)
            return

        songNumList = []
        for each in sm.megaArray:
            if each[0][0][0] == ctx.guild.id:
                songNumList = each[0][0][2]
                break
                
        if songNumList:
            success = db.save_playlist(ctx.message.author.id, playListName, songNumList)
            if success:
                await messageHandler(ctx=ctx,
                                     lines=["@#F Saved! @#V Playlist **" + str(playListName) + "** is now saved.",
                                            "@#F ----- @#V " +
                                            str(len(songNumList)) + " songs in the playlist."], quietMode=2)
            else:
                await messageHandler(ctx=ctx, lines=[f"@#F Error: @#V A playlist named '{playListName}' already exists."], quietMode=2)
        else:
            await messageHandler(ctx=ctx, lines=["@#F Error: @#V There is nothing to save."], quietMode=2)
        return

    @commands.command(name="delsave")
    async def delsave(self, ctx):
        """Deletes a saved playlist."""
        commandPrefix = await self.bot.get_prefix(ctx.message)
        user_playlists = db.get_user_playlists(ctx.message.author.id)
        
        if not user_playlists:
            await messageHandler(ctx=ctx, lines=[f" @#F Error: @#V You have no saved playlists."], quietMode=2)
            return
            
        try:
            playListNumber = int(str(ctx.message.content.split(" ")[1]))
        except (IndexError, ValueError):
            loadStr = ""
            for i, name in enumerate(user_playlists):
                loadStr += f"\n-- II {i + 1}. {name}"
            await messageHandler(ctx=ctx,
                                 lines=["@#F Playlists Available: " +
                                        "@#V ```yaml\n" + str(loadStr) + "``` ",
                                        "@#F You can use: " + f" @#V {commandPrefix}delsave [Number] for this command."], quietMode=2)
            return

        if 1 <= playListNumber <= len(user_playlists):
            playlist_to_delete = user_playlists[playListNumber - 1]
            success = db.delete_playlist(ctx.message.author.id, playlist_to_delete)
            if success:
                await messageHandler(ctx=ctx,
                                     lines=[f" @#F Playlist Removed: @#V Playlist **{playlist_to_delete}** has been deleted."])
            else:
                await messageHandler(ctx=ctx, lines=[f" @#F Error: @#V Could not delete playlist."])
        else:
            await messageHandler(ctx=ctx, lines=[f" @#F Error: @#V Invalid playlist number."])
        return

    @commands.command(name='load')
    async def load(self, ctx):
        """Loads a saved playlist into the queue."""
        commandPrefix = await self.bot.get_prefix(ctx.message)
        user_playlists = db.get_user_playlists(ctx.message.author.id)
        
        if not user_playlists:
            # Check for legacy .npy files
            legacy_playlists = []
            SaveDir = os.path.join(config.HomeDir, "Saves", str(ctx.message.author.id))
            if os.path.exists(SaveDir):
                legacy_playlists = [f for f in os.listdir(SaveDir) if f.endswith('.npy') and f.startswith('Playlist.')]
            
            if not legacy_playlists:
                await messageHandler(ctx=ctx, lines=[f" @#F Error: @#V You have no saved playlists."], quietMode=2)
                return
            else:
                # Found legacy files, instruct user to load them one by one
                await messageHandler(ctx=ctx, lines=[f" @#F Info: @#V Found legacy playlists. Please use `{commandPrefix}load [Number]` to migrate them to the new database."])

        try:
            playListNumber = int(str(ctx.message.content.split(" ")[1]))
        except (IndexError, ValueError):
            loadStr = ""
            for i, name in enumerate(user_playlists):
                loadStr += f"\n-- II {i + 1}. {name}"
            
            # Add legacy playlists to list
            legacy_load_str = ""
            if 'legacy_playlists' in locals() and legacy_playlists:
                 for i, name in enumerate(legacy_playlists):
                    legacy_load_str += f"\n-- II {len(user_playlists) + i + 1}. {name.split('.')[1]} (Legacy)"
            
            await messageHandler(ctx=ctx,
                                 lines=["@#F Playlists Available: @#V ```" + loadStr + legacy_load_str + "```",
                                        "@#F You can use:"
                                        f" @#V {commandPrefix}load [Number] for this command."], quietMode=2)
            return
            
        playLists = None
        saveName = ""
        
        # Try loading from new DB
        if 1 <= playListNumber <= len(user_playlists):
            saveName = user_playlists[playListNumber - 1]
            playLists = db.load_playlist(ctx.message.author.id, saveName)
        
        # Try loading from legacy .npy
        elif 'legacy_playlists' in locals() and 1 <= (playListNumber - len(user_playlists)) <= len(legacy_playlists):
            legacy_index = playListNumber - len(user_playlists) - 1
            legacy_file = legacy_playlists[legacy_index]
            saveName = legacy_file.split('.')[1]
            legacy_path = os.path.join(config.HomeDir, "Saves", str(ctx.message.author.id), legacy_file)
            
            print(f"Loading legacy .npy playlist: {legacy_path}")
            playLists = numpy.load(legacy_path, allow_pickle=True).tolist()
            # Save it to the new DB format
            if not db.save_playlist(ctx.message.author.id, saveName, playLists):
                 # Playlist name collision, add (migrated)
                 saveName = f"{saveName}_migrated"
                 db.save_playlist(ctx.message.author.id, saveName, playLists)
            # Delete old .npy file
            os.remove(legacy_path)
            
        else:
             await messageHandler(ctx=ctx, lines=[f" @#F Error: @#V Invalid playlist number."])
             return

        if playLists is None:
            await messageHandler(ctx=ctx, lines=[f" @#F Error: @#V Could not load playlist data for {saveName}."])
            return

        # Check if playlist needs rebuilding (old format)
        if len(playLists) > 0 and len(playLists[0]) < 4:
            print(f"{Style.RESET_ALL}{Fore.RED}REBUILDING PLAYLIST {saveName} FOR USER "
                  f"{ctx.message.author}-{ctx.message.author.id}{Fore.LIGHTWHITE_EX}")
            playLists = await self.rebuildPlaylist(ctx=ctx, listT=playLists)
            # Re-save the rebuilt list
            db.delete_playlist(ctx.message.author.id, saveName) # Delete old
            db.save_playlist(ctx.message.author.id, saveName, playLists) # Save new

        current_songList = []
        for each in sm.megaArray:
            if each[0][0][0] == ctx.guild.id:
                current_songList = each[0][0][2]
                break
        
        start_index = len(current_songList)
        
        for i, each in enumerate(playLists):
            await self.add2(ctx, f_clip=each[0], f_title=each[2], video_duration=each[3], 
                            SongNumber=start_index + 1 + i, nosend="NaN", addlistcmd="notnone", noLinkCheck=1)

        await messageHandler(ctx=ctx, lines=[
            f"@#F Success: @#V Added {str(len(playLists))} songs to the playlist from **{saveName}**"], quietMode=2)
        print(f"{Style.RESET_ALL}{Fore.LIGHTBLUE_EX}{str(ctx.message.guild.name)} {Fore.LIGHTWHITE_EX} ||-||  "
              f"{str(ctx.message.channel.name)}{Fore.LIGHTWHITE_EX}  ||-||  "
              f"{Fore.LIGHTGREEN_EX} Loaded: {Fore.YELLOW} {str(len(playLists))} songs {Fore.LIGHTWHITE_EX}from {str(saveName)}")

        return

    @commands.command(name='next')
    async def next(self, ctx):
        """Plays the next song in the queue."""
        print(f"NEXT FUNC - function begin - {ctx.guild.name}")
        
        megaEntry = next((each for each in sm.megaArray if each[0][0][0] == ctx.guild.id), None)
        
        if megaEntry is None:
            print("NEXT FUNC - no megaEntry")
            return

        songList = megaEntry[0][0][2]
        clip2 = megaEntry[0][5] # Current song
        shuffle = megaEntry[0][2]

        if not songList:
            print(f"NEXT FUNC - songList empty - {ctx.guild.name}")
            await self.stopplaying(ctx, nosend="notNaN")
            await self.leave(ctx)
            return

        nextClip, nextTitle, nextDuration, nextSongNum = None, None, None, None

        if shuffle is None or shuffle == 0:
            # --- NORMAL PLAY ---
            try:
                current_index = next((i for i, song in enumerate(songList) if song[0] == clip2), -1)
                next_index = (current_index + 1) % len(songList) # Wrap around
                
                song_to_play = songList[next_index]
                nextClip, nextSongNum, nextTitle, nextDuration = song_to_play[0], song_to_play[1], song_to_play[2], song_to_play[3]
                
            except Exception as e:
                print(f"Error in 'next' (normal mode): {e}. Defaulting to first song.")
                song_to_play = songList[0]
                nextClip, nextSongNum, nextTitle, nextDuration = song_to_play[0], song_to_play[1], song_to_play[2], song_to_play[3]
        
        else:
            # --- SHUFFLE PLAY ---
            if len(songList) > 0:
                song_to_play = random.choice(songList)
                nextClip, nextSongNum, nextTitle, nextDuration = song_to_play[0], song_to_play[1], song_to_play[2], song_to_play[3]
            else:
                 await self.stopplaying(ctx, nosend="notNaN")
                 await self.leave(ctx)
                 return

        if nextClip:
            print(f"NEXT FUNC -  await skipto - {ctx.guild.name}")
            await self.skipto(ctx, direct=[nextClip, nextTitle, nextDuration, nextSongNum])
        else:
            print(f"NEXT FUNC - no next clip found - {ctx.guild.name}")
            await self.stopplaying(ctx, nosend="notNaN")
            await self.leave(ctx)
        return

    @commands.command(name='prev')
    async def prev(self, ctx):
        """Plays the previous song in the queue (shuffle must be off)."""
        megaEntry = next((each for each in sm.megaArray if each[0][0][0] == ctx.guild.id), None)
        
        if megaEntry is None:
            return

        songList = megaEntry[0][0][2]
        clip2 = megaEntry[0][5] # Current song
        shuffle = megaEntry[0][2]

        if shuffle == 1:
            await messageHandler(ctx=ctx,
                                 lines=[f"@#F Information: @#V 'prev' command is disabled while shuffle is on."],
                                 quietMode=2)
            return
            
        if not songList:
            return

        nextClip, nextTitle, nextDuration, nextSongNum = None, None, None, None

        try:
            current_index = next((i for i, song in enumerate(songList) if song[0] == clip2), -1)
            next_index = (current_index - 1)
            if next_index < 0:
                next_index = len(songList) - 1 # Wrap around to end
            
            song_to_play = songList[next_index]
            nextClip, nextSongNum, nextTitle, nextDuration = song_to_play[0], song_to_play[1], song_to_play[2], song_to_play[3]
            
        except Exception as e:
            print(f"Error in 'prev': {e}. Defaulting to last song.")
            song_to_play = songList[-1]
            nextClip, nextSongNum, nextTitle, nextDuration = song_to_play[0], song_to_play[1], song_to_play[2], song_to_play[3]

        if nextClip:
            await self.skipto(ctx, direct=[nextClip, nextTitle, nextDuration, nextSongNum])
        return

    async def generate_spotipy_token(self):
        """Generates a Spotipy client credentials token."""
        client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
        client_id = os.getenv("SPOTIPY_CLIENT_ID")
        if not client_id or not client_secret:
            print("SPOTIPY_CLIENT_ID or SPOTIPY_CLIENT_SECRET not in .env file.")
            return None
        
        credentials = oauth2.SpotifyClientCredentials(
            client_id=client_id,
            client_secret=client_secret)
        token = credentials.get_access_token(as_dict=False) # Get raw token
        return token

    @commands.command(name='addlist')
    async def addlist(self, ctx, URL=None):
        """Adds songs from a YouTube or Spotify playlist to the queue."""
        if ctx.guild.id in sm.addListsActive:
            await messageHandler(ctx=ctx, lines=[
                "@#F Error: @#V there is already an addlists command running, please wait."], quietMode=2)
            return

        ctxmsg = ctx.message
        ctxsend = ctx.send
        ctxchan = ctx.message.channel
        
        content = ctx.message.content
        
        sm.addListsActive.append(ctx.guild.id)
        
        try:
            # --- SPOTIFY PLAYLIST ---
            if ("spotify.com" in content and "playlist" in content) or \
               ("http://googleusercontent.com/spotify.com" in content): # Handle old link
                token = await self.generate_spotipy_token()
                if not token:
                    await messageHandler(ctx=ctxchan, lines=[f" @#F Error: @#V Spotify API credentials not set up by bot owner."])
                    sm.addListsActive.remove(ctx.guild.id)
                    return
                    
                playlistID = content.split("playlist/")[1].split("?")[0]
                playlist_id = f'spotify:playlist:{playlistID}'
                spotify = spotipy.Spotify(auth=token)
                
                results = spotify.playlist(playlist_id)
                tracks = []
                for item in results['tracks']['items']:
                    if item['track']:
                        tracks.append(f"{item['track']['name']} - {item['track']['artists'][0]['name']}")
                
                msg2edit = await ctxsend(f"```Please wait... 0/{len(tracks)}```")
                await self.spotifylistadd(ctx, tracks, len(tracks), msg2edit)

            # --- YOUTUBE PLAYLIST ---
            elif "youtube.com" in content and "list=" in content:
                urls = re.findall(r'https?://[^\s]+', content)
                youtube_links = [url for url in urls if "youtube.com" in url and "list=" in url]
                
                if not youtube_links:
                    await messageHandler(ctx=ctxchan, lines=[f" @#F Error: @#V No valid YouTube playlist link found."])
                    sm.addListsActive.remove(ctx.guild.id)
                    return
                
                if not os.getenv('YOUTUBE_API_KEY'):
                    await messageHandler(ctx=ctxchan, lines=[f" @#F Error: @#V YouTube API key not set up by bot owner. Cannot add playlists."])
                    sm.addListsActive.remove(ctx.guild.id)
                    return

                taskloops = []
                for link in youtube_links:
                    taskloops.append(self.addlist2(ctx=ctx, url=link))
                
                await asyncio.gather(*taskloops)
                await messageHandler(ctx=ctxchan, lines=[
                        f"@#F Task(s) Completed: @#V Added playlist(s) to the current queue."])

            else:
                await messageHandler(ctx=ctxchan, lines=[f" @#F Error: @#V Link not recognized. Please provide a YouTube or Spotify playlist link."])
        
        except Exception as e:
            print(traceback.format_exc())
            await messageHandler(ctx=ctxchan, lines=[f" @#F Error: @#V Failed to process playlist. {e}"])
        
        finally:
            if ctx.guild.id in sm.addListsActive:
                sm.addListsActive.remove(ctx.guild.id)
        return

    async def spotifylistadd(self, ctx, tracks, totaltracknumber, msg2edit):
        """Helper function to add Spotify tracks to the queue."""
        counter = 0
        counter2 = 0
        for each in tracks:
            print(f"Spotify List Add: {each}")
            counter += 1
            counter2 += 1
            if counter2 >= 5:
                counter2 = 0
                try:
                    await msg2edit.edit(content=f"```Please wait... {counter}/{totaltracknumber}```")
                except:
                    pass # Ignore edit errors
            
            f_clip, f_title, video_duration, data = await getVideoTitle(clip2=None, returnB="clip2",
                                                                        video_title=each,
                                                                        mode="loadmatch", spopifoo=each) # Use search as spopifoo key
            if f_clip is None or f_title is None or video_duration is None:
                f_clip = await getClip(each)
                if not f_clip:
                    print(f"Could not find YouTube match for {each}")
                    continue # Skip this track
                f_title, video_duration = await getVideoTitle(clip2=f_clip, returnB="notNone", mode="load")
                # Cache this result for next time
                sm.loop.create_task(referenceDB(f_clip, f_title, video_duration, "spopify", spopifoo=each))


            await self.add2(ctx=ctx,
                            retrplz=False,
                            f_clip=f_clip,
                            f_title=each, # Use spotify title
                            nosend="NaN",
                            SongNumber=None,
                            addlistcmd="notnone",
                            video_duration=video_duration,
                            noLinkCheck=1)
            await asyncio.sleep(0.5) # Rate limit
            
        await msg2edit.edit(content=f"```Added {counter}/{totaltracknumber} from your spotify playlist```")
        return

    @commands.command(name='active')
    @commands.is_owner()
    async def reportactive(self, ctx):
        """Reports active voice connections (Owner only)."""
        if not sm.megaArray:
            await ctx.send("No active voice connections.")
            return

        for each in sm.megaArray:
            GuildID = each[0][0][0]
            server = each[0][0][4]
            voice_client = each[0][0][3]
            voiceChannel = each[0][0][1]
            songNumList = each[0][0][2]
            songNumListLen = len(songNumList)
            
            voiceChannelStr = voiceChannel.name if voiceChannel else "None"
            member_string = "None"
            if voiceChannel:
                member_string = str(len(voiceChannel.members))
            
            voice_clientSTR = str(voice_client) if voice_client else "None"

            print(
                f"{Style.RESET_ALL}{Fore.LIGHTWHITE_EX}------------------------------------------------------------")
            print(f"{Style.RESET_ALL}{Fore.CYAN}Voice Channel Guild: " + str(server))
            print(f"{Style.RESET_ALL}{Fore.CYAN}Voice Channel Name: " + str(voiceChannelStr))
            print(f"{Style.RESET_ALL}{Fore.LIGHTRED_EX}Voice Channel members: " + str(member_string))
            print(f"{Style.RESET_ALL}{Fore.MAGENTA}Number of songs in current list: " + str(songNumListLen))
            print(f"{Style.RESET_ALL}{Fore.YELLOW}Voice client obj: " + str(voice_clientSTR))
            print(
                f"{Style.RESET_ALL}{Fore.LIGHTWHITE_EX}------------------------------------------------------------{Style.RESET_ALL}")
        await ctx.send("Active connection data printed to console.")
        return

    @commands.command(name="play")
    async def play2(self, ctx):
        """Plays a song or resumes the queue."""
        megaEntry = next((each for each in sm.megaArray if each[0][0][0] == ctx.guild.id), None)
        command_parts = ctx.message.content.split(" ")

        # Case 1: Just `!play`
        if len(command_parts) <= 1:
            if megaEntry is None:
                await messageHandler(ctx=ctx, lines=["@#F Error: @#V There is nothing in the queue to play."])
                return

            voice_client = megaEntry[0][0][3]
            songNumList = megaEntry[0][0][2]

            if voice_client and voice_client.is_paused():
                voice_client.resume()
                await messageHandler(ctx=ctx, lines=["@#F Resumed: @#V Playback resumed."])
                return

            if voice_client and voice_client.is_playing():
                # Already playing, show 'np'
                await self.nowplayingfuck(ctx)
                return
            
            if not songNumList:
                 await messageHandler(ctx=ctx, lines=["@#F Error: @#V The queue is empty."])
                 return

            # --- Start playing from queue ---
            song_to_play_clip = megaEntry[0][5] # Get current/last song clip
            
            song_data = next((s for s in songNumList if s[0] == song_to_play_clip), None)
            if song_data is None and songNumList:
                song_data = songNumList[0] # Default to first song
            elif song_data is None:
                 await messageHandler(ctx=ctx, lines=["@#F Error: @#V Queue is empty."])
                 return
            
            clip2, video_title, songNumber, songDuration = song_data[0], song_data[2], song_data[1], song_data[3]

            # FIXED: Use helper function instead of pafy
            audio = await self.get_audio_url(clip2)
            
            if not audio:
                await messageHandler(ctx=ctx, lines=[f"@#F Error: @#V Could not get audio for {video_title}."])
                return
            
            channel = await getChannel(ctx)
            if not channel:
                await messageHandler(ctx=ctx, lines=[f"@#F Error: @#V You must be in a voice channel."])
                return
                
            voice_client = await getVoice(ctx, channel)
            if not voice_client:
                await messageHandler(ctx=ctx, lines=[f"@#F Error: @#V Could not join your voice channel."])
                return
                
            server = ctx.guild
            await arrayBuilder(ctx=ctx, audio=audio, clip2=clip2, playingSongNum=songNumber,
                               videoDuration=songDuration, video_title=video_title, voice_client=voice_client)
            await self.playingLoop(ctx, voice_client, server, config.ProjectFFMPEG, audio, clip2,
                                  video_title, songNumber, songDuration)
            return

        # Case 2: `!play [song query/url]`
        else:
            try:
                result = await self.add2(ctx, retrplz=True)
                if not result: # add2 failed and sent a message
                    return
                clip2, video_title, SongNumber, video_duration = result
            except TypeError:
                return
            
            megaEntry = next((each for each in sm.megaArray if each[0][0][0] == ctx.guild.id), None)
            
            is_playing = False
            if megaEntry and megaEntry[0][0][3]:
                vc = megaEntry[0][0][3]
                is_playing = vc.is_playing() or vc.is_paused()

            if not is_playing:
                # FIXED: Use helper function instead of pafy
                audio = await self.get_audio_url(clip2)
                
                if not audio:
                    await messageHandler(ctx=ctx, lines=[f"@#F Error: @#V Could not get audio for {video_title}."])
                    return

                await arrayBuilder(ctx, audio=audio, playingSongNum=SongNumber, clip2=clip2,
                                   video_title=video_title, videoDuration=video_duration)
                
                channel = await getChannel(ctx)
                if not channel:
                    await messageHandler(ctx=ctx, lines=[f"@#F Error: @#V You must be in a voice channel to play."])
                    return
                
                voice_client = await getVoice(ctx, channel)
                if not voice_client:
                    await messageHandler(ctx=ctx, lines=[f"@#F Error: @#V Could not join your voice channel."])
                    return

                await self.playingLoop(ctx, voice_client, ctx.guild, config.ProjectFFMPEG, audio, clip2,
                                      video_title, SongNumber, songDuration=video_duration)
            # Else: song was just added to queue by add2, confirmation was sent by it.
        return

    @commands.command(name='remove')
    async def remove(self, ctx):
        """Removes a song or range of songs from the queue."""
        megaEntry = next((each for each in sm.megaArray if each[0][0][0] == ctx.guild.id), None)
        
        if megaEntry is None or not megaEntry[0][0][2]:
            await messageHandler(ctx=ctx, lines=["@#F Error: @#V The queue is empty."], quietMode=2)
            return
        
        try:
            parts = str(ctx.message.content.split(" ")[1])
            if "-" in parts:
                range1 = int(parts.split("-")[0])
                range2 = int(parts.split("-")[1])
            else:
                range1 = int(parts)
                range2 = int(parts)
        except (IndexError, ValueError):
            await messageHandler(ctx=ctx, lines=["@#F Error: @#V Invalid format. Use `!remove [number]` or `!remove [num1-num2]`."], quietMode=2)
            return

        songList = megaEntry[0][0][2]
        playingSongNum = megaEntry[0][4]
        songListNew = []
        songremovedcounter = 0
        newSongNum = 0
        
        removed_playing_song = False
        
        for key in songList:
            song_num = key[1]
            if not (range1 <= song_num <= range2):
                newSongNum += 1
                songListNew.append([key[0], newSongNum, key[2], key[3]])
            else:
                songremovedcounter += 1
                if song_num == playingSongNum:
                    removed_playing_song = True
                    
        await arrayBuilder(ctx=ctx, songList=songListNew)
        await messageHandler(ctx=ctx,
                             lines=[f"@#F Complete: @#V Removed {songremovedcounter} songs from the playlist"])
        
        if removed_playing_song:
            await messageHandler(ctx=ctx, lines=["@#F Info: @#V The song that was playing was removed. Skipping..."])
            await self.next(ctx) # Play next song
        
        return

    @commands.command(name='clear')
    async def clear(self, ctx):
        """Clears the entire song queue."""
        megaEntry = next((each for each in sm.megaArray if each[0][0][0] == ctx.guild.id), None)
        
        if megaEntry:
            await arrayBuilder(ctx, songList=[])
            await messageHandler(ctx=ctx, lines=[f"@#F Playlist cleared: @#V Removed all from the playlist."],
                                 quietMode=2)
        else:
            await messageHandler(ctx=ctx, lines=[f"@#F Info: @#V Playlist is already empty."], quietMode=2)
        return

    @commands.command(name="tts")
    async def tts(self, ctx):
        """Generates and plays Text-to-Speech in the voice channel."""
        if ctx.guild.id in sm.stopArray:
            return # TTS already in progress
            
        sm.stopArray.append(ctx.guild.id)
        
        try:
            stringy = " ".join(ctx.message.content.split(" ")[1:])
            voices = ["david-attenborough", "arnold-schwarzenegger", "bob-barker", 
                      "bill-gates", "bill-clinton", "bill-nye", "homer-simpson",
                      "peter-griffin", "gilbert-gottfried"]
            stringy2 = random.choice(voices) # Selected voice
            
            # Custom voice selection
            if r"//" in stringy:
                parts = stringy.split(r"//")
                stringy = parts[0].strip()
                stringy2 = parts[1].strip().lower()
                if stringy2 not in voices:
                    await messageHandler(ctx=ctx, lines=[" @#F Failure: @#V Invalid voice specified."])
                    await sm.clearStopArray(ctx.guild.id)
                    return

            if not stringy:
                 await messageHandler(ctx=ctx, lines=[" @#F Failure: @#V No text provided for TTS."])
                 await sm.clearStopArray(ctx.guild.id)
                 return

            await messageHandler(ctx=ctx, lines=[
                f" @#F Processing: \n @#V Please wait. Processing text to speech...",
                f" @#F Voice Selected: \n @#V {stringy2}", f" @#F Text: @#V {stringy}"])

            try:
                # Use vocodes to generate TTS file
                audio_file = os.path.join(config.HomeDir, "temp_tts.wav")
                file_info = await self.tts_api.save_to_file(stringy2, stringy, audio_file)
                if 'status' in file_info and ("504" in file_info['status'] or "500" in file_info['status']):
                    raise Exception("API Error 50x")
            except Exception as e:
                print(f"TTS API Error: {e}")
                await messageHandler(ctx=ctx, lines=[" @#F Failure: @#V TTS generation failed. Try again."])
                await sm.clearStopArray(ctx.guild.id)
                return

            channel = await getChannel(ctx)
            if not channel:
                await messageHandler(ctx=ctx, lines=[" @#F Failure: @#V You must be in a voice channel."])
                await sm.clearStopArray(ctx.guild.id)
                return
                
            voice = await getVoice(ctx, channel)
            if not voice:
                await messageHandler(ctx=ctx, lines=[" @#F Failure: @#V Could not join your voice channel."])
                await sm.clearStopArray(ctx.guild.id)
                return

            # --- Pause music and store playback time ---
            was_playing = False
            seek_time_str = None
            megaEntry = next((each for each in sm.megaArray if each[0][0][0] == ctx.guild.id), None)
            
            if voice.is_playing() or voice.is_paused():
                was_playing = True
                voice.pause()
                
                # Get current playback time
                startEpoch = None
                for i, epoch in enumerate(sm.playingEpoch):
                    if epoch[0] == ctx.guild.id:
                        startEpoch = epoch[1]
                        sm.playingEpoch.pop(i)
                        break
                
                if startEpoch:
                    seekTime = time.time()
                    elapsed = seekTime - startEpoch
                    hours, rem = divmod(elapsed, 3600)
                    minutes, seconds = divmod(rem, 60)
                    
                    seek_time_str = (
                        f"{int(hours):02d}:{int(minutes):02d}:{int(math.floor(seconds)):02d}"
                    )
                    print(f"{Fore.CYAN}TTS COMMAND: {Fore.LIGHTYELLOW_EX}Time to seek: {Fore.LIGHTGREEN_EX}{seek_time_str}")

            await asyncio.sleep(1)
            
            # --- Play TTS ---
            voice.play(discord.FFmpegPCMAudio(audio_file, executable=config.ProjectFFMPEG))
            while voice.is_playing():
                await asyncio.sleep(0.1)
            
            await asyncio.sleep(1)
            
            # --- Resume music ---
            if was_playing and megaEntry and megaEntry[0][3]: # Check if audio source exists
                videoDuration = megaEntry[0][7]
                audio = megaEntry[0][3]
                playingSongNum = megaEntry[0][4]
                clip2 = megaEntry[0][5]
                video_title = megaEntry[0][6]
                
                resume_opts = config.ffmpeg_opts
                if seek_time_str:
                    resume_opts = {
                        'before_options': f'-ss {seek_time_str} -reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
                        'options': '-vn'
                    }
                
                sm.loop.create_task(
                    self.playingLoop(ctx, voice, ctx.guild, config.ProjectFFMPEG, audio,
                                     clip2, video_title, playingSongNum, videoDuration,
                                     ffmpeg_opts=resume_opts, skipMessage="notNone")
                )

        except Exception as e:
            print(traceback.format_exc())
            await messageHandler(ctx=ctx, lines=[" @#F Failure: @#V An unexpected error occurred."])
        finally:
            await sm.clearStopArray(ctx.guild.id) # Always clear stop array
        return

    # --- CORE MUSIC LOGIC ---

    async def playingLoop(self, ctx, voice, server, ProjectFFMPEG, audio,
                          clip2, video_title, songNumber, songDuration, 
                          ffmpeg_opts=config.ffmpeg_opts, skipMessage=None):
        """The main loop that plays audio in the voice channel."""
        
        # Check if another playingLoop is already starting
        if ctx.guild.id in sm.stopArray:
            print(f"P{ctx.guild.name} - playingLoop blocked by stopArray")
            return
            
        sm.stopArray.append(ctx.guild.id) # Signal that this loop is taking over
        
        # Clear previous epoch
        sm.playingEpoch = [epoch for epoch in sm.playingEpoch if epoch[0] != ctx.guild.id]
        sm.playingEpoch.append([ctx.guild.id, time.time()])

        if clip2 == "NaN":
            await sm.clearStopArray(ctx.guild.id)
            return

        # Ensure voice client is valid
        if voice is None or not voice.is_connected():
            try:
                channel = await getChannel(ctx)
                voice = await getVoice(ctx, channel)
                await arrayBuilder(ctx, audio=audio, voice_client=voice, clip2=clip2, video_title=video_title,
                                   videoDuration=songDuration)
            except Exception as e:
                print(f"Error re-connecting voice in playingLoop: {e}")
                await sm.clearStopArray(ctx.guild.id)
                return
        
        try:
            if voice.is_playing() or voice.is_paused():
                voice.stop()
        except Exception as e:
            print(f"Error stopping previous audio: {e}")
            pass

        if songNumber is not None:
            stringy = str(songNumber)
        else:
            stringy = ""
            
        if songDuration is None:
            video_title, songDuration = await getVideoTitle(clip2, returnB="notNone")
        
        if skipMessage is None and await getQuietMode(ctx) is None:
            commandPrefix = await self.bot.get_prefix(ctx.message)
            try:
                duration_str = (
                    f"{str(lessOrMore(int(math.floor(float(int(songDuration) / 60)))))}:"
                    f"{str(lessOrMore(int(int(songDuration) % 60)))}"
                )
            except:
                duration_str = "N/A"

            sm.loop.create_task(messageHandler(ctx=ctx, lines=[
                " @#F Now Playing: " +
                f" @#V {stringy}. - [" + str(video_title) + f"]({clip2})",
                f" @#F Duration: @#V {duration_str}"
                f" ({commandPrefix}seek 00:00-{duration_str})"
            ]))

        try:
            voice.play(FFmpegPCMAudio(executable=ProjectFFMPEG, source=audio, **ffmpeg_opts))
        except Exception as e:
            print(f"Error starting playback: {e}")
            await messageHandler(ctx=ctx, lines=[f"@#F Error: @#V Could not play audio: {e}"])
            await sm.clearStopArray(ctx.guild.id)
            return

        await arrayBuilder(ctx, isPlaying=1)
        await sm.clearStopArray(ctx.guild.id) # Allow other commands now

        while voice.is_playing() or voice.is_paused():
            await asyncio.sleep(0.5)
            if ctx.guild.id in sm.stopArray:
                print("playingLoop killed by stopArray")
                voice.stop() # Stop playback
                return
            
            if not voice.is_connected():
                print("playingLoop stopped, voice disconnected.")
                await sm.clearStopArray(ctx.guild.id)
                # Remove from megaArray
                sm.megaArray = [entry for entry in sm.megaArray if entry[0][0][0] != ctx.guild.id]
                return # Stop loop if disconnected

        # Song finished naturally
        if ctx.guild.id not in sm.stopArray:
            print("playingLoop() - song finished, calling next()")
            sm.stopArray.append(ctx.guild.id) # Prevent race condition
            await self.next(ctx)
        
        return

    async def addlist2(self, ctx=None, url=None):
        """Helper function to add a YouTube playlist."""
        ctxsend = ctx.send
        
        try:
            query = parse_qs(urlparse(url).query, keep_blank_values=True)
            playlist_id = query["list"][0]
        except KeyError:
            sm.loop.create_task(messageHandler(ctx=ctx, lines=[f"@#F Error: @#V Can't find list in {url}"]))
            return

        try:
            # Note: This requires a Google API Key with YouTube Data API v3 enabled
            youtube = build("youtube", "v3", developerKey=os.getenv('YOUTUBE_API_KEY'))
            request = youtube.playlistItems().list(
                part="snippet",
                playlistId=playlist_id,
                maxResults=50
            )
            playlist_items = []
            
            while request is not None:
                response = request.execute()
                playlist_items += response["items"]
                request = youtube.playlistItems().list_next(request, response)
        except Exception as e:
            print(f"YouTube API Error: {e}")
            await messageHandler(ctx=ctx, lines=[f"@#F Error: @#V Could not fetch YouTube playlist. Check YOUTUBE_API_KEY in .env file. \n```{e}```"])
            return

        print(f"total: {len(playlist_items)}")
        
        messageSent = await ctxsend("```Processed: 0/" + str(len(playlist_items)) + "```")
        counter = 0
        counter2 = 0
        
        for item in playlist_items:
            try:
                if "snippet" not in item or "resourceId" not in item["snippet"] or "videoId" not in item["snippet"]["resourceId"]:
                    print("Skipping private/deleted video in playlist.")
                    continue
                    
                video_id = item["snippet"]["resourceId"]["videoId"]
                clip2 = f'https://www.youtube.com/watch?v={video_id}'
                
                videoData = await referenceDB(clip2, None, None, "load")
                if videoData is not None:
                    video_title, video_duration = videoData[1], videoData[2]
                else:
                    video_title, video_duration = await getVideoTitle(clip2, returnB="NotNone")

                if "error 298" != str(video_title):
                    counter += 1
                    counter2 += 1
                    sm.loop.create_task(self.add2(ctx, f_clip=clip2, f_title=video_title, video_duration=video_duration,
                                          addlistcmd="notnone", noLinkCheck=1, nosend="NaN"))
                    
                    if counter2 > 10: # Update message every 10 songs
                        sm.loop.create_task(messageSent.edit(
                            content=f"```Processed: {counter}/{len(playlist_items)}\n{video_title[:25]}...```"))
                        counter2 = 0
            except Exception as e:
                print(f"Error adding song from playlist: {e}")
        
        await messageSent.edit(content=f"```-Added: \n{counter} / {len(playlist_items)}\nsongs from youtube playlist.```")
        return

    async def rebuildPlaylist(self, ctx, file=None, listT=None):
        """Rebuilds a playlist file if it's in an old format."""
        if file is None and listT is None:
            return
        
        PlayList = []
        if listT is not None:
            PlayList = listT
        elif file is not None:
            PlayList = numpy.load(file, allow_pickle=True).tolist()
            
        newList = []
        for each in PlayList:
            try:
                clip2 = each[0]
                position = each[1]
                title = each[2]
                
                localVideoData = await referenceDB(clip2, None, None, "load")
                
                if localVideoData is not None:
                    newList.append([localVideoData[0], position, localVideoData[1], localVideoData[2]])
                else:
                    title, duration = await getVideoTitle(clip2, returnB="notnone")
                    newList.append([clip2, position, title, duration])
            except Exception as e:
                print(f"Error rebuilding playlist entry: {e}")

        # Note: This function no longer saves to the file,
        # it just returns the rebuilt list. The 'load' command handles saving.
        
        sm.loop.create_task(messageHandler(ctx=ctx, lines=[f"@#F Information: @#V Finished rebuilding playlist."]))
        return newList

    async def add2(self, ctx, retrplz=False, f_clip=None, f_title=None, nosend="NaN",
                   SongNumber=None, addlistcmd=None, video_duration=None, noLinkCheck=None):
        """Core logic for adding a song to the queue."""
        
        content = ctx.message.content
        if ("http" in content and ("youtube" in content or "spotify" in content) and \
            ("list=" in content or "playlist" in content) and noLinkCheck is None):
            sm.loop.create_task(self.addlist(ctx)) # Reroute to addlist command
            return

        clipStr = " ".join(ctx.message.content.split(" ")[1:])

        if f_clip is None and f_title is None:
            if "http" in clipStr.lower() and "youtube.com" in clipStr.lower() and "://" in clipStr.lower():
                if "watch?v=" in clipStr:
                    f_clip = "http://www.youtube.com/watch?v=" + clipStr.split("watch?v=")[1][:11]
                    f_title, video_duration = await getVideoTitle(clip2=f_clip, returnB="notNone")
            else:
                if not clipStr:
                     await messageHandler(ctx=ctx, lines=[f" @#F Error: @#V Please provide a song name or URL."])
                     return None if retrplz else None
                
                # --- SAFE SEARCH LOGIC ---
                # 1. Try to find in cache
                f_clip, f_title, video_duration = None, None, None
                try:
                    cached_data = await getVideoTitle(clip2=None, returnB="clip2",
                                                      video_title=clipStr,
                                                      mode="loadmatch", spopifoo=None)
                    if cached_data and len(cached_data) >= 3:
                        # We ignore the 4th item (dataString/matchInfo) if present
                        f_clip, f_title, video_duration = cached_data[0], cached_data[1], cached_data[2]
                except Exception:
                    pass # Cache lookup failed or unpacking error, move to web search

                # 2. If cache miss, search web
                if f_clip is None:
                    f_clip = await getClip(clipStr)
                    if f_clip:
                        f_title, video_duration = await getVideoTitle(clip2=f_clip, returnB="notNone")

        if f_title == "error 298" or f_clip is None:
            await messageHandler(ctx=ctx, lines=[f" @#F Error: @#V Could not find or access the video."])
            return None if retrplz else None

        video_title = f_title
        
        songNumList = []
        megaEntry = next((each for each in sm.megaArray if each[0][0][0] == ctx.guild.id), None)
        
        if megaEntry:
            songNumList = megaEntry[0][0][2]
        
        if SongNumber is None:
            SongNumber = len(songNumList) + 1
            
        songNumList.append([f_clip, SongNumber, video_title, video_duration])
        
        await arrayBuilder(ctx=ctx, songList=songNumList)

        if retrplz:
            return f_clip, video_title, SongNumber, video_duration
        
        if nosend != "NaN":
            commandPrefix = await self.bot.get_prefix(ctx.message)
            await messageHandler(ctx=ctx, lines=[" @#F Added: @#V " + f"```{config.formatString}\n" + str(video_title) + \
                                                 "```\n to the playlist \n Position : " + str(len(songNumList)) + \
                                                 f"\nYou can use {commandPrefix}skipto {str(len(songNumList))}"],
                                 quietMode=await getQuietMode(ctx))
        return

    
    async def list2cmd(self, ctx, page=0, msg=None):
        """Logic for the paginated list command."""
        
        # Determine if we're handling a command or an interaction
        is_interaction = isinstance(ctx, discord.Interaction)
        
        guild_id = ctx.guild.id if hasattr(ctx, 'guild') and ctx.guild else ctx.guild_id
        channel = ctx.channel
        
        if is_interaction:
            msg = ctx.message # The message to edit
        
        currentPage = 0
        
        # Get current page for this guild
        guild_pages = [entry for entry in sm.list2array if entry[0] == guild_id]
        if guild_pages:
            currentPage = guild_pages[0][3] # Get page from first entry
        
        # Clear old page data for this guild
        sm.list2array = [entry for entry in sm.list2array if entry[0] != guild_id]
        
        # Get SongList
        SongList = []
        megaEntry = next((each for each in sm.megaArray if each[0][0][0] == guild_id), None)
        if megaEntry:
            SongList = megaEntry[0][0][2]

        if not SongList:
            await messageHandler(ctx=channel, lines=[f" @#F Playlist: @#V There is nothing in the list."], quietMode=2, msg2edit=msg, view=None)
            return
        
        counter2 = -1 # Page index
        targetPage = currentPage + page
        
        # Ensure target page is valid
        if targetPage < 0:
            targetPage = 0

        msgString = ""
        pagen = ""
        
        for key in SongList:
            if len(str(key[2])) >= 45:
                stringy = "..."
            else:
                stringy = ""
            msgString += f"**{key[1]}.** {str(key[2])[:45]}{stringy} \n"
            
            if len(msgString) > 500: # Page break
                counter2 += 1
                sm.list2array.append([guild_id, counter2, msgString, targetPage])
                if counter2 == targetPage:
                    pagen = msgString
                msgString = ""
        
        if msgString: # Add the last page
            counter2 += 1
            sm.list2array.append([guild_id, counter2, msgString, targetPage])
            if pagen == "": # If it was the only page
                pagen = msgString
        
        if counter2 == -1: # No pages (should be caught by SongList check)
             await messageHandler(ctx=channel, lines=[f" @#F Playlist: @#V There is nothing in the list."], quietMode=2, msg2edit=msg, view=None)
             return

        # Ensure target page is valid after counting
        if targetPage > counter2:
            targetPage = counter2
            
        # Update array with corrected targetPage
        for i in range(len(sm.list2array)):
            if sm.list2array[i][0] == guild_id:
                sm.list2array[i][3] = targetPage
        
        # Get the correct page content
        pagen = ""
        for entry in sm.list2array:
            if entry[0] == guild_id and entry[1] == targetPage:
                pagen = entry[2]
                break
        
        # Create the view for buttons
        view = ListView(self, targetPage, counter2)

        if pagen:
            await messageHandler(ctx=channel, lines=[
                f" @#F Playlist Page {targetPage + 1}/{str(counter2 + 1)}: @#V \n{pagen}"], quietMode=2,
                                 view=view, msg2edit=msg)
        return