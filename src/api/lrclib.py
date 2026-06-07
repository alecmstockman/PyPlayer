import requests
import json
from src.models.track import Track


def fetch_lyrics_from_lrclib_cached(track: Track) -> dict | None:
    base_url = "https://lrclib.net"

    track_name = track.title.strip().replace(' ', '+')
    artist_name = track.artist.strip().replace(' ', '+')
    album_name = track.album.strip().replace(' ', '+')
    duration = track.length
    
    cached = f"/api/get-cached?artist_name={artist_name}&track_name={track_name}&album_name={album_name}&duration={duration}"

    cached_response = requests.get(base_url + cached)
    
    if 199 < cached_response.status_code < 300:
        data = cached_response.json()
        return data
    
    return None

def fetch_lyrics_from_lrclib(track: Track) -> dict | None:
    base_url = "https://lrclib.net"

    track_name = track.title.strip().replace(' ', '+')
    artist_name = track.artist.strip().replace(' ', '+')
    album_name = track.album.strip().replace(' ', '+')
    duration = track.length

    query = f"/api/get?artist_name={artist_name}&track_name={track_name}&album_name={album_name}&duration={duration}"

    response = requests.get(base_url + query)

    if 199 < response.status_code < 300:
        data = response.json()
        return data
    
    return None