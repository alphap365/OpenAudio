import pytest

from openaudio.core import config
from openaudio.core.models import DownloadOptions, TrackMetadata


@pytest.fixture
def config_file(tmp_path, monkeypatch):
    config_dir = tmp_path / "config"
    config_dir.mkdir()
    config_file = config_dir / "config.json"
    monkeypatch.setattr(config, "CONFIG_DIR", config_dir)
    monkeypatch.setattr(config, "CONFIG_FILE", config_file)
    return config_file


@pytest.fixture
def track_metadata():
    return TrackMetadata(title="Track", artists=["Lead Artist", "Guest"])


@pytest.fixture
def download_options(tmp_path):
    return DownloadOptions(output_dir=tmp_path)
