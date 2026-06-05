from src.models.track import Track
from src.api.lrclib import fetch_lyrics_from_lrclib


def fetch_lyrics(track: Track):



    lyric_data = fetch_lyrics_from_lrclib(track)