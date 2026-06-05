import sqlite3
from pathlib import Path


DB_PATH = Path("data/pyplayer.db")

def connect_to_sqlite():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)

    try:
        conn = sqlite3.connect(DB_PATH)
        conn.execute("PRAGMA foreign_keys = ON")
        return conn
    except sqlite3.Error as e:
        print(f"Unable to connect to sqlite3: {e}")
        return None

def init_playlists_db():
    conn = connect_to_sqlite()
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
        return True
    
    except sqlite3.Error as e:
        print(f"Unable to create playlists db: {e}")
        conn.close()
        return False

def init_playlist_tracks_db():
    conn = connect_to_sqlite()
    cursor = conn.cursor()

    try:
        cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS playlist_tracks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            playlist_id TEXT NOT NULL,
            track_id TEXT NOT NULL,
            tree_id TEXT,
            track_position INTEGER,
                       
            FOREIGN KEY (playlist_id) 
                REFERENCES playlists(playlist_id)
                ON DELETE CASCADE,
            FOREIGN KEY (track_id) 
                REFERENCES library(track_id)
                ON DELETE CASCADE
        )
        """)
        conn.commit()
        conn.close()
        return True
    
    except sqlite3.Error as e:
        print(f"Unable to create playlist_tracks db: {e}")
        conn.close()
        return False


def create_playlist_in_playlists(playlist_id: str, playlist_name: str):
    conn = connect_to_sqlite()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT OR IGNORE INTO playlists (
                playlist_id,
                name
            ) 
            VALUES (?, ?)             
            """, (
            playlist_id,
            playlist_name
        ))
        conn.commit()
        conn.close()
        return True
    
    except sqlite3.Error as e:
        print(f"Unable to create playlist: {playlist_name}: {e}")
        conn.close()
        return False

def delete_playlist_from_playlists(playlist_id: str):
    conn = connect_to_sqlite()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            DELETE FROM playlists
            WHERE playlist_id = ?
        """, (
            playlist_id,
        ))
        conn.commit()
        conn.close()
        return True
    
    except sqlite3.Error as e:
        print(f"Unable to delete {playlist_id} from playlist db")
        conn.close()
        return False
    
def delete_all_playlists():
    conn = connect_to_sqlite()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            DELETE FROM playlists
        """)
        conn.commit()
        conn.close()
        return True
    
    except sqlite3.Error as e:
        print(f"Unable to delete all playlists")
        conn.close()
        return False
    
def get_all_from_playlists():
    conn = connect_to_sqlite()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    try:
        cursor.execute("""
            SELECT *
            FROM playlists
        """)
        rows = cursor.fetchall()
        conn.close()
        return rows
  
    except sqlite3.Error as e:
        print(f"Unable to get all playlists from playlists db: {e}")
        conn.close()
        return None

def add_track_to_playlist_tracks(track_id: str, playlist_id: str, tree_id: str | None = None):
    conn = connect_to_sqlite()
    cursor = conn.cursor()
    
    try:
        cursor.execute("""
            INSERT INTO playlist_tracks (
                playlist_id,
                track_id,
                tree_id,
                track_position
            ) VALUES (
                ?, ?, ?, ?
            )
        """, (
            playlist_id,
            track_id,
            tree_id,
            None
        ))
        conn.commit()
        conn.close()
        return True
    
    except sqlite3.Error as e:
        print(f"Unable to add {track_id} to {playlist_id}: {e}")
        conn.close()
        return False
    
def delete_track_from_playlist(track_id: str, tree_id: str ,playlist_id: str):
    conn = connect_to_sqlite()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            DELETE FROM playlist_tracks
            WHERE tree_id = ?
            AND playlist_id = ?
        """, (
            tree_id, 
            playlist_id
        ))
        conn.commit()
        conn.close()
        return True
    
    except sqlite3.Error as e:
        print(f"Unable to delete from playlist tracks: {e}")
        conn.close()
        return False

def get_playlist_tracks_from_playlist_tracks(playlist_id: str):
    conn = connect_to_sqlite()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    try:
        cursor.execute("""
            SELECT *
            FROM playlist_tracks
            WHERE playlist_id = ?
        """, (
            playlist_id, 
        ))
        
        rows = cursor.fetchall()
        conn.close()
        return rows
        
    except sqlite3.Error as e:
        print(f"Unable to get tracks from {playlist_id}: {e}")
        conn.close()
        return False

