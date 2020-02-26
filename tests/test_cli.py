import functools
import logging
import os
import os.path

import pytest
from python_eulerian_video_magnification import cli

from python_eulerian_video_magnification.mode import Mode

base_path = functools.partial(os.path.join, os.getcwd(), 'tests', 'videos')
sample = base_path('guitar1sec.mp4')
wrong_video = base_path('wrong_video.txt')


def test_for_correctly_set_file():
    sut = cli.CLI()
    sut.parse(args=[sample])
    assert sut.get_file.name == sample


def test_for_wrong_file():
    sut = cli.CLI()
    with pytest.raises(SystemExit) as e:
        sut.parse(args=[wrong_video])
    assert "10" in str(e.value)


def test_check_mode():
    sut = cli.CLI()
    sut.parse(args=[sample, '-m', 'motion'])
    assert sut.get_mode == Mode.MOTION


def test_mode_default():
    sut = cli.CLI()
    sut.parse(args=[sample])
    assert sut.get_mode == Mode.COLOR


def test_log_level_set():
    sut = cli.CLI()
    sut.parse(args=[sample, '--loglevel=warning'])
    assert sut.get_log_level == logging.WARNING, "log level should be warning"


def test_log_level_wrong():
    sut = cli.CLI()
    with pytest.raises(SystemExit) as e:
        sut.parse(args=[sample, '--loglevel=fubar'])
    assert "2" in str(e.value)


@pytest.mark.parametrize(
    "value, parameter_flag, method",
    [
        (0.5, "-c", 'get_low'),
        (3.2, '-p', 'get_high'),
        (5, '-l', 'get_levels'),
        (10, '-a', 'get_amplification')
    ]
)
def test_correctly_set_numeric(value, parameter_flag, method):
    sut = cli.CLI()
    sut.parse(args=[sample, '%s %s' % (parameter_flag, value)])
    assert getattr(sut, method) == value


def test_for_invalid_output_path():
    sut = cli.CLI()
    sut.parse(args=[sample, '-o %s' % base_path('invalid.path')])
