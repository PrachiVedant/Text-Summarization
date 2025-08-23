import os
import logging

from Text_Summarization.entity import DataValidationConfig

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_data(self):
        try:
            logging.info("Validating data...")
            validation_status = None

            all_files = os.listdir(os.path.join("artifacts", "data_ingestion", "samsum_dataset"))
            for files in all_files:
                if files not in self.config.ALL_REQUIRED_FILES:
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status : {validation_status}")
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status : {validation_status}")
        
            return validation_status
        
        except Exception as e:
            raise e
    