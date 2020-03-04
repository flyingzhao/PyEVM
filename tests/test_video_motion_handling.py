import os

from python_eulerian_video_magnification.cli import main
from python_eulerian_video_magnification.metadata import MetaData

sample = os.path.join(os.getcwd(), 'tests', 'videos', 'guitar1sec.mp4')


def test_process_video(tmp_path, capsys, monkeypatch):
    monkeypatch.setattr(MetaData, "get_date", lambda: "2020-01-01-16:16:16")
    main([sample, '-o', str(tmp_path)])

    captured = capsys.readouterr()

    assert "Starting Magnification in Color Mode" in captured.out
    assert os.path.isfile(MetaData.output_file_name(filename=sample, suffix="color", path=tmp_path))
