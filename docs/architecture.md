# Architecture

OpenTunes is a Python package under `src/opentunes`. The command-line entry point is declared in `pyproject.toml` and delegates to `opentunes:main`.

## Request flow

1. **Entry point and mode selection** — `main.py` parses CLI arguments and selects diagnostics, the full-screen Textual interface, the compact mobile interface, a batch, a search, or a direct download.
2. **Metadata resolution** — `core/pipeline.py` routes Spotify URLs to `SpotifyExtractor`, YouTube URLs to `YouTubeExtractor`, and plain queries to a yt-dlp search. The result is represented by `PlaylistInfo` and `TrackMetadata`.
3. **Candidate matching** — `AudioMatcher` searches for YouTube audio candidates for each track and ranks them against the source metadata.
4. **Download and output path** — `Sequencer` chooses a destination path, and `AudioDownloader` uses yt-dlp to retrieve and convert the audio.
5. **Lyrics and tags** — `LyricsFetcher` retrieves lyrics and can save synced lyrics as an `.lrc` file. `AudioTagger` embeds metadata, artwork, and available lyrics in the output.
6. **Progress and presentation** — `DownloadProgress` events are passed to the CLI, mobile, or Textual UI through callbacks.

## Supporting services

- `core/config.py` loads and saves user settings and builds `DownloadOptions`.
- `core/models.py` contains track, playlist, download-option, and progress models.
- `utils/formatting.py` handles filenames and display values.
- `utils/system.py` provides platform, storage, network, terminal-size, and FFmpeg helpers.

The UI consumes the same pipeline and models as the CLI; source resolution and track processing remain in the core modules.
