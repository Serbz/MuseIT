import sqlite3
import os
import json
import numpy # Still needed for legacy list conversion in load_playlist
import config

DB_PATH = os.path.join(config.HomeDir, 'Saves', 'Databases', 'museit.db')

def init_db():
    """
    Initializes the database and all required tables.
    Also creates all necessary directories for the bot.
    """
    # 1. Create all directories
    os.makedirs(os.path.join(config.HomeDir, 'Saves', 'Databases'), exist_ok=True)
    os.makedirs(os.path.join(config.HomeDir, 'Saves', 'YTMP3'), exist_ok=True)
    os.makedirs(os.path.join(config.HomeDir, 'Saves', 'ImageGeneration'), exist_ok=True)
    os.makedirs(os.path.join(config.HomeDir, 'Saves', 'Sneks'), exist_ok=True)
    os.makedirs(os.path.join(config.HomeDir, 'fonts'), exist_ok=True)
    os.makedirs(os.path.join(config.HomeDir, 'AutoHotkey'), exist_ok=True)

    # 2. Create database connection
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()

        # 3. Create tables
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS prefixes (
            guild_id TEXT PRIMARY KEY,
            prefix TEXT NOT NULL
        )''')
        
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS video_cache (
            video_id TEXT PRIMARY KEY,
            title TEXT,
            duration INTEGER,
            clip_url TEXT
        )''')
        
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS spotify_cache (
            search_query TEXT PRIMARY KEY,
            video_id TEXT,
            title TEXT,
            duration INTEGER,
            clip_url TEXT
        )''')
        
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS playlists (
            user_id TEXT NOT NULL,
            playlist_name TEXT NOT NULL,
            songs TEXT NOT NULL,
            PRIMARY KEY (user_id, playlist_name)
        )''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS session (
            guild_id TEXT PRIMARY KEY,
            mega_array_json TEXT
        )''')
        
        conn.commit()

# --- Prefix Functions ---

def get_all_prefixes():
    """Loads all guild prefixes from the DB."""
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT guild_id, prefix FROM prefixes")
            # Convert list of tuples [('id', 'prefix')] to list of lists [[id, prefix, None, None]]
            # to match the old serverData format
            return [[row[0], row[1], None, None] for row in cursor.fetchall()]
    except Exception as e:
        print(f"Error loading prefixes from DB: {e}")
        return []

def set_prefix(guild_id, prefix):
    """Saves or updates a guild's prefix."""
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO prefixes (guild_id, prefix)
        VALUES (?, ?)
        ON CONFLICT(guild_id) DO UPDATE SET prefix = excluded.prefix
        ''', (str(guild_id), prefix))
        conn.commit()

# --- Video Cache Functions ---

def get_video_cache(video_id):
    """Retrieves a video's data from the cache by its ID."""
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT clip_url, title, duration FROM video_cache WHERE video_id = ?", (video_id,))
        row = cursor.fetchone()
        if row:
            # Return in the format helper_utils.referenceDB expects: [clip_url, title, duration]
            return [row[0], row[1], row[2]]
        return None

def set_video_cache(video_id, clip_url, title, duration):
    """Saves video data to the cache."""
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('''
        INSERT OR IGNORE INTO video_cache (video_id, clip_url, title, duration)
        VALUES (?, ?, ?, ?)
        ''', (video_id, clip_url, title, duration))
        conn.commit()

# --- Spotify Cache Functions ---

def get_spotify_cache(search_query):
    """Retrieves a cached YouTube result for a Spotify search query."""
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT clip_url, title, duration, video_id FROM spotify_cache WHERE search_query = ?", (search_query,))
        row = cursor.fetchone()
        if row:
            # Return format: [clip_url, title, duration, video_id]
            return [row[0], row[1], row[2], row[3]]
        return None

def set_spotify_cache(search_query, clip_url, title, duration, video_id):
    """Saves a YouTube result for a Spotify search query."""
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('''
        INSERT OR IGNORE INTO spotify_cache (search_query, clip_url, title, duration, video_id)
        VALUES (?, ?, ?, ?, ?)
        ''', (search_query, clip_url, title, duration, video_id))
        conn.commit()

# --- Playlist Functions ---

def get_user_playlists(user_id):
    """Retrieves a list of all playlist names for a user."""
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT playlist_name FROM playlists WHERE user_id = ?", (str(user_id),))
        # Return a simple list of names
        return [row[0] for row in cursor.fetchall()]

def save_playlist(user_id, playlist_name, song_list):
    """Saves a user's playlist (song_list) as a JSON string."""
    songs_json = json.dumps(song_list)
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        try:
            cursor.execute('''
            INSERT INTO playlists (user_id, playlist_name, songs)
            VALUES (?, ?, ?)
            ''', (str(user_id), playlist_name, songs_json))
            conn.commit()
            return True # Success
        except sqlite3.IntegrityError:
            return False # Playlist name already exists

def load_playlist(user_id, playlist_name):
    """Loads a user's playlist from the DB."""
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT songs FROM playlists WHERE user_id = ? AND playlist_name = ?", (str(user_id), playlist_name))
        row = cursor.fetchone()
        if row:
            # The original script saved songs as a numpy array.
            # We now save as JSON. We'll try to load as JSON,
            # but fall back to numpy for old .npy files if needed.
            try:
                return json.loads(row[0])
            except json.JSONDecodeError:
                # This fallback is for converting old .npy files,
                # but new saves will be JSON.
                # In this refactor, we just load the JSON.
                print(f"Could not decode JSON for playlist {playlist_name}")
                return None 
        return None

def delete_playlist(user_id, playlist_name):
    """Deletes a user's playlist."""
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM playlists WHERE user_id = ? AND playlist_name = ?", (str(user_id), playlist_name))
        conn.commit()
        return cursor.rowcount > 0 # Return True if a row was deleted

# --- Session Functions (for megaArray) ---

def save_session(guild_id, mega_array_entry):
    """Saves a guild's megaArray state to the DB."""
    # We can't serialize discord objects, so we need a custom serializer
    def json_serializer(obj):
        if isinstance(obj, (discord.Guild, discord.TextChannel, discord.VoiceChannel, discord.VoiceClient, commands.Context, discord.Message)):
            return str(obj.id) # Just save the ID
        if isinstance(obj, numpy.ndarray):
            return obj.tolist()
        return f"<<UNSERIALIZABLE: {type(obj)}>>"

    try:
        session_json = json.dumps(mega_array_entry, default=json_serializer)
    except Exception as e:
        print(f"Error serializing session for guild {guild_id}: {e}")
        return

    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO session (guild_id, mega_array_json)
        VALUES (?, ?)
        ON CONFLICT(guild_id) DO UPDATE SET mega_array_json = excluded.mega_array_json
        ''', (str(guild_id), session_json))
        conn.commit()

def load_session(bot):
    """Loads all guild sessions from the DB and reconstructs megaArray."""
    # This is complex because we must re-fetch discord objects from IDs
    # This function will load the data, but arrayBuilder will be
    # needed to fully re-populate the state.
    
    all_sessions = {}
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT guild_id, mega_array_json FROM session")
        rows = cursor.fetchall()
    
    # Return a dictionary of {guild_id: mega_array_json}
    return {row[0]: json.loads(row[1]) for row in rows}