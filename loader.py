from abc import ABC, abstractmethod
from typing import List
from data_capsule import DataCapsule


class Loader(ABC):

    def __init__(self, config: dict):
        self.config = config

    @abstractmethod
    def write_data_capsule_list(self, dc_list: List[DataCapsule]):
        pass

    def run(self, dc_list=None):
        self.write_data_capsule_list(dc_list=dc_list)
        return dc_list
