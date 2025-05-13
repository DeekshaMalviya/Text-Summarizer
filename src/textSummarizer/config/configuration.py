from textSummarizer.constants import *
from textSummarizer.utils.common import read_yaml,create_directories
from textSummarizer.entity import (DataIngestionConfig)
from textSummarizer.entity import (DataValidationConfig)

class ConfigurationManager:  ## preparing method for data ingestion
  def __init__(     ##creating constructor 
      self,
      config_filepath = CONFIG_FILE_PATH,
      param_filepath = PARAMS_FILE_PATH):

      self.config = read_yaml(config_filepath)   ##read this yaml file and access all the variable inside
      self.params = read_yaml(param_filepath)

      ##create artifacts folder using create_dir function  
      create_directories([self.config.artifacts_root]) 



  def get_data_ingestion_config(self) -> DataIngestionConfig:  ## this is the return type      
    # this is data ingestion related config to access all the thing under config.yaml file 
    config = self.config.data_ingestion

    create_directories([config.root_dir])

    data_ingestion_config = DataIngestionConfig(
      root_dir= config.root_dir,
      source_URL= config.source_URL,
      local_data_file= config.local_data_file,
      unzip_dir= config.unzip_dir
    )

    return data_ingestion_config
  



  def get_data_validation_config(self) -> DataValidationConfig:  ## this is the return type      
    # this is data validation related config to access all the thing under config.yaml file 
    config = self.config.data_validation

    create_directories([config.root_dir])

    data_validation_config = DataValidationConfig(
      root_dir= config.root_dir,
      STATUS_FILE= config.STATUS_FILE,
      ALL_REQUIRED_FILES= config.ALL_REQUIRED_FILES
    )

    return data_validation_config


  