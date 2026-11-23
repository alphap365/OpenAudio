import json

from opentunes.core import config


def test_load_config_merges_saved_values_with_defaults(config_file):
    config_file.write_text(json.dumps({"format": "flac"}), encoding="utf-8")

    loaded = config.load_config()

    assert loaded["format"] == "flac"
    assert loaded["fetch_lyrics"] == config.DEFAULT_CONFIG["fetch_lyrics"]


def test_get_download_options_applies_overrides_and_clamps_concurrency(
    tmp_path, monkeypatch
):
    monkeypatch.setattr(
        config,
        "load_config",
        lambda: {
            **config.DEFAULT_CONFIG,
            "output_dir": str(tmp_path),
            "concurrent_downloads": 2,
        },
    )

    options = config.get_download_options(
        {"format": "flac", "concurrent_downloads": 99}
    )

    assert options.format == "flac"
    assert options.output_dir == tmp_path
    assert options.concurrent_downloads == 5
