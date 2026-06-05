import requests
import json
from src.models.track import Track



def fetch_lyrics_from_lrclib(track: Track) -> dict | None:
    print("DISPLAY: FETCH LYRICS FROM LRCLIB")

    base_url = "https://lrclib.net"

    track_name = track.title
    artist_name = track.artist
    album_name = track.album
    duration = track.length

    query = f"/api/get?artist_name={artist_name}&track_name={track_name}&album_name={album_name}&duration={duration}"


    response = requests.get(base_url + query)

    if response.status_code == 200:
        data = response.json()
        return data
    
    return None