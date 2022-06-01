import json
from typing import List

import psycopg2.extras

from data_capsule import DataCapsule
from extractor import Extractor
from Databases.postgresql import PostgreSQL


class PostgreSQLExtractor(Extractor, PostgreSQL):
    def __init__(self, *args, **kwargs):
        PostgreSQL.__init__(self, *args, **kwargs)
    def read_data_capsule_list(self) -> List[DataCapsule]:
        result = None
        if self.config.get("query"):
            self.cursor.execute(self.config.get("query"))
            result = self.cursor.fetchall()
        else:
            self.cursor.execute("SELECT * FROM {};".format(self.config.get("table")))
            result = self.cursor.fetchall()

        result = self.__convert_RealDictRows_to_datacapsule_list(result)
        return self.__convert_jsons_to_datacapsule_list(result)

    def __convert_RealDictRows_to_datacapsule_list(self, rows: List[psycopg2.extras.RealDictRow]):
        ans = []
        for item in rows:
            current_json = {i: item[i] for i in item.keys()}
            ans.append(current_json)
        return ans

    def __convert_jsons_to_datacapsule_list(self, jsons: List[dict]):
        ans = [DataCapsule(item) for item in jsons]
        return ans


if __name__ == "__main__":
    obj = PostgreSQLExtractor(json.loads(open("../sample_configs/postgresql_extractor_config.json", "r").read()))
    result = obj.read_data_capsule_list()
    for i in result:
        i.beautiful_print()
    print(obj.__dict__)
