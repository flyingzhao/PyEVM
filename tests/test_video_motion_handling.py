import os

import pytest

from python_eulerian_video_magnification.cli import main

sample = os.path.join(os.getcwd(), 'tests', 'videos', 'guitar1sec.mp4')


def test_process_video(tmp_path):
    main([sample, '-o %s' % tmp_path])
    assert 0
