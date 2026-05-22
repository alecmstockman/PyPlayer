import sqlite3
from pathlib import Path

DB_PATH = Path("data/library.db")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS library_db (
        track_id INTEGER PRIMARY KEY,
        filepath TEXT,
        title TEXT,
        artist TEXT,
        album TEXT,
        length INTEGER,
                   
        composer TEXT,
        copyright TEXT,
        albumartist TEXT,
        conductor TEXT,
        discnumber INTEGER,
        tracknumber INTEGER,
        genre TEXT,
        date STRING,
        
        samplerate INTEGER,
        bitrate INTEGER,
        channels INTEGER,
        codec TEXT,
    )
    """)