from abc import ABC, abstractmethod
from data_capsule import DataCapsule
from typing import List


class Extractor(ABC):

    def __init__(self, config: dict):
        self.config = config

    @abstractmethod
    def read_data_capsule_list(self) -> List[DataCapsule]:
        pass
