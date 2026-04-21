# PyPlayer

A music library designed to play (almost) any filetype and see song metadata!

![Python](https://img.shields.io/badge/python-3.x-blue)
![Tkinter](https://img.shields.io/badge/gui-tkinter-green)
![License](https://img.shields.io/badge/license-MIT-lightgrey)


## Motivation

As a lifelong musician I have always struggled with organizing my demo tracks, working songs tests, and finished songs in a clean way that is separate from my standard music library. Coincidentally I have also been learning programming and I thought, what better way to practice programming and my desktop that is littered in demo tracks than to create my own music player? And, after many a difficult hour, PyPlayer was born!
This is a music player app similar to Apple Music or VLC player and a personal project for the Boot.dev backend engineering course. 

See my profile here: [https://www.boot.dev/u/stockman] [https://www.boot.dev/u/stockman]


## Screenshots

<img width="1505" height="766" alt="Screenshot 2026-03-24 at 10 16 38 PM" src="https://github.com/user-attachments/assets/3d3e35f4-928b-4bf9-997f-e796faec5037" />


<img width="1066" height="616" alt="Screenshot 2026-03-24 at 10 18 21 PM" src="https://github.com/user-attachments/assets/8209f64c-e864-4293-a8b2-12afb53924b0" />


<img width="715" height="455" alt="Screenshot 2026-03-24 at 10 19 10 PM" src="https://github.com/user-attachments/assets/1a4f5847-a4ed-4b9a-aa97-6c4c61c86cb0" />


<img width="715" height="620" alt="Screenshot 2026-03-24 at 10 19 49 PM" src="https://github.com/user-attachments/assets/3f710618-cdb2-49db-a519-146cc724614a" />



## Built With
  * tkinter
  * python-vlc
  * mutagen

## Quick Controls

- **Space** : Play / Pause  
- **Cmd + →** : Next Track  
- **Cmd + ←** : Previous Track  
- **Cmd + ↑ / ↓** : Volume

## Features
* Plays following audio types: .mp3, .wav, .aac, .flac, .wma, ac3
* Create, save, and delete custom user playlists
* Seamlessly change states - Shuffle, Loop Playlist, Loop Track
* Clickable progress bar allows you change playback position
* Add songs to your favorites list
* Easily see total playlist time

# Setup

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

# Project Structure

```
music-player/
│
├── main.py                # Application entry point
├── README.md
│
├── src/
│   ├── config.py
│   ├── player_controls.py
│   ├── playlist.py
│   ├── playlist_display.py
│   ├── sidebar.py
│   ├── styles.py
│   └── vlc_player.py
│
├── data/                  # JSON data files (favorites, playlists, etc.)
│
├── Music/
│   ├── Songs/
│   └── Albums/
│
└── venv/                  # Python virtual environment (ignored by git)
```

---

# Current Features

- Playlist view using **Tkinter Treeview**
- Sortable columns
- Favorite tracks
- Playlist creation
- Context menu actions
- VLC-based audio playback
- Sidebar library navigation

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
* Ability to write meta-data to song files
* Ability to change theme and styles
* Recently Played Playlist


## 🤝 Contributing

### 1. Clone the repository

```bash
git clone https://github.com/alecmstockman/music-player.git
cd music-player
```

### Submit a pull request

If you'd like to contribute, please fork the repository and open a pull request to the `main` branch.




    
