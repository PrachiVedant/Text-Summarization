import os
import urllib.request as request
import zipfile
from Text_Summarization.utils.common import get_size
from Text_Summarization.logging import logging
from pathlib import Path
from Text_Summarization.entity import DataIngestionConfig

class DataIngestion:
    def __init__(self,config: DataIngestionConfig):
        self.config = config

    def download_data(self):
        if not os.path.exists(self.config.local_data_file):
            filename,headers = request.urlretrieve(
                url=self.config.source_url,
                filename=self.config.local_data_file
            )
            logging.info(f"{filename} download! with following info: \n{headers}")
        else:
            logging.info(f"Data already downloaded to {self.config.local_data_file}")

    def unzip_data(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file,'r') as zip_ref:
            zip_ref.extractall(unzip_path)