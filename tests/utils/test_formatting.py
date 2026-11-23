from openaudio.utils.formatting import (
    clean_artist_name,
    format_bytes,
    format_duration,
    pad_number,
    sanitize_filename,
)


def test_sanitize_filename_replaces_invalid_characters_and_reserved_names():
    assert sanitize_filename("Artist/Track: Live") == "Artist_Track_ Live"
    assert sanitize_filename("CON") == "CON_track"


def test_format_duration_handles_hour_boundary_and_invalid_values():
    assert format_duration(3599) == "59:59"
    assert format_duration(3600) == "01:00:00"
    assert format_duration(-1) == "00:00"


def test_format_bytes_scales_to_kilobytes():
    assert format_bytes(1536) == "1.5 KB"
    assert format_bytes(0) == "0 B"


def test_clean_artist_name_removes_channel_suffixes():
    assert clean_artist_name("Artist - Topic") == "Artist"
    assert clean_artist_name("Artist VEVO") == "Artist"


def test_pad_number_expands_for_large_collections():
    assert pad_number(7, 12) == "007"
    assert pad_number(7, 1000) == "0007"
