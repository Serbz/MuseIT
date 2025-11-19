import os
import ssl
from dotenv import load_dotenv
from string import ascii_lowercase

# --- GENERAL SETTINGS ---
quietOut = True
accTimers = False
potatoesBool = True
devMode = False  # FIXED: Disabled Developer Mode
samuraibbot = False
musicbotDisable = 0
timers = True
formatString = "yaml"

# --- PATHS ---
# HomeDir is relative to the script location
HomeDir = os.path.dirname(os.path.abspath(__file__))

# Use os.path.join for cross-platform compatibility
ProjectFFMPEG = os.path.join(HomeDir, "ffmpeg", "bin", "ffmpeg.exe")
ProjectFFMPEG4 = os.path.join(HomeDir, "pyproj", "ffmpeg", "bin", "ffprobe.exe")
ProjectFFMPEG2 = os.path.join(HomeDir, "pyproj", "ffmpeg", "bin", "ffplay.exe")
ProjectFFMPEG3 = os.path.join(HomeDir, "pyproj", "ffmpeg", "bin", "ffprobe.exe")

# --- DATABASE PATH ---
DB_PATH = os.path.join(HomeDir, 'Saves', 'Databases', 'museit.db')

# --- API & TOKENS ---
load_dotenv() 
TOKENS = []
tokenCounter = 0
while tokenCounter < 1:
    tokenCounter += 1
    token = os.getenv('DISCORD_TOKEN' + str(tokenCounter))
    if token:
        TOKENS.append(token)

if not TOKENS:
    print("FATAL ERROR: 'DISCORD_TOKEN1' not found in .env file.")
    print(f"Looked for .env in: {os.getcwd()}")
    exit()

if not os.getenv('YOUTUBE_API_KEY'):
    print("WARNING: 'YOUTUBE_API_KEY' not found in .env file. /addlist command will fail.")
    
if not os.getenv('SPOTIPY_CLIENT_ID') or not os.getenv('SPOTIPY_CLIENT_SECRET'):
    print("WARNING: 'SPOTIPY_CLIENT_ID' or 'SPOTIPY_CLIENT_SECRET' not found. Spotify /addlist will fail.")


# --- BOT & API SETTINGS ---
sysChannelID = 871650226828619808
ID_List = [
    "246892047284436992",  # Serbz#0001
    "246892047284436992",  # Serbz#0001
]

# --- NETWORK & PROXIES ---
proxies = [
    {'http': 'socks5h://127.0.0.1:9100', 'https': 'socks5h://127.0.0.1:9100'},
    {'http': 'socks5h://127.0.0.1:9106', 'https': 'socks5h://127.0.0.1:9106'},
    {'http': 'socks5h://127.0.0.1:9105', 'https': 'socks5h://127.0.0.1:9105'},
    {'http': 'socks5h://127.0.0.1:9104', 'https': 'socks5h://127.0.0.1:9104'},
    {'http': 'socks5h://127.0.0.1:9103', 'https': 'socks5h://127.0.0.1:9103'},
    {'http': 'socks5h://127.0.0.1:9102', 'https': 'socks5h://127.0.0.1:9102'},
    {'http': 'socks5h://127.0.0.1:9101', 'https': 'socks5h://127.0.0.1:9101'},
    {'http': 'socks5h://127.0.0.1:9109', 'https': 'socks5h://127.0.0.1:9109'},
    {'http': 'socks5h://127.0.0.1:9108', 'https': 'socks5h://127.0.0.1:9108'},
    {'http': 'socks5h://127.0.0.1:9201', 'https': 'socks5h://127.0.0.1:9201'},
    {'http': 'socks5h://127.0.0.1:9202', 'https': 'socks5h://127.0.0.1:9202'},
    {'http': 'socks5h://127.0.0.1:9203', 'https': 'socks5h://127.0.0.1:9203'},
    {'http': 'socks5h://127.0.0.1:9204', 'https': 'socks5h://127.0.0.1:9204'},
    {'http': 'socks5h://127.0.0.1:9205', 'httpss': 'socks5h://127.0.0.1:9205'},
    {'http': 'socks5h://127.0.0.1:9206', 'https': 'socks5h://127.0.0.1:9206'},
    {'http': 'socks5h://127.0.0.1:9207', 'https': 'socks5h://127.0.0.1:9207'},
    {'http': 'socks5h://127.0.0.1:9208', 'https': 'socks5h://127.0.0.1:9208'},
    {'http': 'socks5h://127.0.0.1:9209', 'https': 'socks5h://127.0.0.1:9209'}
]

tsctx = ssl.create_default_context()
tsctx.check_hostname = False
tsctx.verify_mode = ssl.CERT_NONE

TorSocketIP = "192.168.1.64"
TorSocketPorts = ["9050", "9051", "9052", "9053", "9054", "9055", "9056", "9057", "9058", "9059"]

# --- CUSTOM LOGGER TO SUPPRESS WARNINGS ---
class YTDLLogger(object):
    def debug(self, msg):
        pass # Ignore debug messages

    def warning(self, msg):
        # Filter out the specific annoying warnings
        if "No supported JavaScript runtime" in msg:
            return
        if "formats have been skipped" in msg:
            return
        if "check the logs" in msg:
            return
        # Print other warnings
        print(f"[YTDL Warning] {msg}")

    def error(self, msg):
        print(f"[YTDL Error] {msg}")

# --- MUSIC BOT SETTINGS ---
ffmpeg_opts = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'noplaylist': True,
    'quiet': True,
    'no_warnings': True,
    'logger': YTDLLogger(), # Inject custom logger
    'extractor_args': {
        'youtube': {
            'player_client': ['default'] # Forces stable client (removes 'web_safari' warnings)
        }
    }
}