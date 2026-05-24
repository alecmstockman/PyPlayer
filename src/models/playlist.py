import tkinter as tk
from tkinter import ttk
from pathlib import Path
import json
import uuid
from ..config import AUDIO_FILETYPES
from src.metadata.metadata import load_track_metadata
from src.database.library_db import (
    init_library_db,
    save_track_to_library_db, 
    get_track_from_library_db, 
    remove_track_from_library_db,
    get_all_tracks_from_library
)
from src.database.playlists_db import (
    create_playlist_in_playlists,
    add_track_to_playlist_tracks,
    get_all_from_playlists,
    get_playlist_tracks_from_playlist_tracks,
    delete_playlist_from_playlists
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
        print("\n------- LOAD LIBRARY --------")
        tracks = get_all_tracks_from_library()

        if not tracks:
            self.create_library()
            print("not tracks creating library")
        try:
            for row in tracks:
                track_data = {}
                for key in row.keys():
                    track_data[key] = row[key]
                track = Track(**track_data)
                self.tracks[track.track_id] = track

                # print(f"title: {track.title}, artist: {track.artist}, genre: {track.genre} sample rate: {track.sample_rate}")
                # print()
        except: 
            print("CREATE LIBRARY EXCEPTION:")
            self.create_library()
        # except Exception as e:
        #     raise Exception("Unable to load library")
            




        # if not LIBRARY_JSON_PATH.exists():
        #     print("Library json file not found, creating new library")
        #     self.create_library()
        #     return
        
        # try: 
        #     with LIBRARY_JSON_PATH.open("r", encoding="utf-8") as f:
        #         data = json.load(f)

        #         for track_id, track_data in data.items():
        #             track = Track(**track_data)
        #             track_id = str(track_id)
        #             track.track_id = str(track_id)
        #             self.tracks[track_id] = track

        # except Exception as e:
        #     print(f"Failed to load library: {e}")    

    def add_track(self, track):
        self.tracks[track.track_id] = track

    def add_track_to_library_db(self, track):
        save_track_to_library_db(track)
        return track

    def remove_track(seslf, track_id):
        return
 
    def remove_track_from_library_db(self, track_id):
        try: 
            remove_track_from_library_db(track_id)
        except Exception as e:
            print("Unable to remove track:", e)

    def get_track(self, track_id):
        return self.tracks[track_id]
    
    def get_track_from_library_db(self, track_id):
        return get_track_from_library_db(track_id)
    
    def get_track_length(self, track_id):
        return self.tracks[track_id].length

    # def save_library_to_json(self):
    #     print("SAVE LIBRARY TO JSON")
    #     # print("not functioning")
    #     # return
    #     library = {}
    #     for track in self.tracks.values():
    #         library[track.track_id] = {
    #             key: str(value) if key == "filepath" else value
    #             for key, value in vars(track).items()
    #         }

    #     try: 
    #         with LIBRARY_JSON_PATH.open("w", encoding="utf-8") as f:
    #             json.dump(library, f , indent=2)
    #     except Exception as e:
    #         print(f"Failed to save library: {e}")
        

    def save_library_to_library_db(self):
        print("SAVE LIBRARY TO LIBRARY DB")
        library = {}
        for track in self.tracks.values():
            library[track.track_id] = {
                key: str(value) if key == "filepath" else value 
                for key, value in vars(track).items()
            }

        try:
            print("saving to library database")
            for track_id in self.tracks.keys():
                save_track_to_library_db(self.tracks[track_id])
        except Exception as e:
            print(f"Failed to save library to database: {e}")


class Playlist():
    def __init__(self, name, track_id_list=None, song_id=None):
        self.id = song_id if song_id is not None else uuid.uuid4()
        self.name = name
        self.track_id_list = track_id_list

    def __repr__(self):
        return f"PLAYLIST NAME: {self.name}, ID: {self.id}"
    
    def __str__(self):
        return f"PLAYLIST NAME: {self.name}, ID: {self.id}"

class PlaylistManager():
    def __init__(self, library):
        self.library = library
        self.library_playlist = None
        self.user_playlists = {}
        self.id = uuid.uuid4()
        self.favorites_playlist = Playlist("Favorites", [])

    def create_library_playlist(self):
        library_track_list = []
        for item in self.library.tracks.keys():
            library_track_list.append(item)
        self.library_playlist = Playlist("Library Playlist", library_track_list)

    def create_playlist(self, name, tracks=None):
        print(f"\nCREATE PLAYLIST: {name}")
        if tracks == None:
            playlist = Playlist(name, [])
        else:
            playlist = Playlist(name, tracks)

        playlist.id = str(uuid.uuid4())
        create_playlist_in_playlists(playlist.id, name)

        self.user_playlists[playlist.id] = playlist
        return playlist

    def save_playlists(self):
        user_playlists = {}
        print("\nSAVE PLAYLISTS")
        for key, value in self.user_playlists.items():
            create_playlist_in_playlists(key, value.name)
            print(f"key: {key}\nvalue: {value}")
            print(value.name)
            track_list = []
            for track in value.track_id_list:
                try:
                    res = add_track_to_playlist_tracks(track, key)
                    print(f"succesfully added track {track} ", res)
                except Exception as e:
                    print("Unable to save due to ", e)
                
                track_list.append(str(track))
            user_playlists[key] = {"name": value.name, "tracks": track_list, "id": key}

    def update_favorites_playlist(self):
        self.favorites_playlist.track_id_list = []

        for _, value in self.library.tracks.items():
            if value.favorite == True:
                self.favorites_playlist.track_id_list.append(value.track_id)

    def load_playlist(self):
        self.user_playlist = {}

        rows = get_all_from_playlists()
        for row in rows:
            playlist_id = row["playlist_id"]
            name = row["name"]

            track_rows = get_playlist_tracks_from_playlist_tracks(playlist_id)
            track_list = []

            for row in track_rows:
                track_list.append(row["track_id"])

            self.user_playlists[playlist_id] = Playlist(name, track_list, playlist_id)
        
        # for playlist in user_playlists.items():
        #     print(playlist)
            

        # path = Path("data/playlists.json")

        # if not path.exists():
        #     self.user_playlists = {}
        #     return
        # try: 
        #     with path.open("r", encoding="utf-8") as f:
        #         user_playlists = json.load(f)
        #         print("\n--- user playlists from json ---")
        #         print(user_playlists)
        # except Exception as e:
        #     print(f"Failed to load playlist: {e}")
        #     self.user_playlists = {}

        # for key, value in user_playlists.items():
        #     print(f"key: {key}\nvalue: {value}")
        #     track_id_list = []
        #     track_list = value["tracks"]
        #     for track in track_list:
        #         track_id_list.append(track)
        #     self.user_playlists[key] = Playlist(value["name"], track_id_list, key)
    
    def add_to_user_playlist(self, playlist_id, track_id):
        print("\nADD TO USER PLAYLIST")
        print(f"playlist_id: {playlist_id}, track_id: {track_id}")
        playlist = self.user_playlists[playlist_id]
        playlist.track_id_list.append(track_id)
        res = add_track_to_playlist_tracks(track_id, playlist_id)
        print("res: ", res)
        # self.save_playlists()

    def update_user_playlist(self, playlist_id):
        playlist = self.user_playlists[playlist_id]
        self.save_playlists()

    def delete_user_playlist(self, playlist_id):
        print("\nDELETE USER PLAYLIST")
        res = delete_playlist_from_playlists(playlist_id)
        print(f"res: {res}")

        remaining_user_playlists = {}
        for key, playlist in self.user_playlists.items():
            if key != playlist_id:
                remaining_user_playlists[key] = playlist

        self.user_playlists = remaining_user_playlists
        self.save_playlists()


class CreatePlaylistEntry(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.withdraw()
        self.title("Create Playlist")
        self.result = None
        self.transient(parent)

        container = ttk.Frame(self, padding=12)
        container.pack(fill="both", expand=True)
        ttk.Label(container, text="Playlist Name:").pack(anchor="w")

        self.entry = ttk.Entry(container, width=30)
        self.entry.pack(fill="x", pady=(4, 10))
        self.entry.focus()

        btn_row = ttk.Frame(container)
        btn_row.pack(fill="x")
        ttk.Button(btn_row, text="Cancel", command=self.destroy).pack(side="right")
        ttk.Button(btn_row, text="Create", command=self.on_create).pack(side="right", padx=(0, 6))

        self.bind("<Return>", self.on_create)
        self.center_over_parent(parent)
        self.wait_visibility()
        self.deiconify()
        self.lift()
        self.grab_set()


    def center_over_parent(self, parent):
        root = parent.winfo_toplevel()
        self.update_idletasks()
        root.update_idletasks()

        root_x = root.winfo_rootx()
        root_y = root.winfo_rooty()
        root_w = root.winfo_width()
        root_h = root.winfo_height()

        win_w = self.winfo_reqwidth()
        win_h = self.winfo_reqheight()

        x = root_x + (root_w - win_w) // 2
        y = root_y - 100 + (root_h - win_h) // 2

        self.geometry(f"{win_w}x{win_h}+{x}+{y}")
        self.deiconify()
        self.lift()
        self.entry.focus_set()

    def on_create(self, event=None):
        name = self.entry.get().strip()
        if name:
            self.result = name
        self.destroy()

    