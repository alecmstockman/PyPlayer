import tkinter as tk
from tkinter import ttk, filedialog
from pathlib import Path
import json
from src.config import BACKGROUND_COLORS, FONT_COLORS, FONTS
from mutagen import File


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
            return
        
        try: 
            with SETTINGS_JSON.open("r", encoding="utf-8") as f:
                data = json.load(f)
                self.selected_background_color = data["background"]
                self.selected_font_color = data["font_color"]
                self.font_selection = data["font_selection"]

        except Exception as e:
            print(f"Failed to load settings: {e}")


class WriteMetaDataWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.filepath = "None"
        self.audio_file = None
        self.edit_entry = None
        self.entries = {}
        
        self.withdraw()
        self.minsize(700, 500)
        self.transient(parent)   
        self.grab_set()          
        self.focus_force()

        self.title("MP3 Meta-Data Writer")

        self.select_filepath = ttk.Button(self, text="Select Filepath", command=self.select_filepath, takefocus=0, width=10)
        self.select_filepath.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.save_meta_data = ttk.Button(self, text="Save Data", command=self.save_meta_data, takefocus=0, width=10)
        self.save_meta_data.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        self.filepath_label = ttk.Label(self, text="Filepath")
        self.filepath_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        
        self.center_over_parent(parent)
        self.deiconify()
        self.lift()
        self.grab_set()

    def select_filepath(self):
        print("SELECT FILEPATH")
        filepath = filedialog.askopenfilename(
            title = "Select audio file"
        )

        path = Path(filepath)

        if path.suffix != ".mp3":
            print(f"Invalid file type: {path.suffix}")
            return

        self.filepath = filepath
        self.filepath_label = ttk.Label(self, text=self.filepath).grid(row=1, column=1, padx=10, pady=10, sticky="w")
        
        if not filepath:
            self.filepath_label = ttk.Label(self, text="invalid file").grid(row=1, column=1, padx=10, pady=10, sticky="w")
            return

        self.audio_file = File(filepath, easy=True)
        self.set_fields_and_data()
        return self.audio_file
    
    def save_meta_data(self):
        updated_data = self.collect_metadata_entries()
        print("Updated data:")
        print(updated_data)

        track = File(self.filepath, easy=True)

        for key, value in updated_data.items():
            if value == "n/a":
                updated_data[key] = ""

        track["album"] = [updated_data["album"]]
        track["composer"] = [updated_data["composer"]]
        track["copyright"] = [updated_data["copyright"]]
        track["title"] = [updated_data["title"]]
        track["artist"] = [updated_data["artist"]]
        track["albumartist"] = [updated_data["album_artist"]]
        track["conductor"] = [updated_data["conductor"]]
        track["discnumber"] = [updated_data["disc_number"]]
        track["tracknumber"] = [updated_data["track_number"]]
        track["genre"] = [updated_data["genre"]]
        track["date"] = [updated_data["date"]]

        track.save()

    def set_fields_and_data(self, close_entry=False):
        tags = self.audio_file.tags
        print("tags")
        print(tags)

        fields = ["album", "composer", "copyright", "title", "artist", "albumartist", "conductor", "disc_number", "track_number", "genre", "date"]
        self.entries = {}

        for row, field in enumerate(fields): 
            ttk.Label(self, text=field.title()).grid(row=row+2, column=0, sticky="w", padx=8, pady=8)
            entry = ttk.Entry(self, width=40)
            entry.grid(row=row+2, column=1, sticky="ew")

            current_value = tags.get(field, ["n/a"])
            if isinstance(current_value, list):
                entry.insert(0, current_value[0])
            else:
                entry.insert(0, current_value)

            self.entries[field] = entry
        
        self.columnconfigure(2, weight=1)

        if close_entry:
            self.entry.destroy()
            self.edit_entry=None

    def collect_metadata_entries(self):
        new_values = {}

        for field, entry in self.entries.items():
            new_values[field] = entry.get()

        return new_values

    def on_tree_click(self, event):
        row_id = self.meta_data_display.identify_row(event.y)
        col_id = self.meta_data_display.identify_column(event.x)
        
        print("click")
        print("row_id: ", row_id, "col_id: ", col_id)

        if not row_id:
            return
        
        # fields = ["album", "composer", "copyright", "title", "artist", "album artist", "conductor", "disc_number", "track_number", "genre", "date"]

    def on_tree_right_click(self, event):
        print("ON TREE RIGHT CLICK")

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

        x = parent_x + (parent_w // 2) - (win_w // 2) - 180
        y = parent_y + (parent_h // 2) - (win_h // 2) -  180

        self.geometry(f"{win_w}x{win_h}+{x}+{y}")
        self.lift()
        self.focus_force()


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

        self.settings_button = ttk.Button(self, text="Edit File Metadata", command=self.open_write_meta_data, takefocus=0, width=15)
        self.settings_button.grid(row=3, column=0, padx=10, pady=10, sticky="w")

        self.settings_button = ttk.Button(self, text="Rescan Library", command=self.open_write_meta_data, takefocus=0, width=15)
        self.settings_button.grid(row=4, column=0, padx=10, pady=10, sticky="w")
        
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

        font_color_label = ttk.Label(self, text="COMING SOON!").grid(row=1, column=3, padx=10, pady=10, sticky="w")
        font_type_label = ttk.Label(self, text="COMING SOON!").grid(row=2, column=3, padx=10, pady=10, sticky="w")
        library_rescan_label = ttk.Label(self, text="COMING SOON!").grid(row=4, column=3, padx=10, pady=10, sticky="w")

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

    def open_write_meta_data(self):
        meta_data_window = WriteMetaDataWindow(self.parent)
        print("\n open write meta data")

    def rescan_library(self):
        print("rescan library")

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


class SettingsButton(ttk.Frame):
    def __init__(self, parent, settings):
        super().__init__(parent)
        self.settings_button = ttk.Button(self, text="⚙️", command=self.open_settings, takefocus=0, width=3)
        self.settings_button.pack(padx=(5), pady=5)
        self.settings = settings
        self.settings_window = None

    def open_settings(self):
        self.settings_window = SettingsWindow(self, self.settings)


