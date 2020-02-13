
import pytest

from python_eulerian_video_magnification.cli import main


def test_main_as_smoke_test_wrong_filename():
    """This tests the setup of main for wrong input file only as a smoke test, as I'm not testing arparse"""
    with pytest.raises(SystemExit) as e:
        main(['fu.bar'])
    assert "2" in str(e.value)
