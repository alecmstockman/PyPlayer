import tkinter as tk
from tkinter import ttk
from pathlib import Path
import random

class TrackInfo(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        container = ttk.Frame(self, padding=12)
        container.pack(fill = "both", expand = True)
        
        self.info_tree = ttk.Treeview(
            self,
            columns=("field", "data"),
            show="headings"
        )
        self.info_tree.pack(sid="left", fill="both", expand=True)
