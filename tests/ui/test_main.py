import sys

from opentunes.main import normalize_quality, parse_args


def test_normalize_quality_accepts_common_aliases():
    assert normalize_quality(" 256 ") == "256k"
    assert normalize_quality("lossless") == "best"
    assert normalize_quality(None) is None


def test_parse_args_reads_search_format_and_bitrate(monkeypatch):
    monkeypatch.setattr(
        sys,
        "argv",
        ["opentunes", "--search", "Artist Song", "--format", "flac", "--quality", "192k"],
    )

    args = parse_args()

    assert args.search == "Artist Song"
    assert args.format == "flac"
    assert args.bitrate == "192k"
