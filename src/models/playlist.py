import tkinter as tk
from tkinter import ttk
import uuid
from src.database.playlists_db import (
    create_playlist_in_playlists,
    add_track_to_playlist_tracks,
    get_all_from_playlists,
    get_playlist_tracks_from_playlist_tracks,
    delete_playlist_from_playlists
)


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

    