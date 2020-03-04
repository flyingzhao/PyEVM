import os.path

from python_eulerian_video_magnification.metadata import MetaData
from python_eulerian_video_magnification.mode import Mode


def test_output_filename(monkeypatch):
    monkeypatch.setattr(MetaData, "get_date", lambda: "2020-01-01-16:16:16")
    out = MetaData.output_file_name("abd.avi", "color", "/fu/bar/")
    assert out == "/fu/bar/abd_color_evm_2020-01-01-16:16:16.avi"


def test_output_filename_with_path(monkeypatch):
    monkeypatch.setattr(MetaData, "get_date", lambda: "2020-01-01-16:16:16")
    out = MetaData.output_file_name("/tmp/abd.avi", "color", "/fu/bar/")
    assert out == "/fu/bar/abd_color_evm_2020-01-01-16:16:16.avi"


def test_output_filename_with_path_for_metadata(monkeypatch):
    monkeypatch.setattr(MetaData, "get_date", lambda: "2020-01-01-16:16:16")
    out = MetaData.output_file_name("/tmp/abd.avi", "color", "/fu/bar/", generate_json=True)
    assert out == "/fu/bar/abd_color_evm_2020-01-01-16:16:16.json"


def test_for_data_as_expected(monkeypatch):
    monkeypatch.setattr(MetaData, "get_date", lambda: "2020-01-01-16:16:16")
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
                                               'target': "/out/put/gob_color_evm_2020-01-01-16:16:16.avi",
                                               'meta_target': "/out/put/gob_color_evm_2020-01-01-16:16:16.json",
                                               'low': 0.1, 'high': 2.1,
                                               'levels': 4,
                                               'amplification': 23, 'mode': 'COLOR', 'suffix': 'color', 'date': None}


def test_json_save(tmp_path):
    sut = MetaData(
        file_name="/fu/bar/gob.avi",
        output_folder=str(tmp_path),
        mode=Mode.COLOR,
        suffix="color",
        low=0.1,
        high=2.1,
        levels=4,
        amplification=23
    )
    sut.save_meta_data()
    assert os.path.exists(sut['meta_target'])
