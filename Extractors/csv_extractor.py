import json
from typing import List
import csv
from data_capsule import DataCapsule
from extractor import Extractor
from Databases.csv import CSV

KEY_NAME = "file_path"

class CSVExtractor(Extractor, CSV):
    def __init__(self, *args, **kwargs):
        CSV.__init__(self, *args, **kwargs)

    def read_data_capsule_list(self) -> List[DataCapsule]:
        header = None
        rows = []
        with open(self.config[KEY_NAME]) as file:
            csv_reader = csv.reader(file)
            header = next(csv_reader)
            for row in csv_reader:
                rows.append(row)
        result = self.__convert_csv_list_to_json(header, rows)
        return self.__convert_jsons_to_datacapsule_list(result)

    def __convert_csv_list_to_json(self, header: list, rows: list):
        result = []
        for row in rows:
            current_json = {}
            for field, value in zip(header, row):
                current_json[field] = value
            result.append(current_json)
        return result

    def __convert_jsons_to_datacapsule_list(self, jsons: List[dict]):
        ans = [DataCapsule(item) for item in jsons]
        return ans


if __name__ == "__main__":
    obj = CSVExtractor(json.loads(open("../sample_configs/csv_extractor_config.json", "r").read()))
    result = obj.read_data_capsule_list()
    for i in result:
        i.beautiful_print()
    print(obj.__dict__)
