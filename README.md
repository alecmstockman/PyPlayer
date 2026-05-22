# PyPlayer

PyPlayer is a desktop music player and library manager built with Python, Tkinter, and VLC. It supports playlist management, metadata editing, sorting, favorites, shuffle/loop playback, and dynamic library organization through a custom GUI application architecture.

![Python](https://img.shields.io/badge/python-3.x-blue)
![Tkinter](https://img.shields.io/badge/gui-tkinter-green)
![VLC](https://img.shields.io/badge/player-VLC-orange?logo=vlcmediaplayer)
![Mutagen](https://img.shields.io/badge/metadata-Mutagen-purple)
![SQLite](https://img.shields.io/badge/database-SQLite-07405E?logo=sqlite&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-lightgrey)


## Motivation

As a lifelong musician, I’ve always struggled to organize my demo tracks, song drafts, and finished recordings in a way that keeps them separate from my main music library. I was also looking for a way to add metadata to song files on my finished tracks. Coincidentally, I’ve also been learning programming, and I thought—what better way to practice and clean up my demo littered desktop than by creating my own music player and file editor? And, after many a difficult hour, PyPlayer was born!

#### Challenges:

Like most personal projects, I vastly underestimated the amount of work involved in building a custom music player from scratch. I ran into several significant challenges like deciding how to handle audio playback, implementing shuffle for the current view, and learning Tkinter, but by far the biggest was managing play state across different menus. There were countless small edge cases to solve to keep song display, playlist display, and backend play order in sync as users switched tracks and navigated between libraries and playlists. The core functionality is now fully built out, but I have many more updates on the way. I’d love to hear what you think!

This is a music player app similar to Apple Music and VLC media player but with additional file editing features, and a personal project for the Boot.dev backend engineering course.

See my Boot.dev profile and other projects here: [https://www.boot.dev/u/stockman]


## Screenshots

<img width="1511" height="944" alt="Screenshot 2026-05-21 at 9 44 55 PM" src="https://github.com/user-attachments/assets/545cb000-0b55-448f-9a40-27b8c77eee61" />
<br><br>
<img width="450" height="300" alt="Screenshot 2026-03-24 at 10 18 21 PM" src="https://github.com/user-attachments/assets/8209f64c-e864-4293-a8b2-12afb53924b0" />

<img width="450" height="300" alt="Screenshot 2026-03-24 at 10 19 10 PM" src="https://github.com/user-attachments/assets/1a4f5847-a4ed-4b9a-aa97-6c4c61c86cb0" />
<br><br>
<img width="450" height="300" alt="Screenshot 2026-05-21 at 9 49 03 PM" src="https://github.com/user-attachments/assets/0ad62c37-0b1f-478f-b3c4-8668a016a1b7" />

<img width="450" height="300" alt="Screenshot 2026-03-24 at 10 19 49 PM" src="https://github.com/user-attachments/assets/3f710618-cdb2-49db-a519-146cc724614a" />



## Built With
* Python
* Tkinter / ttk
* python-vlc
* Mutagen
* JSON persistence
* pathlib

## Quick Start

- **Space** : Play / Pause  
- **Cmd + →** : Next Track  
- **Cmd + ←** : Previous Track  
- **Cmd + ↑ / ↓** : Volume

## Features
- Audio playback using VLC bindings
- Playlist management
- Sortable music library
- Metadata editing with Mutagen
- Shuffle and loop playback modes
- Favorites system
- Keyboard shortcuts
- Dynamic progress bar and scrubbing
- Album/artist metadata support
- Custom Tkinter/ttk UI architecture
- JSON-based library persistence

# Usage

### 1. Clone the repository

```bash
git clone https://github.com/alecmstockman/music-player.git
cd music-player
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
```

### 3. Activate the virtual environment

macOS / Linux:

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

You must also have **VLC installed** on your system since playback is handled through the VLC engine.

---

# Running the App

Start the application with:

```bash
python3 main.py
```

---

# Running the App

Add audio files to root/music in either the 'Albums' or 'Songs' folder.

---
# Architecture

```
.
├── data
│   ├── library.db
│   ├── library.json
│   ├── playlists.db
│   ├── playlists.json
│   └── settings.json
├── main.py
├── Music
│   ├── Albums
│   │   ├── Muri Album
│   │   └── Test Album
│   └── Songs
├── README.md
├── requirements.txt
└── src
    ├── __init__.py
    ├── config.py
    ├── database
    │   └── database.py
    ├── display
    │   ├── playlist_display.py
    │   └── sidebar.py
    ├── metadata
    │   └── metadata.py
    ├── models
    │   ├── playlist.py
    │   └── track.py
    ├── player_controls
    │   ├── player_controls.py
    │   ├── right_controls.py
    │   ├── settings.py
    │   └── track_display.py
    ├── styles.py
    ├── track_info.py
    └── vlc_player.py             
```

---

# Current Features

- Playlist view using **Tkinter Treeview**
- Sortable columns
- Favorite tracks
- Playlist creation
- Edit metadata on MP3 files
- Context menu actions
- VLC-based audio playback
- Sidebar library navigation
- Change the background color theme

---

## Controls

### Playback

| Key | Action |
|----|----|
| `Space` | Play / Pause |
| `Cmd + →` | Next Track |
| `Cmd + ←` | Previous Track |

### Volume

| Key | Action |
|----|----|
| `Cmd + ↑` | Volume Up |
| `Cmd + ↓` | Volume Down |

### Playlist

| Key | Action |
|----|----|
| `Click Row` | Select Track |
| `Click ⋯` | Open Track Menu |
| `Click ★` | Toggle Favorite |

### Sidebar

| Action | Result |
|----|----|
| Click Playlist | Load playlist |
| Right Click Playlist | Open playlist menu |

### Mouse Actions

| Action | Result |
|----|----|
| Click Column Header | Sort by column |
| Right Click Track | Track options menu |

---

# Notes

Music files are **not stored in the repository**.  
Place your music files inside:

```
Music/Songs/
Music/Albums/
```

The project uses `.gitkeep` files so these directories exist even when empty.

## Planned Features
* Updates to controls, hotkeys, and right clicks
* Add artwork Display
* Update UI with CustomTkinter
* Create popup play queue and history display
* Implement a play counts column
* Ability to change theme and styles
* Recently Played Playlist


## 🤝 Contributing

### 1. Clone the repository

```bash
git clone https://github.com/alecmstockman/music-player.git
cd music-player

python -m venv venv
source venv/bin/activate

pip install -r requirements.txt
python main.py
```


### Submit a pull request

If you'd like to contribute, please fork the repository and open a pull request to the `main` branch.




    
