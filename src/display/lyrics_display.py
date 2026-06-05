import tkinter as tk
from tkinter import ttk


class LyricsDisplay(ttk.frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent