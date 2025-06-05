# Spotify CLI Search Tool

A lightweight Python CLI that lets you quickly look up **artists** and **tracks** on Spotify and see rich, nicely-formatted information (popularity, followers, preview link, etc.).  
Perfect for small scripts, demos, or augmenting a music database with Spotify links.

---

## ✨ Features

| Command | What it does |
|---------|--------------|
| **Artist search** | Look up to 10 matching artists by name, then dive into popularity, genres, followers, and profile link. |
| **Track search**  | Find up to 10 tracks, view artist(s), album, release date, popularity, preview URL, and direct Spotify URL. |
| **Clean output**  | Pretty printing with clear dividers—easy to read or copy-paste elsewhere. |

---

## 🛠 Prerequisites

1. **Python 3.8+**
2. A free Spotify Developer account  
   *Create one at <https://developer.spotify.com> → Dashboard → “Create App”.*
3. **Client ID** and **Client Secret** from your Spotify app
4. _(Optional but recommended)_ A virtual environment (`python -m venv venv`)

---

## 📦 Installation

```bash
# 1. Clone or download this repo
git clone https://github.com/your-name/spotify-cli-search.git
cd spotify-cli-search

# 2. Create & activate a virtual environment (optional)
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# 3. Install required packages
pip install python-dotenv requests