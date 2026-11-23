# Termux guide

OpenTunes runs as a Python command-line app in Termux. It requires Python 3.13 or newer and the system `ffmpeg` executable.

## Install

1. Update Termux and install the system packages:

   ```bash
   pkg update && pkg upgrade
   pkg install python ffmpeg git
   ```

2. Confirm that the installed Python meets the project requirement:

   ```bash
   python --version
   ```

   It must report Python 3.13 or newer.

3. Clone OpenTunes:

   ```bash
   git clone https://github.com/radiantfalcon/OpenTunes.git
   cd OpenTunes
   ```

4. Install the project. If `uv` is available in your Termux environment:

   ```bash
   uv sync
   ```

   Otherwise, create a virtual environment and install with pip:

   ```bash
   python -m venv .venv
   .venv/bin/python -m pip install --upgrade pip
   .venv/bin/python -m pip install .
   ```

5. Start the compact mobile interface:

   ```bash
   uv run opentunes --mobile
   ```

   If you installed with pip, use `.venv/bin/opentunes --mobile`.

To run a download directly, pass a URL or search query:

```bash
.venv/bin/opentunes "https://music.youtube.com/playlist?list=PLAYLIST_ID" --mobile
.venv/bin/opentunes --search "Artist Song" --mobile
```

## Shared music storage

To let OpenTunes write to shared Android storage, grant Termux storage access:

```bash
termux-setup-storage
```

Accept Android's permission prompt. OpenTunes uses a writable shared Music directory when available; otherwise its fallback is `~/Music`. You can also set `output_dir` in the OpenTunes configuration file to a directory under `~/storage/shared`.

## Troubleshooting

- If installation reports an unsupported Python version, update Termux packages and confirm that `python --version` is at least 3.13.
- If audio conversion fails, check that FFmpeg is installed with `ffmpeg -version`.
- If shared storage is unavailable, run `termux-setup-storage` again and check Termux's storage permission in Android settings.
- If a download is slow or fails, retry on a stable network and verify that the source URL is publicly accessible.
