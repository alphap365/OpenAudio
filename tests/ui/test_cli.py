from openaudio.core.models import DownloadOptions
from openaudio.ui import cli


class StubDownloadUI:
    def __init__(self, is_mobile=False):
        self.error = None

    def display_error_popup(self, title, message, hint=None):
        self.error = (title, message, hint)


def test_execute_download_reports_missing_ffmpeg(monkeypatch):
    ui = StubDownloadUI()
    monkeypatch.setattr(cli, "DownloadUI", lambda is_mobile=False: ui)
    monkeypatch.setattr(cli, "MobileUI", lambda: object())
    monkeypatch.setattr(cli, "is_ffmpeg_available", lambda: False)
    monkeypatch.setattr(cli, "get_ffmpeg_install_instructions", lambda: "install ffmpeg")

    result = cli.execute_download("track", DownloadOptions(), mobile=True)

    assert result == 1
    assert ui.error == (
        "FFmpeg Missing",
        "FFmpeg is required to convert and encode audio files.",
        "Install FFmpeg using: install ffmpeg",
    )
