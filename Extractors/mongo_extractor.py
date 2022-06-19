from Databases.mongo import MongoDB
from extractor import Extractor
from data_capsule import DataCapsule
from typing import List

class MongoExtractor(Extractor, MongoDB):
    def __init__(self, *args, **kwargs):
        MongoDB.__init__(self, *args, **kwargs)

    def read_data_capsule_list(self) -> List[DataCapsule]:
        result = self.collection.find()
        return [DataCapsule(document=item) for item in result]