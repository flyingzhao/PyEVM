import json
import os.path
from datetime import datetime

from python_eulerian_video_magnification.mode import Mode


class MetaData:

    def __init__(self, file_name: str, output_folder: str,
                 mode: Mode, suffix: str,
                 low: float, high: float,
                 levels: int = 3, amplification: int = 20
                 ):
        self.__data = {
            'file': file_name,
            'output': output_folder,
            'target': MetaData.output_file_name(file_name, suffix=suffix, path=output_folder),
            'meta_target': MetaData.output_file_name(file_name, suffix=suffix, path=output_folder, generate_json=True),
            'low': low,
            'high': high,
            'levels': levels,
            'amplification': amplification,
            'mode': mode.name,
            'suffix': suffix,
            'date': None,
        }

    @staticmethod
    def output_file_name(filename: str, suffix: str, path: str, generate_json=False):
        filename_split = os.path.splitext(os.path.split(filename)[-1])
        extension = ".json" if generate_json else filename_split[1]
        return os.path.join(path, filename_split[0] + "_%s_evm_%s" % (suffix, MetaData.get_date()) + extension)

    def __getitem__(self, item):
        return self.__data[item]

    def save_meta_data(self):
        """stores the meta data dictionary as a json"""
        self.__data['date'] = self.get_date()
        with open(self.__data['meta_target'], 'w') as fp:
            json.dump(self.__data, fp=fp, sort_keys=True, indent=4, separators=(',', ': '))

    @staticmethod
    def get_date() -> str:
        return str(datetime.now()).replace(' ', '-').split('.')[0]
