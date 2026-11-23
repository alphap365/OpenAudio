# Components

This page maps the source package to its primary responsibilities. Paths are relative to `src/opentunes`.

| Component | Responsibility |
|---|---|
| `main.py` | CLI argument parsing, quality normalization, and application-mode selection |
| `core/config.py` | Configuration persistence and creation of `DownloadOptions` |
| `core/models.py` | `TrackMetadata`, `PlaylistInfo`, `DownloadOptions`, `DownloadProgress`, and `TrackStatus` |
| `core/pipeline.py` | Resolve inputs and process tracks end to end |
| `core/spotify.py` | Spotify URL parsing and playlist, album, artist, and track metadata extraction |
| `core/youtube.py` | YouTube URL parsing and video or playlist metadata extraction |
| `core/matcher.py` | Find and rank YouTube audio candidates for a track |
| `core/downloader.py` | Download and convert audio with yt-dlp |
| `core/lyrics.py` | Fetch lyrics and write synced `.lrc` files |
| `core/tagger.py` | Write audio metadata, artwork, and lyrics for supported formats |
| `core/sequencer.py` | Build output folders and filenames |
| `ui/cli.py` | Terminal diagnostics and download orchestration |
| `ui/mobile.py` | Compact prompt-based interface for narrow terminals and Termux |
| `ui/progress.py` | Shared download status and progress presentation |
| `ui/tui.py` | Full-screen Textual application |
| `utils/formatting.py` | Filename sanitization and display formatting |
| `utils/system.py` | Platform detection, FFmpeg checks, network checks, and default music-directory selection |

## Main data objects

- `PlaylistInfo` groups the source metadata and tracks for a single input.
- `TrackMetadata` carries identifying information used for matching, download, and tagging.
- `DownloadOptions` contains output format, quality, folder, lyrics, and concurrency settings.
- `DownloadProgress` reports a track's current status and output path to the UI.

The package-root functions are listed in the [Python API guide](python-api.md).
