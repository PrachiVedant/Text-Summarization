from Text_Summarization.config.configuration import ConfigurationManager
from Text_Summarization.components.data_validation import DataValidation
from Text_Summarization.logging import logging

class DataValidationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_validation_config()

        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_data()