import json
from typing import List

from data_capsule import DataCapsule
from loader import Loader
from Databases.kafka import Kafka
from confluent_kafka import Producer


class KafkaLoader(Loader, Kafka):
    def __init__(self, *args, **kwargs):
        Kafka.__init__(self, *args, **kwargs)
        self.conf = {'bootstrap.servers': self.config["bootstrap_servers"]}
        self.producer = Producer(self.conf)

    def write_data_capsule_list(self, dc_list: List[DataCapsule]):
        for dc in dc_list:
            self.producer.produce(topic=self.config["topic"], value=json.dumps(dc.document))
            self.producer.flush()


if __name__ == "__main__":
    obj = KafkaLoader(json.loads(open("../sample_configs/kafka_loader_config.json", "r").read()))
