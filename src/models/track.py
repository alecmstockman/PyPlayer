

class Track:
    def __init__(self, track_id=None, title=None, artist=None, album=None, length=None, play_count=None, favorite=None, **metadata):
        self.track_id = track_id
        self.title = title
        self.artist = artist
        self.album = album
        self.length = length

        self.play_count = play_count
        self.favorite = favorite

        for key, value in metadata.items():
            setattr(self, key, value)

    def __repr__(self):
        return (
            f"Track("
            f"title={self.title!r}, "
            f"artist={self.artist!r}, "
            f"album={self.album!r}"
            f")"
        )
    
    def __str__(self):
        return (f"TITLE: {self.title}, ARTIST: {self.artist}, ALBUM: {self.album}, ID: {self.track_id}")
    
    def __eq__(self, other):
        return self.filepath == other.filepath