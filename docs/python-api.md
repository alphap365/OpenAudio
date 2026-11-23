# Python API

OpenTunes supports Python 3.13 and newer. From a checkout, sync the project environment with uv:

```sh
uv sync
```

Run Python code in that environment with `uv run python your_script.py`.

## Package-level functions

The package root re-exports its public functions and lists them in `opentunes.__all__`.

```python
from opentunes import (
    __version__,
    get_download_options,
    sanitize_filename,
)

print(__version__)
options = get_download_options({"output_dir": "~/Music"})
filename = sanitize_filename("Artist / Track")
```

The exports are grouped by purpose:

- **Application and CLI:** `main`, `parse_args`, `normalize_quality`, `execute_download`, `run_diagnostics`, `run_interactive_tui`
- **Configuration:** `load_config`, `save_config`, `get_download_options`
- **Formatting:** `sanitize_filename`, `clean_artist_name`, `format_duration`, `format_bytes`, `pad_number`
- **Platform and environment:** `is_termux`, `get_platform_name`, `is_ffmpeg_available`, `get_ffmpeg_path`, `get_ffmpeg_install_instructions`, `get_default_music_dir`, `check_internet_connection`, `is_narrow_screen`

For example, `main()` runs the same command-line application as the `opentunes` executable. It may terminate the process with `SystemExit`, as normal command-line entry points do.

## Download pipeline

Lower-level download models and orchestration are available from their modules:

```python
from opentunes import get_download_options
from opentunes.core.pipeline import DownloadPipeline

playlist = DownloadPipeline.resolve_input(
    "https://www.youtube.com/watch?v=VIDEO_ID"
)
options = get_download_options({"output_dir": "~/Music"})

for index, track in enumerate(playlist.tracks, start=1):
    DownloadPipeline.process_track(
        track,
        options,
        folder_name=playlist.title,
        total_tracks=len(playlist.tracks),
        index=index,
    )
```

`resolve_input` accepts Spotify and YouTube URLs, as well as a search query. `process_track` returns the destination `Path` and can report progress through its optional callback. For model types such as `DownloadOptions`, `TrackMetadata`, and `PlaylistInfo`, import from `opentunes.core.models`.

The CLI and lower-level modules share implementation details; importing these functions does not imply a stability guarantee beyond the current package API.
