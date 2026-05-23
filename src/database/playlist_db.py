import sqlite3
from pathlib import Path
import uuid


PLAYLISTS_DB_PATH = Path("data/playlists.db")

def init_playlists_db():
    conn = sqlite3.connect(PLAYLISTS_DB_PATH)
    cursor = conn.cursor()

    try:
        cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS playlists (
            playlist_id TEXT PRIMARY KEY,
            name TEXT
        )
        """)
        conn.commit()
        conn.close()
    except sqlite3.IntegrityError:
        print("Unable to create playlists db")
        conn.close()

PLAYLIST_TRACKS_DB_PATH = Path("data/playlists_tracks.db")

def init_playlist_tracks_db():
    print("init playlist db")
    conn = sqlite3.connect(PLAYLIST_TRACKS_DB_PATH)
    cursor = conn.cursor()

    try:
        cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS playlist_tracks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            playlist_id TEXT NOT NULL,
            track_id TEXT NOT NULL,
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


def create_playlist_in_playlists_db(playlist_id: str, playlist_name: str):
    print(f"creating playlist: {playlist_name}")
    conn = sqlite3.connect(PLAYLISTS_DB_PATH)
    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO playlists (
                playlist_id,
                name
            ) 
            VALUES (?, ?)             
            """, (
            playlist_id,
            playlist_name
        ))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        print(f"Unable to create playlist: {playlist_name}")
        conn.close()
        return False

def add_track_to_playlist_tracks(track_id: str, playlist_id: str):
    conn = sqlite3.connect(PLAYLIST_TRACKS_DB_PATH)
    cursor = conn.cursor()
    
    try:
        cursor.execute("""
        INSERT INTO playlists_tracks (
            playlist_id,
            track_id,
            track_position
        ) VALUES (
            ?, ?, ?
        )
        """, (
            playlist_id,
            track_id,
            None
        ))
        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError:
        print(f"Unable to add {track_id} to {playlist_id}")
        conn.close()
        return False

def get_playlist_tracks_from_playlists_tracks_db(playlist_id: str):
    conn = sqlite3.connect(PLAYLIST_TRACKS_DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    try:
        cursor.execute("""
            SELECT *
            FROM playlist_tracks
            WHERE playlist_id = ?
        """, (playlist_id))
        
        row = cursor.fetchone()
        conn.close()

        if row is None:
            return None
        
        return row
        
    except sqlite3.IntegrityError:
        print(f"Unable to get tracks from {playlist_id}")
        conn.close()
        return False


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