from Extractors.csv_extractor import CSVExtractor
from Extractors.mysql_extractor import MySQLExtractor
from Extractors.postgresql_extractor import PostgreSQLExtractor
from Extractors.kafka_extractor import KafkaExtractor


class ExtractorFactory:
    @classmethod
    def create_object(cls, config: dict):
        if str(config["type"]).lower() == "mysql":
            return MySQLExtractor(config)
        elif str(config["type"]).lower() == "postgresql":
            return PostgreSQLExtractor(config)
        elif str(config["type"]).lower() == "kafka":
            return KafkaExtractor(config)
        elif str(config["type"]).lower() == "csv":
            return CSVExtractor(config)
