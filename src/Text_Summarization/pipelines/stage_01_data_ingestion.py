from Text_Summarization.config.configuration import ConfigurationManager
from Text_Summarization.components.data_ingestion import DataIngestion
from Text_Summarization.logging import logging

class DataIngestionPipeline:
    def __init__(self):
        pass

    def main(self):
        config_manager = ConfigurationManager()
        data_ingestion_config = config_manager.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)

        data_ingestion.download_data()
        data_ingestion.unzip_data()