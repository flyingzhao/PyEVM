import os

import pytest

from python_eulerian_video_magnification.cli import main
from python_eulerian_video_magnification.magnifycolor import MagnifyColor

sample = os.path.join(os.getcwd(), 'tests', 'videos', 'guitar1sec.mp4')


def test_process_video(tmp_path, capsys):
    main([sample, '-o %s' % tmp_path])

    captured = capsys.readouterr()

    assert "Starting Magnification in Color Mode" in captured.out
    assert os.path.isfile(MagnifyColor.output_file_name(filename=sample, suffix="color", path=tmp_path))
    # findet tmp file nicht - obwohl da


def test_output_filename():
    out = MagnifyColor.output_file_name("abd.avi", "color", "/fu/bar/")
    assert out == "/fu/bar/abd_color_evm.avi"


def test_output_filename_with_path():
    out = MagnifyColor.output_file_name("/tmp/abd.avi", "color", "/fu/bar/")
    assert out == "/fu/bar/abd_color_evm.avi"
