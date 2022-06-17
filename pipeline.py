import time
import json
from data_capsule import DataCapsule
from extractor import Extractor
from loader import Loader
import random
from extractor_factory import ExtractorFactory
from loader_factory import LoaderFactory
from transformer import Transformer
from redis_manager import RedisManager

class Pipeline:
    __config: dict
    __extractor: Extractor
    __transformers: list
    __loader: Loader

    def __init__(self, config: dict):
        self.__config = config

        if not self.__config.get("unique_id"):
            self.__config["unique_id"] = self.generate_unique_id()
        self.__loader = LoaderFactory.create_object(config["loader"])
        self.__extractor = ExtractorFactory.create_object(config["extractor"])
        self.__transformers = [Transformer(item) for item in config["transformers"]]
        self.redis = RedisManager()

    def get_config(self):
        return self.__config

    def generate_unique_id(self):
        # generate a random unique string
        x = ""
        for i in range(8):
            x += str(random.randint(0, 9))
        return x

    def get_unique_id(self):
        return self.__config['unique_id']

    def should_run(self):
        if self.__config.get("disabled"):
            return False
        else:
            return True

    def run(self):
        if self.redis.key_exists(self.get_unique_id()) and self.redis.load_state(self.get_unique_id()) != "finished":
            rdata = self.redis.load_state(self.get_unique_id())
            dc_list = [DataCapsule(json_data=i) for i in rdata["data"]]
            step = int(rdata["step"])
            job_list = [self.__extractor] + self.__transformers + [self.__loader]
            while step < len(job_list):
                job = job_list[step]
                dc_list = job.run(dc_list)
                step += 1
                self.redis.save_state(self.get_unique_id(), {"step": step, "data": [i.get_json() for i in dc_list]})
            self.__config["disabled"] = True
        else:
            step = 0
            data = self.__extractor.read_data_capsule_list()
            step = 1
            self.redis.save_state(self.get_unique_id(), {"step": step, "data": [i.get_json() for i in data]})
            for transformer in self.__transformers:
                data = transformer.run(data)
                step += 1
                self.redis.save_state(self.get_unique_id(), {"step": step, "data": [i.get_json() for i in data]})
            self.__loader.write_data_capsule_list(data)
            self.redis.save_state(self.get_unique_id(), "finished")
            self.__config["disabled"] = True

    @classmethod
    def test_pipeline_config(cls, full_config: dict):
        try:
            _ = LoaderFactory.create_object(full_config["loader"])
        except Exception:
            print(full_config)
            print(full_config["loader"])
            return False, ["Incorrect loader config"]
        try:
            _ = ExtractorFactory.create_object(full_config["extractor"])
        except Exception:
            return False, ["Incorrect extractor config"]

        # TODO TRY TRANSFORMER

        return True, ["ok"]


if __name__ == "__main__":
    config = json.loads(open("sample_configs/full_config_1.json", "r").read())
    p = Pipeline(config)
    p.run()
