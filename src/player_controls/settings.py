import tkinter as tk
from tkinter import ttk
from pathlib import Path
import json
from src.config import BACKGROUND_COLORS, FONT_COLORS, FONTS


ROOT = Path(__file__).resolve().parent.parent.parent
SETTINGS_JSON = Path(f"{ROOT}/data/settings.json")

class Settings():
    def __init__(self):
        self.user = ""
        self.selected_background_color = "" 
        self.selected_font_color = ""
        self.font_selection = ""

    def load_settings(self):
        if not SETTINGS_JSON.exists():
            print("Settings json file not found, creating new settings.json")
            print("*** make create_settings_JSON function")
            return
        
        try: 
            with SETTINGS_JSON.open("r", encoding="utf-8") as f:
                data = json.load(f)
                self.selected_background_color = data["background"]
                self.selected_font_color = data["font_color"]
                self.font_selection = data["font_selection"]

        except Exception as e:
            print(f"Failed to load settings: {e}")  
        

class SettingsWindow(tk.Toplevel):
    def __init__(self, parent, settings):
        super().__init__(parent)
        self.parent = parent
        self.settings = settings

        self.withdraw()
        self.minsize(500, 450)
        self.transient(parent)   
        self.grab_set()          
        self.focus_force()

        self.title("Settings")

        self.selected_background_color = tk.StringVar(value="#064C15")
        self.selected_font_color = tk.StringVar(value="#ECECEC")
        self.fonts = tk.StringVar(value="trebuchet MS")

        ttk.Label(self, text="Background").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        ttk.Label(self, text="Font Color").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        ttk.Label(self, text="Font Selection").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        ttk.Label(self, text="Rescan Library").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        
        background_color_dropdown = ttk.Combobox(
            self,
            textvariable=self.selected_background_color,
            values=BACKGROUND_COLORS,
            state="readonly",
            width=12,
        )
    
        background_color_dropdown.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        background_color_dropdown.bind("<<ComboboxSelected>>", self.on_background_selected)
        
        font_color_dropdown = ttk.Combobox(
            self,
            textvariable=self.selected_font_color,
            values=FONT_COLORS,
            state="readonly",
            width=12,
        )
        
        font_color_dropdown.grid(row=1, column=1, padx=10, pady=10, sticky="ew")
        font_color_dropdown.bind("<<ComboboxSelected>>", self.on_font_color_selected)
        
        font = ttk.Combobox(
            self,
            textvariable=self.fonts,
            values=FONTS,
            state="readonly",
            width=12,
        )

        font.grid(row=2, column=1, padx=10, pady=10, sticky="ew")
        font.bind("<<ComboboxSelected>>", self.on_font_selection)

        self.center_over_parent(parent)
        self.deiconify()
        self.lift()
        self.grab_set()

    def on_background_selected(self, event=None):
        self.settings.selected_background_color = self.selected_background_color.get()
        self.parent.event_generate("<<SettingsChanged>>")
        self.save_settings()

    def on_font_color_selected(self, event=None):
        self.settings.selected_font_color = self.selected_font_color.get()
        self.save_settings()

    def on_font_selection(self, event=None):
        self.save_settings()

    def save_settings(self):
        settings_JSON = {
            "background": self.settings.selected_background_color,
            "font_color": self.settings.selected_font_color,
            "font_selection": self.settings.font_selection
        }
        try: 
            with SETTINGS_JSON.open("w", encoding="utf-8") as f:
                json.dump(settings_JSON, f , indent=4)
        except Exception as e:
            print(f"Failed to save settings: {e}")

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

        x = parent_x + (parent_w // 2) - (win_w // 2) - 100
        y = parent_y + (parent_h // 2) - (win_h // 2) - 250

        self.geometry(f"{win_w}x{win_h}+{x}+{y}")
        self.lift()
        self.focus_force()


class SettingsButton(ttk.Frame):
    def __init__(self, parent, settings):
        super().__init__(parent)
        self.settings_button = ttk.Button(self, text="⚙️", command=self.open_settings, takefocus=0, width=3)
        self.settings_button.pack(padx=(5), pady=5)
        self.settings = settings
        self.settings_window = None

    def open_settings(self):
        self.settings_window = SettingsWindow(self, self.settings)
        # if self.settings_window is None or not self.settings_window.winfo_exists():
        #     self.settings_window = SettingsWindow(self, self.settings)
        # else:
        #     self.settings_window.close_settings_window()
        #     self.settings_window = None


