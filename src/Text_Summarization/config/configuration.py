from Text_Summarization.constants import *
from Text_Summarization.utils.common import read_yaml, create_dictionaries
from Text_Summarization.entity import (DataIngestionConfig,
                                       DataValidationConfig,
                                       DataTransformationConfig)

from pathlib import Path
CONFIG_FILE_PATH = Path("config/config.yaml")
PARAMS_FILE_PATH = Path("params.yaml")

class ConfigurationManager:
    def __init__(self,
                 config_filepath = CONFIG_FILE_PATH,
                 params_filepath = PARAMS_FILE_PATH):
        
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_dictionaries([self.config.artifacts_root],verbose=True)

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_dictionaries([config.root_dir],verbose=True)

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_url=config.source_url,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion_config
    



    def get_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation

        create_dictionaries([config.root_dir],verbose=True)

        data_validation_config = DataValidationConfig(
            root_dir=Path(self.config.data_validation.root_dir),
            STATUS_FILE=Path(self.config.data_validation.STATUS_FILE),
            ALL_REQUIRED_FILES=self.config.data_validation.ALL_REQUIRED_FILES
        )
        return data_validation_config
    
    
    def get_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation

        create_dictionaries([config.root_dir], verbose=True)
        
        data_transformation_config =  DataTransformationConfig(
            root_dir=Path(self.config.data_transformation.root_dir),
            data_path=Path(self.config.data_transformation.data_path),
            tokenizer=self.config.data_transformation.tokenizer
        )
        return data_transformation_config