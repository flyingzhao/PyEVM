import pytest

from python_eulerian_video_magnification.magnify import Magnify
from python_eulerian_video_magnification.metadata import MetaData
from python_eulerian_video_magnification.mode import Mode


@pytest.fixture
def magnify_sut():
    data = MetaData(file_name="fubar", output_folder="/fu/bar", mode=Mode.COLOR, suffix="color",
                    low=0.1, high=3.1, levels=2,
                    amplification=23)
    return Magnify(data=data)


@pytest.mark.parametrize(
    "property_to_test, value",
    [
        ("_low", 0.1),
        ("_high", 3.1),
        ("_levels", 2),
        ("_amplification", 23)
    ]
)
def test_properties(property_to_test, value, magnify_sut):
    assert getattr(magnify_sut, property_to_test) == value
