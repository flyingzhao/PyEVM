from python_eulerian_video_magnification.metadata import MetaData
from python_eulerian_video_magnification.mode import Mode


def test_output_filename():
    out = MetaData.output_file_name("abd.avi", "color", "/fu/bar/")
    assert out == "/fu/bar/abd_color_evm.avi"


def test_output_filename_with_path():
    out = MetaData.output_file_name("/tmp/abd.avi", "color", "/fu/bar/")
    assert out == "/fu/bar/abd_color_evm.avi"


def test_output_filename_with_path_for_metadata():
    out = MetaData.output_file_name("/tmp/abd.avi", "color", "/fu/bar/", generate_json=True)
    assert out == "/fu/bar/abd_color_evm.json"


def test_for_data_as_expected():
    sut = MetaData(
        file_name="/fu/bar/gob.avi",
        output_folder="/out/put/",
        mode=Mode.COLOR,
        suffix="color",
        low=0.1,
        high=2.1,
        levels=4,
        amplification=23
    )
    assert getattr(sut, "_MetaData__data") == {'file': "/fu/bar/gob.avi", 'output': "/out/put/",
                                               'target': "/out/put/gob_color_evm.avi",
                                               'meta_target': "/out/put/gob_color_evm.json", 'low': 0.1, 'high': 2.1,
                                               'levels': 4,
                                               'amplification': 23, 'mode': 'COLOR', 'suffix': 'color'}
