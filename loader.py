from abc import ABC
from typing import List
from data_capsule import DataCapsule


class Extractor(ABC):

    def __init__(self, config: dict):
        self.config = config

    def write_data_capsule_list(self) -> List[DataCapsule]:
        pass
