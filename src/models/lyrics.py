

class TrackLyrics():
    def __init__(self, track_id):
        self.track_id = track_id

        self.lyrics_id = None
        self.track_name = None
        self.artist_name = None
        self.album_name = None
        self.duration = None
        self.instrumental = None
        self.plain_lyrics = None
        self.synced_lyrics = None

    def __str__(self):
        return f"TrackLyrics Obj: track_id: {self.track_id}, track_name: {self.track_name}, lyrics_id: {self.lyrics_id}"
