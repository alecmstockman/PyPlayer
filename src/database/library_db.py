import sqlite3
from pathlib import Path
from ..models.track import Track

DB_PATH = Path("data/pyplayer.db")

def init_library_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    try:
        cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS library (
            track_id TEXT PRIMARY KEY,
            filepath TEXT UNIQUE,
            title TEXT,
            artist TEXT,
            album TEXT,
            length INTEGER,
                       
            play_count INTEGER,
            favorite BOOLEAN,
                    
            composer TEXT,
            copyright TEXT,
            albumartist TEXT,
            conductor TEXT,
            discnumber TEXT,
            tracknumber TEXT,
            genre TEXT,
            date TEXT,
            
            sample_rate INTEGER,
            bit_rate INTEGER,
            channels INTEGER,
            codec TEXT
        )
        """)

        conn.commit()
        conn.close()
        return True
    
    except sqlite3.Error as e:
        print(f"Unable to create library db: {e}")
        conn.close()
        return False

def save_track_to_library_db(track: Track):
    print(f"SAVE TRACK TO LIBRARY")
    print(track)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO library (
                track_id,
                filepath,
                title,
                artist,
                album,
                length,
                       
                play_count,
                favorite,

                composer,
                copyright,
                albumartist,
                conductor,
                discnumber,
                tracknumber,
                genre,
                date,

                sample_rate,
                bit_rate,
                channels,
                codec
            )
            VALUES (
                ?, ?, ?, ?, ?, 
                ?, ?, ?, ?, ?, 
                ?, ?, ?, ?, ?, 
                ?, ?, ?, ?, ?
            )
            """, (
                track.track_id,
                track.filepath,
                track.title,
                track.artist,
                track.album,
                track.length,

                track.play_count,
                track.favorite,

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
        return True

    except sqlite3.Error as e:
        print(f"Unable to save track {track.title} to library:", e)
        conn.close()
        return False

def update_track_favorite(track_id: str, favorite: bool):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    try:
        cursor.execute("""
            UPDATE library
            SET favorite = ?
            WHERE track_id = ?
        """, (
            favorite, track_id
        ))

        conn.commit()
        conn.close()
        return True
    
    except sqlite3.Error as e:
        print(f"Unable to update favorite to {favorite} for {track_id}", e)
        conn.close()
        return False
    
def get_track_from_library_db(track_id: str):
    if not isinstance(track_id, str):
        return ValueError("_get_track_from_library_db only accepts track_id as a string")

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    try:
        cursor.execute("""
            SELECT * 
            FROM library
            WHERE track_id = ?
            
        """, (str(track_id), ))

        row = cursor.fetchone()
        conn.close()

        if row is None:
            return None
        
        track = Track(**dict(row))
        return track
    
    except sqlite3.Error as e:
        conn.close()
        print(f"Unable to get track from library: {e}")
        return False

def remove_track_from_library_db(track_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    try: 
        cursor.execute("""
            DELETE *
            FROM library
            WHERE track_id = ?
        """, (track_id, )
        )
        conn.commit()
        conn.close()
        return True
    
    except sqlite3.Error as e:
        print(f"Unable to remove track {track_id}: {e}")
        conn.close()
        return False
    
def get_all_tracks_from_library():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    try:
        cursor.execute("""
            SELECT *
            FROM library
        """)
        rows = cursor.fetchall()
        conn.close()
        return rows
    
    except sqlite3.Error as e:
        print(f"Unable to get all tracks: {e}")
        conn.close()
        return False
    
def delete_all_tracks_from_library():
    print("\nDelete all tracks from library")
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    try: 
        cursor.execute("DELETE FROM playlist_tracks;")
        cursor.execute("DELETE FROM playlists;")
        cursor.execute("DELETE FROM library;")

        conn.commit()
        conn.close()
        return True
    
    except sqlite3.Error as e:
        print(f"Unable to delete all track from library: {e}")
        conn.close()
        return False

