import json
from typing import List

from data_capsule import DataCapsule
from loader import Loader
from Databases.mysql import MySQL


class MySQLLoader(Loader, MySQL):
    def __init__(self, *args, **kwargs):
        MySQL.__init__(self, *args, **kwargs)
        self.cursor.execute("SHOW columns FROM student;")
        self.columns = [item["Field"] for item in self.cursor.fetchall()]

    def write_data_capsule_list(self, dc_list: List[DataCapsule]):
        for dc in dc_list:
            value_str = ",".join([('"{}"'.format(str(dc.document[column]))) for column in self.columns])
            self.cursor.execute("""INSERT INTO {} VALUES ({})""".format(self.config.get("table"), value_str))
            self.db.commit()


if __name__ == "__main__":
    obj = MySQLLoader(json.loads(open("../sample_configs/mysql_loader_config.json", "r").read()))
