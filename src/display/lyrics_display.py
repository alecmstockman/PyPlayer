import tkinter as tk
from tkinter import ttk
from src.api.lrclib import fetch_lyrics_from_lrclib
from src.models.lyrics import TrackLyrics



class LyricsWindow(tk.Toplevel):
    def __init__(self, parent, track_lyrics: TrackLyrics):
        super().__init__(parent)
        self.parent = parent
        self.track_lyrics = track_lyrics

        self.withdraw()
        self.minsize(600, 700)
        self.transient(parent)
        self.focus_force()

        self.title("Lyrics")

        self.lyrics_text = tk.Text(self, wrap="word", font=("Trebuchet MS", 14))
        self.lyrics_text.pack(fill="both", expand="True", padx=5, pady=5)

        self.center_over_parent(parent)
        self.deiconify()
        self.lift()
        self.grab_set()

        self.display_plain_lyrics(self.track_lyrics.plain_lyrics)

    def display_plain_lyrics(self, plain_lyrics):
        print("\nWINDOW: DISPLAY LYRICS")
        self.lyrics_text.config(padx=20, pady=10)
        self.lyrics_text.config(state="normal")
        self.lyrics_text.delete("1.10", tk.END)
        self.lyrics_text.insert("1.10", plain_lyrics)
        self.lyrics_text.config(state="disabled")

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

        x = parent_x + (parent_w // 2) - (win_w // 2) 
        y = parent_y + (parent_h // 2) - (win_h // 2) - 100

        self.geometry(f"{win_w}x{win_h}+{x}+{y}")
        self.lift()
        self.focus_force()

