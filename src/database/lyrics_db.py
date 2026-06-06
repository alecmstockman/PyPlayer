import sqlite3
from pathlib import Path
from ..models.track import Track
from ..models.lyrics import TrackLyrics

DB_PATH = Path("data/pyplayer.db")

def init_lyrics_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    try: 
        cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS lyrics (
            track_id TEXT PRIMARY KEY,
            id INTEGER,
            track_name TEXT,
            artist_name TEXT,
            album_name TEXT,
            duration INTEGER,
            instrumental,
            plain_lyrics TEXT,
            synced_lyrics TEXT,
                       
            FOREIGN KEY (track_id)
                REFERENCES library(track_id)
        )
        """)
        conn.commit()
        conn.close()
        return True
    
    except sqlite3.Error as e:
        print(f"Unable to create lyrics db: {e}")
        conn.close()
        return False
    
def save_lyrics_to_lyrics_db(lyrics: TrackLyrics):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT OR REPLACE INTO lyrics (
                track_id,
                id,
                track_name,
                artist_name,
                album_name,
                duration,
                instrumental,
                plain_lyrics,
                synced_lyrics
            )
            VALUES (
                ?, ?, ?, 
                ?, ?, ?,
                ?, ?, ?
            )""", (
                lyrics.track_id,
                lyrics.id,
                lyrics.track_name,
                lyrics.artist_name,
                lyrics.album_name,
                lyrics.duration,
                lyrics.instrumental,
                lyrics.plain_lyrics,
                lyrics.synced_lyrics
        ))
        conn.commit()
        conn.close()
        return True
    
    except sqlite3.Error as e:
        print(f"Unable to save {lyrics.track_name} to lyrics db: {e}")
        conn.close()
        return False
    
def get_lyrics_from_lyrics_db(track_id: str) -> TrackLyrics:
    print("\nLYRICS_DB: GET LYRICS FROM LYRICS DB")
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    try:
        cursor.execute(f"""
            SELECT *
            FROM lyrics
            WHERE track_id = ?
        """, (
            track_id, 
        ))

        row = cursor.fetchone()
        conn.close()

        if row is None:
            return None
        
        lyrics_data = dict(row)
        track_lyrics = TrackLyrics(lyrics_data["track_id"])

        track_lyrics.id = lyrics_data["id"]
        track_lyrics.track_name = lyrics_data["track_name"]
        track_lyrics.artist_name = lyrics_data["artist_name"]
        track_lyrics.album_name = lyrics_data["album_name"]
        track_lyrics.duration = lyrics_data["duration"]
        track_lyrics.instrumental = lyrics_data["instrumental"]
        track_lyrics.plain_lyrics = lyrics_data["plain_lyrics"]
        track_lyrics.synced_lyrics = lyrics_data["synced_lyrics"]

        return track_lyrics
    
    except sqlite3.Error as e:
        print(f"Unable to get track: {track_id}: {e}")
        conn.close()
        return None
    
def delete_all_from_lyrics_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    try:
        cursor.execute("""
            DELETE
            FROM lyrics
        """)
        conn.commit()
        conn.close()
        return True

    except sqlite3.Error as e:
        print("Unable to delete all from lyrics db: {e}")
        conn.close
        return False