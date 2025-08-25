from Text_Summarization.config.configuration import ConfigurationManager
from Text_Summarization.components.data_training import ModelTrainerConfig,ModelTrainer
from Text_Summarization.logging import logging

class DataTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config=model_trainer_config)
        model_trainer.train()