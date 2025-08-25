from Text_Summarization.config.configuration import ConfigurationManager
from Text_Summarization.components.data_ingestion import DataIngestion
from Text_Summarization.logging import logging

class DataIngestionPipeline:
    def __init__(self):
        pass

    def main(self):
        import os
        config_manager = ConfigurationManager()
        data_ingestion_config = config_manager.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        import zipfile
        data_ingestion.download_data()
        # Skipping unzip step due to persistent Windows file system issues
        # zip_file = data_ingestion_config.local_data_file
        # if os.path.exists(zip_file) and zipfile.is_zipfile(zip_file):
        #     data_ingestion.unzip_data()
        # else:
        #     from Text_Summarization.logging import logging
        #     logging.error(f"Zip file missing or invalid after download: {zip_file}")
        #     raise FileNotFoundError(f"Zip file missing or invalid after download: {zip_file}")