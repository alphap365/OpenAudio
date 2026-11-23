from opentunes.core.spotify import SpotifyExtractor


def test_parse_embed_track_filters_missing_artist_names():
    playlist = SpotifyExtractor._parse_embed_track(
        {
            "name": "Track",
            "artists": [
                {"name": None},
                None,
                {"name": "Lead Artist"},
            ],
        },
        "https://open.spotify.com/track/example",
    )

    assert playlist.author == "Lead Artist"
    assert playlist.tracks[0].artists == ["Lead Artist"]


def test_parse_embed_track_uses_subtitle_or_unknown_artist_fallback():
    subtitle_playlist = SpotifyExtractor._parse_embed_track(
        {"name": "Track", "artists": [], "subtitle": "Subtitle Artist"},
        "https://open.spotify.com/track/example",
    )
    unknown_playlist = SpotifyExtractor._parse_embed_track(
        {"name": "Track", "artists": []},
        "https://open.spotify.com/track/example",
    )

    assert subtitle_playlist.author == "Subtitle Artist"
    assert unknown_playlist.author == "Unknown Artist"
