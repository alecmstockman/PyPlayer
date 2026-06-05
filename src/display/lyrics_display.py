import tkinter as tk
from tkinter import ttk
from src.api.lrclib import fetch_lyrics_from_lrclib



class LyricsWindow(tk.Toplevel):
    def __init__(self, parent, library, track):
        super().__init__(parent)
        self.parent = parent
        self.library = library
        self.track = track

        self.withdraw()
        self.minsize(600, 800)
        self.transient(parent)
        self.focus_force()

        self.title("Lyrics")

        lyrics_plain_text = tk.Text(self, wrap="word")


        self.center_over_parent(parent)
        self.deiconify()
        self.lift()
        self.grab_set()

        self.fetch_lyrics()

    def fetch_lyrics(self):
        print("LYRICS WINDOW: FETCH LYRICS")
        lyrics_json = fetch_lyrics_from_lrclib(self.track)
        # print("lyrics_json:\n", lyrics_json)
        
        lrc_track_data = Lyrics()
        print("\n\n")
        print(lyrics_json["id"])
        print(lyrics_json["trackName"])
        print(lyrics_json["artistName"])
        print(lyrics_json["duration"])
        print(lyrics_json["instrumental"])
        print(lyrics_json["plainLyrics"])

        

    def parse_lyrics(self, lyrics):
        split = lyrics.split("\n\n")



    def center_over_parent(self, parent):
        parent = parent.winfo_toplevel()
        parent.update_idletasks()
        self.update_idletasks()

        parent_x = parent.winfo_rootx()
        parent_y = parent.winfo_rooty()
        parent_w = parent.winfo_width()
        parent_h = parent.winfo_height()

        win_w = self.winfo_reqwidth()
        win_h = self.winfo_reqheight()

        x = parent_x + (parent_w // 2) - (win_w // 2) - 50
        y = parent_y + (parent_h // 2) - (win_h // 2) - 200

        self.geometry(f"{win_w}x{win_h}+{x}+{y}")
        self.lift()
        self.focus_force()

