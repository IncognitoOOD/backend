from confluent_kafka import Consumer
from confluent_kafka import KafkaError


class Kafka():
    def __init__(self, config = None):
        self.config = config
