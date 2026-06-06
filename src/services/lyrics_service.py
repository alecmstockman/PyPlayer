from src.models.track import Track
from src.api.lrclib import fetch_lyrics_from_lrclib, fetch_lyrics_from_lrclib_cached
from src.models.lyrics import TrackLyrics
from src.database.lyrics_db import save_lyrics_to_lyrics_db, get_lyrics_from_lyrics_db, delete_all_from_lyrics_db


def fetch_lyrics_from_db(track: Track) -> TrackLyrics | None:
    print("\nFETCH LYRICS FROM DB")
    lyric_data = get_lyrics_from_lyrics_db(track.track_id)
    if lyric_data:
        print("successfully fetched from db!")
    return lyric_data

def fetch_lyrics(track: Track) -> TrackLyrics:
    print("\nFETCH LYRICS")

    lyric_data = fetch_lyrics_from_lrclib_cached(track)
        
    if lyric_data is None:
        lyric_data = fetch_lyrics_from_lrclib(track)

    if lyric_data is None:
        print(f"Unable to get lyrics for {track.title}")
        return None
    print(f"lyrics_data: {lyric_data}")

    track_lyrics = TrackLyrics(track.track_id)

    track_lyrics.id = lyric_data["id"] if lyric_data["id"] else None
    track_lyrics.track_name = lyric_data["trackName"]
    track_lyrics.artist_name = lyric_data["artistName"]
    track_lyrics.album_name = lyric_data["albumName"]
    track_lyrics.duration = lyric_data["duration"]
    track_lyrics.instrumental = lyric_data["instrumental"]
    track_lyrics.plain_lyrics = lyric_data["plainLyrics"]
    track_lyrics.synced_lyrics = lyric_data["syncedLyrics"]

    saved = save_lyrics_to_lyrics_db(track_lyrics)
    print(f"Saved lyrics to db: {saved}")

    return track_lyrics



def parse_lyrics(lyric_data):
    pass

def delete_all_cached_lyrics():
    delete_all_from_lyrics_db()