import os
import sys
import subprocess
import importlib.util
import traceback

# --- Environment Setup ---
def setup_environment():
    """
    Checks if required packages are installed.
    """
    # Map import name to pip install name
    required_packages = {
        "discord": "discord.py",
        "nacl": "PyNaCl", # FIXED: Added Voice Support
        "pafy": "pafy",
        "yt_dlp": "yt-dlp", 
        "spotipy": "spotipy",
        "numpy": "numpy",
        "ahk": "ahk",
        "colorama": "colorama",
        "dotenv": "python-dotenv",
        "googleapiclient": "google-api-python-client",
        "httplib2": "httplib2",
        "lxml": "lxml",
        "oauth2client": "oauth2client",
        "vocodes_api": "vocodes-api",
        "psutil": "psutil",
        "textdistance": "textdistance",
        "PIL": "Pillow",
        "cv2": "opencv-python-headless",
        "nest_asyncio": "nest_asyncio",
        "pydub": "pydub",
        "bs4": "beautifulsoup4",
        "requests": "requests",
        "socks": "PySocks" 
    }
    
    missing_packages = []
    print("Verifying environment...")
    
    for import_name, install_name in required_packages.items():
        if importlib.util.find_spec(import_name) is None:
            print(f"  - Missing package: {import_name} (will install {install_name})")
            missing_packages.append(install_name)

    if not missing_packages:
        print("Verified: All required packages found. Launching application.")
        return

    print("\n--- ONE-TIME ENVIRONMENT SETUP ---")
    print("The following libraries are missing and will be installed:")
    for pkg in missing_packages: 
        print(f"  - {pkg}")
    print("This may take a few minutes.")

    try:
        install_command = [sys.executable, "-m", "pip", "install"] + missing_packages
        subprocess.check_call(install_command)
        print("\n--- SETUP COMPLETE ---\nPlease RESTART the application for the changes to take effect.")
        sys.exit(0)
    except Exception as e:
        print(f"An unexpected error occurred during setup: {e}")
        sys.exit(1)

# --- Initial Setup ---
setup_environment()

# --- Main Imports ---
import certifi, ssl
import asyncio, socks, socket, sock
import bs4
import datetime
import fnmatch
import json
import locale
import logging
import math
import numpy
import pickle
import random
import re
import requests
import signal
import string
import threading
import time
import urllib

# --- MONKEY PATCH: Force yt_dlp to be used as youtube_dl ---
import yt_dlp as youtube_dl
sys.modules['youtube_dl'] = youtube_dl
# -----------------------------------------------------------

from discord import Spotify
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from collections import namedtuple
from concurrent.futures import ThreadPoolExecutor
from string import ascii_lowercase
from typing import List
from urllib.parse import parse_qs, urlparse
import discord.user
from ahk import AHK
from bs4 import BeautifulSoup, SoupStrainer
import colorama
from colorama import init, Fore, Back, Style
from dotenv import load_dotenv
from googleapiclient.discovery import build
from httplib2 import Http
from lxml import etree
from oauth2client import file, client, tools
from vocodes_api import VocodesAPI
# Import yt_dlp instead of youtube_dl
from yt_dlp import YoutubeDL, DownloadError 
import discord
from discord import FFmpegPCMAudio, HTTPException, NotFound
from discord.errors import Forbidden, HTTPException, NotFound
from discord.ext import commands
from discord.ext.commands import CommandNotFound, Bot
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
import imgur_url
import ssl
from shutil import copyfile
from pydub import AudioSegment
import sqlite3

try:
    from http.cookiejar import CookieJar
except ImportError:
    from cookielib import CookieJar

# --- BOT SETUP ---

# Import refactored files
import config
import state_manager as sm
import database_manager as db
from bot_events import BotEventsCog
from music_cog import MusicCog
from misc_cog import MiscCog, ButtonView

# Apply nest_asyncio
nest_asyncio.apply()
init()

# -----------------------------------------------------------------
# Initialize Database & Create Folders
# -----------------------------------------------------------------
try:
    db.init_db()
    print("Database and directories initialized.")
except sqlite3.Error as e:
    print(f"FATAL: Could not initialize database at {config.DB_PATH}: {e}")
    exit()

# Initialize AHK
try:
    sm.ahk = AHK(executable_path=config.HomeDir + r"/AutoHotkey/AutoHotkeyU64.exe")
except Exception as e:
    print(f"Warning: AHK failed to load. /cmd command will not work. Error: {e}")
    sm.ahk = None

# Load server prefixes from DB
sm.serverData = db.get_all_prefixes()
print(f"Loaded {len(sm.serverData)} guild prefixes.")

# Load button counter
try:
    with open(config.HomeDir + "/Saves/TheButtonCounter.txt", "r", encoding="utf8") as f:
        sm.counterButton = f.read()
    f.close()
    if sm.counterButton == "" or type(sm.counterButton) is type(None):
        sm.counterButton = 0
    else:
        sm.counterButton = int(sm.counterButton)
except FileNotFoundError:
    print("ButtonCounter.txt not found, creating and starting at 0.")
    with open(config.HomeDir + "/Saves/TheButtonCounter.txt", "w", encoding="utf8") as f:
        f.write("0")
    sm.counterButton = 0
except Exception as e:
    print(f"Error loading button counter: {e}")
    sm.counterButton = 0


# Set converter for pydub
AudioSegment.converter = config.ProjectFFMPEG


async def determine_prefix(bot, message):
    """Determines the command prefix for the bot."""
    commandPrefix = '1!'  # Default
    
    if config.devMode is True:
        commandPrefix = ">?"
        return commandPrefix

    if message.content[:3] == "!!!":
        commandPrefix = "!!!"
        return commandPrefix

    if not hasattr(message, 'guild') or message.guild is None:
         # In DMs
        if (sm.SerbzChannel and message.channel.id == sm.SerbzChannel.id) or \
           (sm.SerbzChannel2 and message.channel.id == sm.SerbzChannel2.id):
            commandPrefix = "?"
        return commandPrefix

    try:
        guildID = message.guild.id
        for each in sm.serverData:
            if each[0] == str(guildID): # Compare as strings
                commandPrefix = each[1]
                break
    except AttributeError:
        pass # Should be caught by guild check
        
    return commandPrefix


# --- BOT INITIALIZATION ---

# Set up intents
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
intents.guilds = True
intents.voice_states = True

# Create Bot instance
sm.musicBot = commands.Bot(command_prefix=determine_prefix, help_command=None, case_insensitive=True, intents=intents)

# Initialize Cogs
music_cog_instance = MusicCog(sm.musicBot)
misc_cog_instance = MiscCog(sm.musicBot)
events_cog_instance = BotEventsCog(sm.musicBot)


# --- MAIN ASYNC FUNCTION ---

async def main():
    """Main function to setup and run the bot."""
    sm.loop = asyncio.get_event_loop()
    
    # Start background tasks
    sm.loop.create_task(sm.guildCountDown())
    
    # Add cogs
    await sm.musicBot.add_cog(music_cog_instance)
    await sm.musicBot.add_cog(misc_cog_instance) 
    await sm.musicBot.add_cog(events_cog_instance)
    
    # Register persistent View
    @sm.musicBot.event
    async def on_ready():
        sm.musicBot.add_view(ButtonView(misc_cog_instance))
        print("Persistent ButtonView added.")
        # Discord automatically calls on_ready in the Cog.

    # Start the bot
    try:
        await sm.musicBot.start(config.TOKENS[0])
    except discord.errors.LoginFailure:
        print("FATAL ERROR: Bot token is invalid. Please check your .env file for 'DISCORD_TOKEN1'.")
    except Exception as e:
        print(f"Error starting bot: {e}")
        traceback.print_exc()
        # Handle restart logic if necessary
        os.execv(sys.executable, ['python'] + sys.argv)

if __name__ == "__main__":
    asyncio.run(main())