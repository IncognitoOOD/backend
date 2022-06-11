from Loaders.csv_loader import CSVLoader
from Loaders.mysql_loader import MySQLLoader
from Loaders.postgresql_loader import PostgreSQLLoader
from Loaders.kafka_loader import KafkaLoader

loader_function = {
    "MySQL": MySQLLoader,
    "PostgreSQL": PostgreSQLLoader,
    "Kafka": KafkaLoader,
    "CSVFile": CSVLoader
}

class LoaderFactory:
    @classmethod
    def create_object(cls, config: dict):
        connection_info = config["Connection_info"]
        platform = config["Platform"]
        config = connection_info
        config["platform"] = platform
        if str(platform)   == "MySQL":
            return MySQLLoader(config)
        elif str(platform) == "PostgreSQL":
            return PostgreSQLLoader(config)
        elif str(platform) == "Kafka":
            return KafkaLoader(config)
        elif str(platform) == "CSVFile":
            return CSVLoader(config)
