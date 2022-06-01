import csv
import json
from typing import List

from data_capsule import DataCapsule
from loader import Loader
from Databases.csv import CSV
import os

FILE = "file_path"

class CSVLoader(Loader, CSV):
    def __init__(self, *args, **kwargs):
        CSV.__init__(self, *args, **kwargs)

    def write_data_capsule_list(self, dc_list: List[DataCapsule]):
        is_new = False
        if not os.path.isfile(self.config[FILE]):
            is_new = True

        if is_new:
            with open(self.config[FILE], "w") as f:
                writer = csv.writer(f)
                writer.writerow(dc_list[0].fields)

        with open(self.config[FILE], "a") as f:
            writer = csv.writer(f)
            for item in dc_list:
                writer.writerow([item.document[field] for field in item.fields])


if __name__ == "__main__":
    obj = CSVLoader(json.loads(open("../sample_configs/csv_loader_config.json", "r").read()))
