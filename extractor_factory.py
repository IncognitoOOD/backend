from Extractors.csv_extractor import CSVExtractor
from Extractors.mysql_extractor import MySQLExtractor
from Extractors.postgresql_extractor import PostgreSQLExtractor
from Extractors.kafka_extractor import KafkaExtractor


class ExtractorFactory:
    @classmethod
    def create_object(cls, config: dict):
        if str(config["platform"]).lower() == "mysql":
            return MySQLExtractor(config)
        elif str(config["platform"]).lower() == "postgresql":
            return PostgreSQLExtractor(config)
        elif str(config["platform"]).lower() == "kafka":
            return KafkaExtractor(config)
        elif str(config["platform"]).lower() == "csv":
            return CSVExtractor(config)
