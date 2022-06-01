import json
from typing import List

from data_capsule import DataCapsule
from loader import Loader
from Databases.postgresql import PostgreSQL


class PostgreSQLLoader(Loader, PostgreSQL):
    def __init__(self, *args, **kwargs):
        PostgreSQL.__init__(self, *args, **kwargs)
        query = """SELECT column_name
  FROM information_schema.columns
 WHERE table_schema = 'public'
   AND table_name   = '{}';""".format(self.config["table"])
        self.cursor.execute(query)
        temp = self.cursor.fetchall()
        self.columns = [item["column_name"] for item in temp]

    def write_data_capsule_list(self, dc_list: List[DataCapsule]):
        for dc in dc_list:
            value_str = ",".join([("'{}'".format(str(dc.document[column]))) for column in self.columns])
            self.cursor.execute("""INSERT INTO {} VALUES ({})""".format(self.config.get("table"), value_str))
            self.db.commit()


if __name__ == "__main__":
    obj = PostgreSQLLoader(json.loads(open("../sample_configs/postgresql_loader_config.json", "r").read()))
