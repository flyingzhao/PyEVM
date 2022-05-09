import numpy as np
from numpy import testing

from python_eulerian_video_magnification.magnifycolor import MagnifyColor
from python_eulerian_video_magnification.metadata import MetaData
from python_eulerian_video_magnification.mode import Mode


def test_reconstruct_video():
    original = np.ones((32, 200, 300, 3), dtype='float')
    modified = np.ones((32, 100, 150, 3), dtype='float')
    # the pyramid up with only 1 level will double the dimensions of modified exactly one time

    meta = MetaData(
        file_name="/fu/bar/gob.avi",
        output_folder="/out/put/",
        mode=Mode.COLOR,
        suffix="color",
        low=0.1,
        high=2.1,
        levels=1,
        amplification=23
    )
    magnify = MagnifyColor(data=meta)

    final = magnify._reconstruct_video(modified, original)
    testing.assert_array_equal(final, np.full((32, 200, 300, 3), 2))


def test_for_pyrup_rounding_error_fix():
    image = np.ones((100, 150, 3), dtype='float')

    meta = MetaData(
        file_name="/fu/bar/gob.avi",
        output_folder="/out/put/",
        mode=Mode.COLOR,
        suffix="color",
        low=0.1,
        high=2.1,
        levels=1,
        amplification=23
    )
    magnify = MagnifyColor(data=meta)

    dimensions = (200, 300, 3)
    solution = magnify._correct_dimensionality_problem_after_pyr_up(image, dimensions)
    testing.assert_equal(dimensions, solution.shape)
