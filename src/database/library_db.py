import sqlite3
from pathlib import Path
from ..models.track import Track

DB_PATH = Path("data/pyplayer.db")

def init_library_db():
    print("INIT LIBRARY DB")
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    try:
        cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS library_db (
            track_id TEXT PRIMARY KEY,
            filepath TEXT UNIQUE,
            title TEXT,
            artist TEXT,
            album TEXT,
            length INTEGER,
                    
            composer TEXT,
            copyright TEXT,
            albumartist TEXT,
            conductor TEXT,
            discnumber TEXT,
            tracknumber TEXT,
            genre TEXT,
            date TEXT,
            
            samplerate INTEGER,
            bitrate INTEGER,
            channels INTEGER,
            codec TEXT
        )
        """)

        conn.commit()
        conn.close()
    except sqlite3.IntegrityError:
        print("Unable to create library db")
        conn.close()

def save_track_to_library_db(track: Track):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO library_db (
                track_id,
                filepath,
                title,
                artist,
                album,
                length,

                composer,
                copyright,
                albumartist,
                conductor,
                discnumber,
                tracknumber,
                genre,
                date,

                samplerate,
                bitrate,
                channels,
                codec
            )
            VALUES (
                ?, ?, ?, ?, ?, ?,
                ?, ?, ?, ?, ?, ?, ?, ?,
                ?, ?, ?, ?
            )
            """, (
                track.track_id,
                track.filepath,
                track.title,
                track.artist,
                track.album,
                track.length,

                track.composer,
                track.copyright,
                track.albumartist,
                track.conductor,
                track.discnumber,
                track.tracknumber,
                track.genre,
                track.date,

                track.sample_rate,
                track.bit_rate,
                track.channels,
                track.codec,
            ))
        
        conn.commit()
        conn.close()
    except sqlite3.IntegrityError:
        # print("Track already exists")
        conn.close()
    

def get_track_from_library_db(track_id):
    print("GET TRACK FROM LIBRARY DB")
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute("""
        SELECT * 
        FROM library_db
        WHERE track_id = ?
        
    """, (track_id, ))

    row = cursor.fetchone()
    conn.close()

    if row is None:
        return None
    
    track = Track(**dict(row))

    return track

def remove_track_from_library_db(track_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        DELETE *
        FROM library_db
        WHERE track_id = ?
    """, (track_id, )
    )
    conn.close()

    print(f"{track_id} has been removed from ")