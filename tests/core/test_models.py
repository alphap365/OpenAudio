from openaudio.core.models import TrackMetadata


def test_track_metadata_derives_artist_fields(track_metadata):
    assert track_metadata.artist_str == "Lead Artist, Guest"
    assert track_metadata.primary_artist == "Lead Artist"
    assert track_metadata.album_artist == "Lead Artist"


def test_track_metadata_uses_unknown_artist_when_artists_are_missing():
    track = TrackMetadata(title="Track")

    assert track.artist_str == "Unknown Artist"
    assert track.primary_artist == "Unknown Artist"


def test_download_options_build_mp3_quality_arguments(download_options):
    download_options.format = "mp3"
    download_options.bitrate = "192"

    assert download_options.get_audio_quality_args() == [
        "-c:a",
        "libmp3lame",
        "-b:a",
        "192k",
    ]
