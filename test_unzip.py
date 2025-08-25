import zipfile
import os

zip_path = os.path.abspath("artifacts/data_ingestion/data.zip")
print("Testing unzip for:", zip_path)
print("Exists:", os.path.exists(zip_path))
try:
    with open(zip_path, 'rb') as f:
        print("File opened for reading.")
except Exception as e:
    print("Failed to open file:", e)
try:
    with zipfile.ZipFile(zip_path, 'r') as zf:
        print("ZipFile opened successfully.")
        zf.extractall("test_unzip")
        print("Extraction complete.")
except Exception as e:
    print("ZipFile error:", e)
