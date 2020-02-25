import pytest

from python_eulerian_video_magnification.cli import main


def test_process_video():
    main(['videos/guitar1sec.mp4'])
