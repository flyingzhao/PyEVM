
import pytest

from python_eulerian_video_magnification.cli import main


def test_main_as_smoke_test_wrong_filename(capsys):
    """This tests the setup of main for wrong input file only as a smoke test, as I'm not testing arparse"""
    with pytest.raises(SystemExit) as e:
        main(['fu.bar'])

    captured = capsys.readouterr()

    assert "No such file or directory: 'fu.bar'" in captured.err
    assert 2 == e.value.code
