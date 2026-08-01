from networksecurity.components.Data_ingestion import DataIngestion
import os
from networksecurity.components.data_validation import DataValidation
import sys
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig, DataValidationConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig

if __name__=='__main__':
    try:
        trainingpipline=TrainingPipelineConfig()
        dataingestionconfig=DataIngestionConfig(trainingpipline)
        data_ingestion=DataIngestion(dataingestionconfig)
        logging.info("Initiate the data ingestion")
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        logging.info("Data Initiation Completed")
        print(dataingestionartifact)
        data_validation_config=DataValidationConfig(trainingpipline)
        data_vaildation=DataValidation(dataingestionartifact,data_validation_config)
        logging.info("Initiate the data validation")
        data_validation_Artifact=data_vaildation.initiate_data_vaildation()
        logging.info("data validation completed")
        
    except Exception as e:
           raise NetworkSecurityException(e,sys)