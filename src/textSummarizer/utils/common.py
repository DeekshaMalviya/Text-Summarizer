#utils =  instead of writing a function again and again in components again and again, we write it in utils.py so hat whenever we need we can import this file 

import os
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations  # to run for same datatype, if there is different datatype then it will give error
from box import ConfigBox    # to access any file and data by dictionary format 
from pathlib import Path
from typing import Any


@ensure_annotations  #decorator
def read_yaml(path_to_yaml:Path) ->ConfigBox:
# " reads yaml file and returns

# Args: 
#     path_to_yaml(str) : path like input

# Raises: 
#     valueError: if yaml file is empty
#      e : empty file


  try:
    with open(path_to_yaml) as yaml_file:
      content = yaml.safe_load(yaml_file)
      logger.info(f"yaml:{path_to_yaml}loaded successfully")
      return ConfigBox(content)
  except BoxValueError:
    raise ValueError("yaml file is empty")
  except Exception as e:
    raise e
  


@ensure_annotations
def create_directories(path_to_directories:list,verbose = True):





  for path in path_to_directories:
    os.makedirs(path,exist_ok = True)
    if verbose:
      logger.info(f"created directory at: {path}")





@ensure_annotations
def get_size(path:Path) -> str:

  size_in_kb = round(os.path.getsize(path)/1024)
  return f"~{size_in_kb} KB"