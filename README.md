<img width="828" height="294" alt="openaudio" src="docs/assets/banner.webp" />

> **Notice:** OpenAudio is based on and is a copy of the [radiantfalcon/OpenTunes](https://github.com/radiantfalcon/OpenTunes) codebase, updated and maintained for use as OpenAudio.

Open-Source Music Aggregator for Spotify, YouTube, and YouTube Music. Downloads songs, albums, and playlists with embedded cover art and lyrics. Available for Linux, Windows, MacOS and Android (Termux)

[![Python 3.13+](https://img.shields.io/badge/python-3.13%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/github/license/alphap365/openaudio)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/alphap365/openaudio?style=social)](https://github.com/alphap365/openaudio/stargazers)
[![Last commit](https://img.shields.io/github/last-commit/alphap365/openaudio)](https://github.com/alphap365/openaudio/commits/main)

---

### Documentation

- [Python API](docs/python-api.md)
- [Termux guide](docs/termux.md)
- [Architecture](docs/architecture.md)
- [Components](docs/components.md)
- [Repository script usage](docs/scripts.md)
- [Contributing](CONTRIBUTING.md)
- [Security policy](SECURITY.md)

---

### Installation

OpenAudio requires Python 3.10 or newer and FFmpeg.

Install [uv](https://docs.astral.sh/uv/getting-started/installation/) if it is not already available, then clone and sync the project:

```bash
git clone https://github.com/alphap365/openaudio.git
cd OpenAudio
uv sync
uv run openaudio
```

`uv sync` creates and manages the project environment. Prefix project commands with `uv run`; this works on Linux, macOS, and PowerShell.

#### Android (Termux)
See the [Termux guide](docs/termux.md) for installation, storage permissions, and mobile mode.

### Repository scripts

From a checkout, use `bash scripts/setup.sh` followed by `bash scripts/run.sh --help` on Linux, macOS, or Termux. On Windows, use `.\scripts\setup.bat` followed by `.\scripts\openaudio.bat --help`.

See the [script usage guide](docs/scripts.md) for the launcher and installer details.

---

### How to Use

#### 1. Interactive Mode
Run without arguments to open the interactive dashboard:
```bash
uv run openaudio
```
Key shortcuts inside the app:
- `1` : Download tab
- `2` : Live Search & Discover tab (searches live as you type)
- `3` : Settings tab (formats, bitrates, lyrics, output path)
- `Ctrl + C` : Quit

#### 2. Command Line Examples

Download a Spotify playlist:
```bash
uv run openaudio "https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M"
```

Download a Spotify album in lossless FLAC:
```bash
uv run openaudio "https://open.spotify.com/album/4m2880jivSbbyEGAKfITCa" -f flac
```

Download a YouTube / YouTube Music playlist in Opus:
```bash
uv run openaudio "https://music.youtube.com/playlist?list=PL..." -f opus -q 160k
```

Search and download a song directly by name:
```bash
uv run openaudio --search "Queen Bohemian Rhapsody"
```

Download to a custom folder:
```bash
uv run openaudio "https://open.spotify.com/track/4cOdK2wGLETKBW3PvgPWqT" -o ~/Music/Rock
```

Batch download from a text file:
```bash
uv run openaudio --batch urls.txt
```
*(urls.txt can have one Spotify link, YouTube link, or song query per line)*

Save synced lyrics as a separate `.lrc` file:
```bash
uv run openaudio "https://open.spotify.com/track/4cOdK2wGLETKBW3PvgPWqT" --lrc
```

Run in simple mobile mode (recommended on narrow terminals / Termux):
```bash
uv run openaudio --mobile
```

Check system environment and FFmpeg installation:
```bash
uv run openaudio --check
```

---

### CLI Reference

| Flag | Short | Description | Default |
|---|---|---|---|
| `url_or_query` | | Spotify/YouTube URL or song name | Launches interactive app |
| `--format` | `-f` | Audio format: `mp3`, `flac`, `opus`, `wav`, `m4a` | `mp3` |
| `--quality` | `-q` | Audio bitrate: `320k`, `256k`, `192k`, `128k`, `best` | `320k` |
| `--output` | `-o` | Destination folder for downloads | `~/Music` |
| `--lrc` | | Export synced `.lrc` lyrics file next to audio | `false` |
| `--no-lyrics` | | Skip fetching and embedding lyrics | `false` |
| `--batch` | | Path to text file with links/queries | `none` |
| `--search` | | Search query to download best match | `none` |
| `--mobile` | | Simple prompt menu for mobile Termux | Auto-detected |
| `--overwrite` | | Force overwrite existing files | `false` |
| `--interactive`| `-i` | Force full-screen TUI | `false` |
| `--check` | | Check system dependencies and FFmpeg | |
| `--version` | `-v` | Print version | |

---

### Audio Formats & Bitrates

- **MP3**: Constant bitrate (`320k`, `256k`, `192k`, `128k`) with universal ID3v2.3 tags and embedded artwork.
- **FLAC**: Lossless compression with Vorbis metadata and embedded artwork.
- **OPUS**: High-efficiency VBR audio (`160k`, `128k`, `96k`) with Vorbis comments.
- **WAV**: Uncompressed 16-bit PCM audio.
- **M4A / AAC**: AAC encoding (`256k`, `320k`) with MP4 metadata.

---

### Configuration

Settings persist across runs and are saved at:
- **Linux / Android**: `~/.config/openaudio/config.json`
- **Windows**: `%USERPROFILE%\.config\openaudio\config.json`

Example `config.json`:
```json
{
  "format": "mp3",
  "bitrate": "320k",
  "output_dir": "~/Music",
  "fetch_lyrics": true,
  "save_lrc": false,
  "embed_cover": true,
  "overwrite": false,
  "max_retries": 3,
  "rate_limit_delay": 1.2
}
```

You can also change these settings interactively through the Settings tab (`[3]`) in the desktop app or the Settings menu in mobile mode.

---

### Requirements

- **Python**: 3.13 or newer
- **FFmpeg**: Required for audio conversion and metadata embedding

Installing FFmpeg:
- **Ubuntu / Debian**: `sudo apt install ffmpeg`
- **Arch Linux**: `sudo pacman -S ffmpeg`
- **macOS**: `brew install ffmpeg`
- **Android (Termux)**: `pkg install ffmpeg`
- **Windows**: `winget install Gyan.FFmpeg`

---

### Development

Install the development dependencies with [uv](https://docs.astral.sh/uv/):
```bash
uv sync --group dev
```

Run the test suite with:
```bash
uv run pytest
```

---

### License

MIT

---

### Contributors

Contributors are updated automatically:

[![Contributors](https://contrib.rocks/image?repo=alphap365/openaudio)](https://github.com/alphap365/openaudio/graphs/contributors)
