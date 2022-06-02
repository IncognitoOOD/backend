from Loaders.csv_loader import CSVLoader
from Loaders.mysql_loader import MySQLLoader
from Loaders.postgresql_loader import PostgreSQLLoader
from Loaders.kafka_loader import KafkaLoader


class LoaderFactory:
    @classmethod
    def create_object(cls, config: dict):
        if str(config["type"]).lower() == "mysql":
            return MySQLLoader(config)
        elif str(config["type"]).lower() == "postgresql":
            return PostgreSQLLoader(config)
        elif str(config["type"]).lower() == "kafka":
            return KafkaLoader(config)
        elif str(config["type"]).lower() == "csv":
            return CSVLoader(config)
