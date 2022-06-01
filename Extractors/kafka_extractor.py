import json
from typing import List
from data_capsule import DataCapsule
from extractor import Extractor
from Databases.kafka import Kafka
from confluent_kafka import Consumer
from confluent_kafka import KafkaError


class KafkaExtractor(Extractor, Kafka):
    def __init__(self, *args, **kwargs):
        Kafka.__init__(self, *args, **kwargs)
        self.conf = {'bootstrap.servers': self.config["bootstrap_servers"],
                     'group.id': self.config["group_id"],
                     'auto.offset.reset': 'earliest'}
        self.consumer = Consumer(self.conf)
        self.consumer.subscribe([self.config["topic"]])

    def read_data_capsule_list(self) -> List[DataCapsule]:
        ans = []
        while True:
            msg = self.consumer.poll(timeout=5.0)
            if msg is None:
                break
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    break
            else:
                ans.append(json.loads(msg.value()))
        return self.__convert_jsons_to_datacapsule_list(ans)

    def __convert_jsons_to_datacapsule_list(self, jsons: List[dict]):
        ans = [DataCapsule(item) for item in jsons]
        return ans


if __name__ == "__main__":
    obj = KafkaExtractor(json.loads(open("../sample_configs/kafka_extractor_config.json", "r").read()))
    result = obj.read_data_capsule_list()
    for i in result:
        i.beautiful_print()
    print(obj.__dict__)




