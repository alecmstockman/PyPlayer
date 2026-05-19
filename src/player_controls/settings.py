import tkinter as tk
from tkinter import ttk


class SettingsWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.withdraw()
        self.minsize(500, 450)
        self.transient(parent)   
        self.grab_set()          
        self.focus_force()


        ttk.Label(self, text="settings").pack(anchor="w")

        self.info_tree = ttk.Treeview(
            self,

            columns=("field", "data"),
            show="headings"
        )

        self.info_tree.column("field", width=100, anchor="w")
        self.info_tree.column("data", width=400, anchor="w")

        self.info_tree.heading("field", text="Field")
        self.info_tree.heading("data", text="Value")

        self.info_tree.pack(fill="both", expand=True)
        

        self.center_over_parent(parent)
        self.deiconify()
        self.lift()
        self.grab_set()

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
        y = parent_y + (parent_h // 2) - (win_h // 2) - 200

        self.geometry(f"{win_w}x{win_h}+{x}+{y}")
        self.lift()
        self.focus_force()


class SettingsButton(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.settings_button = ttk.Button(self, text="⚙️", command=self.open_settings, takefocus=0, width=3)
        self.settings_button.pack(padx=(5), pady=5)

    def open_settings(self):
        self.settings_window = SettingsWindow(self)
        print("OPEN SETTINGS")


