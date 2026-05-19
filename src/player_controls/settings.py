import tkinter as tk
from tkinter import ttk


class SettingsMenu(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.settings_button = ttk.Button(self, text="⚙️", command=self.open_settings, takefocus=0, width=3)
        # self.settings_button.grid(row=0, column=1, padx=(5, 0))
        # self.settings_button.place(relx=1.0, x=-5, y=5, anchor="ne")
        self.settings_button.pack(padx=(5), pady=5)

        # self.center_over_parent(parent)


    def open_settings(self):
        print("OPEN SETTINGS")
        
    def center_over_parent(self, parent):
        parent.update_idletasks()
        self.update_idletasks()

        parent_x = parent.winfo_rootx()
        parent_y = parent.winfo_rooty()
        parent_w = parent.winfo_width()
        parent_h = parent.winfo_height()

        win_w = self.winfo_reqwidth()
        win_h = self.winfo_reqheight()

        x = parent_x + (parent_w // 2) - (win_w // 2) - 100
        y = parent_y + (parent_h // 2) - (win_h // 2) - 200

        self.geometry(f"{win_w}x{win_h}+{x}+{y}")
        self.lift()
        self.focus_force()