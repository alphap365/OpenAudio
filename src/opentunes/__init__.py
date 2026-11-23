
__version__ = "1.0.2"

from .core.config import get_download_options, load_config, save_config
from .main import main, normalize_quality, parse_args
from .ui.cli import execute_download, run_diagnostics
from .ui.tui import run_interactive_tui
from .utils.formatting import (
    clean_artist_name,
    format_bytes,
    format_duration,
    pad_number,
    sanitize_filename,
)
from .utils.system import (
    check_internet_connection,
    get_default_music_dir,
    get_ffmpeg_install_instructions,
    get_ffmpeg_path,
    get_platform_name,
    is_ffmpeg_available,
    is_narrow_screen,
    is_termux,
)

__all__ = [
    "__version__",
    "check_internet_connection",
    "clean_artist_name",
    "execute_download",
    "format_bytes",
    "format_duration",
    "get_default_music_dir",
    "get_download_options",
    "get_ffmpeg_install_instructions",
    "get_ffmpeg_path",
    "get_platform_name",
    "is_ffmpeg_available",
    "is_narrow_screen",
    "is_termux",
    "load_config",
    "main",
    "normalize_quality",
    "pad_number",
    "parse_args",
    "run_diagnostics",
    "run_interactive_tui",
    "sanitize_filename",
    "save_config",
]
