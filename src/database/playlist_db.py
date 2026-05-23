import sqlite3
from pathlib import Path
import uuid
from ..models.track import Track
from ..models.playlist import Playlist


PLAYLISTS_DB_PATH = Path("data/playlists.db")

def init_playlists_db():
    conn = sqlite3.connect(PLAYLISTS_DB_PATH)
    cursor = conn.cursor()

    try:
        cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS playlists_db (
            playlist_id TEXT PRIMARY KEY,
            name TEXT,   
        )
        """)
        conn.commit()
        conn.close()
    except sqlite3.IntegrityError:
        print("Unable to create playlists_db")
        conn.close()

PLAYLIST_TRACKS_DB_PATH = Path("data/playlists_tracks.db")

def init_playlist_tracks_db():
    print("init playlist db")
    conn = sqlite3.connect(PLAYLIST_TRACKS_DB_PATH)
    cursor = conn.cursor()

    try:
        cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS playlist_tracks_db (
            id INTEGER PRIMARY KEY,
            playlist_id TEXT NOT NULL,
            name TEXT,
            track_id TEXT,
            track_position INTEGER,
            FOREIGN KEY (playlist_id) REFERENCES playlists_db(playlist_id),
            FOREIGN KEY (track_id) REFERENCES library_db(track_id)      
        )
        """)
        conn.commit()
        conn.close()
    except sqlite3.IntegrityError:
        print("Unable to create playlist_tracks db")
        conn.close()


def create_playlist_in_playlists_db(name: str, playlist_id: str):
    print(f"creating playlist: {name}")
    conn = sqlite3.connect()
    curser = conn.cursor()

    try:
        conn.execute("""
            
        """)
        conn.commit()
        conn.close()
    except sqlite3.IntegrityError:
        print(f"Unable to create playlist: {name}")
        conn.close()


# def save_playlist_to_playlist_db(playlist: Playlist):
#     conn = sqlite3.connect(DB_PATH)
#     cursor = conn.cursor()

#     try:
#         cursor.execute("""
#             INSERT INTO playlist_db (
#             playlist_id,
#             name,
#             track_id,
#             track_position
#             )
#         """)
#         conn.commit()
#         conn.close()

#     except sqlite3.IntegrityError:
#         print("Unable to save playlist to playlist_db")
#         conn.close()