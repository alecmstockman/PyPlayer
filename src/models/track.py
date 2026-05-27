

class Track:
    def __init__(self, track_id=None, title=None, artist=None, album=None, length=None, play_count=None, favorite=False, **metadata):
        self.track_id = track_id
        self.title = title
        self.artist = artist
        self.album = album
        self.length = length

        self.play_count = 0 if play_count == None else play_count
        self.favorite = favorite

        for key, value in metadata.items():
            setattr(self, key, value)

    def __repr__(self):
        return (f"TITLE: {self.title}, ARTIST: {self.artist}, ALBUM: {self.album}, ID: {self.track_id}, favorite: {self.favorite}")
    
    def __str__(self):
        return (f"TITLE: {self.title}, ARTIST: {self.artist}, ALBUM: {self.album}, ID: {self.track_id}, fav: {self.favorite}")
    
    def __eq__(self, other):
        return self.filepath == other.filepath