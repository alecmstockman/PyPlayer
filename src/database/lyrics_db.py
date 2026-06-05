import sqlite3
from pathlib import Path
from ..models.track import Track

DB_PATH = Path("data/pyplayer.db")

def init_lyrics_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    try: 
        cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS lyrics (
            track_id TEXT PRIMARY KEY,
            lyrics_id INTEGER,
            track_name TEXT,
            album_name TEXT,
            duration INTEGER,
            plain_lyrics TEXT,
            synced_lyrics TEXT
        )
        """)

        conn.commit()
        conn.close()
        return True
    except sqlite3.Error as e:
        print(f"Unable to create lyrics db: {e}")
        conn.close()
        return False