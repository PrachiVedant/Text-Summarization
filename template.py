import os
from pathlib import Path
import logging

project_name = "Text-Summarization"

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

list_of_files=[
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipelines/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/parameters/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    f"src/{project_name}/logging/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    
    ]

for filepath in list_of_files:
    filepaths=Path(filepath)
    filedir,filename = os.path.split(filepaths)

    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory: {filedir}")

    if not os.path.exists(filepaths) or os.path.getsize(filepaths)==0:
        with open(filepaths,'w') as f:
            pass
            logging.info(f"Creating file: {filepath}")

    else:
        logging.info(f"File already exists: {filepath} or is not empty.")