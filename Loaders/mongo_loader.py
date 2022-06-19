from Databases.mongo import MongoDB
from loader import Loader
from data_capsule import DataCapsule
from typing import List

class MongoLoader(Loader, MongoDB):
    def __init__(self, *args, **kwargs):
        MongoDB.__init__(self, *args, **kwargs)

    def load_data_capsule_list(self, data_capsule_list: List[DataCapsule]):
        for item in data_capsule_list:
            self.collection.insert_one(item.document)
        return data_capsule_list