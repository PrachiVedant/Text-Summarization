import os
from box.exceptions import BoxValueError
import yaml
from Text_Summarization.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    try:
        with open(path_to_yaml,'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file loaded successfully from {path_to_yaml}")
            return ConfigBox(content)
    except BoxValueError :
        raise BoxValueError("yaml file is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_dictionaries(path_to_dictionaries:list,verbose=True):
    for path in path_to_dictionaries:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at {path}")

@ensure_annotations
def get_size(path: Path) -> str:
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"