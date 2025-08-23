import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from Text_Summarization.pipelines.stage_01_data_ingestion import DataIngestionPipeline
from Text_Summarization.pipelines.stage_02_data_validation import DataValidationPipeline
from Text_Summarization.logging import logging



STAGE_NAME = "Data Ingestion stage"
try:
   logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionPipeline()
   data_ingestion.main()
   logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logging.exception(e)
        raise e


STAGE_NAME = "Data Validation stage"
try:
   logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_validation = DataValidationPipeline()
   data_validation.main()
   logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logging.exception(e)
        raise e