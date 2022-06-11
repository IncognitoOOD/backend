from Extractors.csv_extractor import CSVExtractor
from Extractors.mysql_extractor import MySQLExtractor
from Extractors.postgresql_extractor import PostgreSQLExtractor
from Extractors.kafka_extractor import KafkaExtractor

extractor_function = {
    "MySQL": MySQLExtractor,
    "PostgreSQL": PostgreSQLExtractor,
    "Kafka": KafkaExtractor,
    "CSVFile": CSVExtractor
}


class ExtractorFactory:
    @classmethod
    def create_object(cls, config: dict):
        connection_info = config["Connection_info"]
        platform = config["Platform"]
        config = connection_info
        config["platform"] = platform
        return extractor_function[platform](config)
