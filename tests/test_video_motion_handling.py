import os
from datetime import datetime

from python_eulerian_video_magnification.cli import main
from python_eulerian_video_magnification.metadata import MetaData

sample = os.path.join(os.getcwd(), 'tests', 'videos', 'guitar1sec.mp4')


def test_process_video(tmp_path, capsys, monkeypatch):
    monkeypatch.setattr(MetaData, "get_date", lambda: datetime(year=2020, month=1, day=1, hour=16, minute=16, second=16, microsecond=1))
    main([sample, '-o', str(tmp_path)])

    captured = capsys.readouterr()

    assert "Starting Magnification in Color Mode" in captured.out
    assert os.path.isfile(MetaData.output_file_name(filename=sample, suffix="color", path=tmp_path))
