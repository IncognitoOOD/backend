import sys
sys.path.append('../')
from Databases.mongo import MongoDB

from loader import Loader
from data_capsule import DataCapsule
from typing import List

class MongoLoader(Loader, MongoDB):
    def __init__(self, *args, **kwargs):
        MongoDB.__init__(self, *args, **kwargs)

    def write_data_capsule_list(self, data_capsule_list: List[DataCapsule]):
        for item in data_capsule_list:
            self.collection.insert_one(item.document)
        return data_capsule_list

if __name__ == "__main__":
    db = MongoLoader(config={"host": "localhost", "port": 27017, "username": "root", "password": "root", "database": "dbt", "collection": "t2"})
    db.load_data_capsule_list([DataCapsule(document={"a": 1, "b": 2}), DataCapsule(document={"a": 3, "b": 4})])