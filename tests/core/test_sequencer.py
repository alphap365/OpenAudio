from opentunes.core.sequencer import Sequencer


def test_destination_path_sanitizes_folder_and_filename(
    track_metadata, download_options
):
    track_metadata.title = "Live/Track"

    destination = Sequencer.get_destination_path(
        track_metadata,
        download_options,
        folder_name="Album/Live",
        total_tracks=12,
        index=3,
    )

    assert destination == (
        download_options.output_dir
        / "Album_Live"
        / "003 - Live_Track - Lead Artist.mp3"
    )
    assert destination.parent.is_dir()
