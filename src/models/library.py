from pathlib import Path
from ..config import AUDIO_FILETYPES
from src.metadata.metadata import load_track_metadata
from src.database.library_db import (
    init_library_db,
    save_track_to_library_db, 
    get_track_from_library_db, 
    remove_track_from_library_db,
    get_all_tracks_from_library,
    update_track_favorite,
    delete_all_tracks_from_library
)
from src.models.track import Track


ROOT = Path(__file__).resolve().parent.parent.parent
MUSIC = Path(f"{ROOT}/Music/")
LIBRARY_JSON_PATH = Path(ROOT/"data/library.json")
LIBRARY_JSON_PATH.parent.mkdir(exist_ok=True)

class Library():
    def __init__(self):
        self.name = "Library"
        self.tracks = {}

    def __str__(self):
        return str(self.tracks)

    def create_library(self):
        init_library_db()

        filename_list = [filename for filename in MUSIC.rglob('*') if filename.suffix in AUDIO_FILETYPES]

        all_tracks = []
        
        for name in filename_list:
            track_data = load_track_metadata(name)
            track = Track(**track_data)
            all_tracks.append(track)

        for track in all_tracks:
            self.tracks[track.track_id] = track

        self.save_library_to_library_db()

    def load_library(self):
        tracks = get_all_tracks_from_library()
        if not tracks:
            print("No tracks creating library")
            self.create_library()
            
        try:
            for row in tracks:
                track_data = {}
                for key in row.keys():
                    track_data[key] = row[key]
                track = Track(**track_data)
                self.tracks[track.track_id] = track
        except: 
            self.create_library()

    def delete_all_tracks(self):
        delete_all_tracks_from_library()
              

    def add_track(self, track):
        self.tracks[track.track_id] = track

    # def add_track_to_library_db(self, track):
    #     save_track_to_library_db(track)
    #     return track
    
    def save_track_to_library_db(self, track):
        save_track_to_library_db(track)
        return track

    def remove_track(seslf, track_id):
        return
 
    def remove_track_from_library_db(self, track_id):
        print("remove track from library db")
        print("track_id: ", track_id )
        try: 
            remove_track_from_library_db(str(track_id))
            del self.tracks[track_id]
            
        except Exception as e:
            print("Unable to remove track:", e)


    def get_track(self, track_id):
        return self.tracks[track_id]
    
    def get_track_from_library_db(self, track_id):
        return get_track_from_library_db(track_id)
    
    def get_track_length(self, track_id):
        return self.tracks[track_id].length        

    def save_library_to_library_db(self):
        library = {}

        for track in self.tracks.values():
            library[track.track_id] = {
                key: str(value) if key == "filepath" else value 
                for key, value in vars(track).items()
            }

        try:
            for track_id in self.tracks.keys():
                save_track_to_library_db(self.tracks[track_id])
        except Exception as e:
            print(f"Failed to save library to database: {e}")

    def update_track_favorite(self, track_id: str, favorite: bool):
        return update_track_favorite(track_id, favorite)

