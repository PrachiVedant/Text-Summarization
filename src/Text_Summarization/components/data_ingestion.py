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
        import zipfile
        import time
        file_exists = os.path.exists(self.config.local_data_file)
        is_valid_zip = False
        if file_exists:
            try:
                is_valid_zip = zipfile.is_zipfile(self.config.local_data_file)
            except Exception:
                is_valid_zip = False
        if (not file_exists) or (not is_valid_zip):
            if file_exists and not is_valid_zip:
                os.remove(self.config.local_data_file)
                logging.warning(f"Removed corrupted or invalid zip: {self.config.local_data_file}")
            filename, headers = request.urlretrieve(
                url=self.config.source_url,
                filename=self.config.local_data_file
            )
            logging.info(f"{filename} download! with following info: \n{headers}")
            # Wait and check for file existence
            for _ in range(5):
                if os.path.exists(self.config.local_data_file):
                    break
                time.sleep(1)
            if not os.path.exists(self.config.local_data_file):
                raise FileNotFoundError(f"Download failed, file not found: {self.config.local_data_file}")
            print("After download, file exists:", os.path.exists(self.config.local_data_file))
            print("Absolute path:", os.path.abspath(self.config.local_data_file))
        else:
            logging.info(f"Data already downloaded and valid at {self.config.local_data_file}")
            print("After download, file exists:", os.path.exists(self.config.local_data_file))
            print("Absolute path:", os.path.abspath(self.config.local_data_file))

    def unzip_data(self):
        print("At unzip, file exists:", os.path.exists(self.config.local_data_file))
        print("Absolute path:", os.path.abspath(self.config.local_data_file))
        # Try to open the file directly
        try:
            with open(self.config.local_data_file, 'rb') as f:
                print("File opened successfully for reading.")
        except Exception as e:
            print("Failed to open file:", e)
        # Force garbage collection and wait to avoid file lock/race condition
        import gc
        import time
        gc.collect()
        time.sleep(1)
        # Force garbage collection and add a short delay to avoid file lock/race condition
        import gc
        import time
        gc.collect()
        time.sleep(1)
        import shutil
        unzip_path = self.config.unzip_dir
        zip_file = os.path.abspath(self.config.local_data_file)
        if not os.path.exists(zip_file):
            raise FileNotFoundError(f"Zip file not found: {zip_file}")
        # Clean extraction directory if it exists
        if os.path.exists(unzip_path):
            shutil.rmtree(unzip_path)
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            for member in zip_ref.infolist():
                # Skip files with invalid Windows names
                filename = member.filename
                # Check for reserved names or invalid characters
                invalid = any(char in filename for char in '<>:"/\\|?*')
                reserved = any(
                    part.upper() in ["CON", "PRN", "AUX", "NUL", "COM1", "COM2", "COM3", "COM4", "COM5", "COM6", "COM7", "COM8", "COM9", "LPT1", "LPT2", "LPT3", "LPT4", "LPT5", "LPT6", "LPT7", "LPT8", "LPT9"]
                    for part in filename.replace('\\', '/').split('/')
                )
                if invalid or reserved:
                    logging.warning(f"Skipping invalid or reserved file in zip: {filename}")
                    continue
                try:
                    zip_ref.extract(member, unzip_path)
                except OSError as e:
                    logging.warning(f"Skipping file due to OSError: {filename} ({e})")
                    continue