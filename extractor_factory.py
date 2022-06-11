from Extractors.csv_extractor import CSVExtractor
from Extractors.mysql_extractor import MySQLExtractor
from Extractors.postgresql_extractor import PostgreSQLExtractor
from Extractors.kafka_extractor import KafkaExtractor


class ExtractorFactory:
    @classmethod
    def create_object(cls, config: dict):
        connection_info = config["Connection_info"]
        platform = config["Platform"]
        config = connection_info
        config["platform"] = platform
        if platform   == "MySQL":
            return MySQLExtractor(config)
        elif platform == "PostgreSQL":
            return PostgreSQLExtractor(config)
        elif platform == "Kafka":
            return KafkaExtractor(config)
        elif platform == "CSVFile":
            return CSVExtractor(config)
