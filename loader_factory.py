from Loaders.csv_loader import CSVLoader
from Loaders.mongo_loader import MongoLoader
from Loaders.mysql_loader import MySQLLoader
from Loaders.postgresql_loader import PostgreSQLLoader
from Loaders.kafka_loader import KafkaLoader
from Loaders.mongo_loader import MongoLoader

loader_function = {
    "MySQL": MySQLLoader,
    "PostgreSQL": PostgreSQLLoader,
    "Kafka": KafkaLoader,
    "CSVFile": CSVLoader,
    "MongoDB": MongoLoader
}


class LoaderFactory:
    @classmethod
    def create_object(cls, config: dict):
        connection_info = config["Connection_info"]
        platform = config["Platform"]
        config = connection_info
        config["platform"] = platform
        return loader_function[platform](config)
