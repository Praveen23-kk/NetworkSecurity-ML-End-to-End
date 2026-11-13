import os 
import sys

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logger.logger import logging

from networksecurity.components.Data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.components.model_trainer import ModelTrainer


from networksecurity.entity.config_entity import(
    TrainingPipelineConfig,
    DataIngestionConfig,
    DataValidationConfig,
    DataTransformationConfig,
    ModelTrainerConfig,
)

from networksecurity.entity.artifact_entity import(
    DataIngestionArtifact,
    DataValidationArtifact,
    DataTransformationArtifact,
    ModelTrainerArtifact,
)
import sys

class TrainingPipline:
    def __init__(self):
        self.training_pipline_config=TrainingPipelineConfig()
        
    def start_data_ingestion(self):
        try:
            self.data_ingestion_config=DataIngestionConfig(training_pipeline_config=self.training_pipline_config)
            logging.info("start data Ingestion")
            data_ingestion=DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifact=data_ingestion.initiate_data_ingestion()
            logging.info(f"Data Ingestion completed and artifacts:{data_ingestion_artifact}")
            return data_ingestion_artifact
        
        except Exception as e:
            raise NetworkSecurityException(e,sys)
                
    def start_data_validation(self,data_ingestion_artifacts:DataIngestionArtifact):
        try:
            data_validation_config=DataValidationConfig(training_pipeline_config=self.training_pipline_config)
            data_vaildation=DataValidation(data_ingestion_artifacts=data_ingestion_artifacts,data_validation_config)
            logging.info("Initiate the data validation")
            data_validation_Artifact=data_vaildation.initiate_data_vaildation()
            return data_validation_Artifact
        except Exception as e:
    
    def start_data_transformaion(self,data_validation_artifact:DataIngestionArtifact):
        try:
            data_transformation_config = DataTransformationConfig(training_pipeline_config=self.training_pipline_config)
            data_transformation= DataTransformation(data_validation_artifacts=data_validation_artifact,data_transformation_config=data_transformation_config)
            
            data_transformation_artifact = data_transformation.initiate_data_transformation()
            return data_transformation_artifact
        except Exception as e:
            raise NetworkSecurityException(e,sys)        