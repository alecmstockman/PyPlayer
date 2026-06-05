from src.models.track import Track
from src.api.lrclib import fetch_lyrics_from_lrclib
from src.models.lyrics import TrackLyrics
from src.database.lyrics_db import save_lyrics_to_lyrics_db


def fetch_lyrics(track: Track) -> TrackLyrics:

    lyric_data = fetch_lyrics_from_lrclib(track)

    track_lyrics = TrackLyrics(track.track_id)

    track_lyrics.lyrics_id = lyric_data["id"]
    track_lyrics.track_name = lyric_data["trackName"]
    track_lyrics.artist_name = lyric_data["artistName"]
    track_lyrics.album_name = lyric_data["albumName"]
    track_lyrics.duration = lyric_data["duration"]
    track_lyrics.instrumental = lyric_data["instrumental"]
    track_lyrics.plain_lyrics = lyric_data["plainLyrics"]
    track_lyrics.synced_lyrics = lyric_data["syncedLyrics"]

    save_lyrics_to_lyrics_db(track_lyrics)

    return track_lyrics



def parse_lyrics(lyric_data):
    pass