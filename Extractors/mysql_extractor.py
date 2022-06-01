import json
from typing import List

from data_capsule import DataCapsule
from extractor import Extractor
from Databases.mysql import MySQL


class MySQLExtractor(Extractor, MySQL):
    def __init__(self, *args, **kwargs):
        MySQL.__init__(self, *args, **kwargs)

    def read_data_capsule_list(self) -> List[DataCapsule]:
        result = None
        if self.config.get("query"):
            self.cursor.execute(self.config.get("query"))
            result = self.cursor.fetchall()
        else:
            self.cursor.execute("SELECT * FROM {};".format(self.config.get("table")))
            result = self.cursor.fetchall()

        return self.__convert_jsons_to_datacapsule_list(result)

    def __convert_jsons_to_datacapsule_list(self, jsons: List[dict]):
        ans = [DataCapsule(item, self.columns) for item in jsons]
        return ans


if __name__ == "__main__":
    obj = MySQLExtractor(json.loads(open("../sample_configs/mysql_extractor_config.json", "r").read()))
    result = obj.read_data_capsule_list()
    for i in result:
        i.beautiful_print()
    print(obj.__dict__)
