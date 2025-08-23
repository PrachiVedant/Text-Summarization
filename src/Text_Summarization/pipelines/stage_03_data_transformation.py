from Text_Summarization.config.configuration import ConfigurationManager
from Text_Summarization.components.data_transformation import DataTransformation, DataTransformationConfig
from Text_Summarization.logging import logging

class DataTransformationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_transformation_config()

        data_transformation = DataTransformation(config=data_transformation_config)
        status = data_transformation.convert()