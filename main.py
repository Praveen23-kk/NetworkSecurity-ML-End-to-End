from networksecurity.components.Data_ingestion import DataIngestion
import os
import sys
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig

if __name__=='__main__':
    try:
        trainingpipline=TrainingPipelineConfig()
        dataingestionconfig=DataIngestionConfig(trainingpipline)
        data_ingestion=DataIngestion(dataingestionconfig)
        logging.info("Initiate the data ingestion")
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        print(dataingestionartifact)
        
    except Exception as e:
           raise NetworkSecurityException(e,sys)