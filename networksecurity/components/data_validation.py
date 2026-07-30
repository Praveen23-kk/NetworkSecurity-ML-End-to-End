from networksecurity.entity.artifact_entity import DataIngestionArtifact,DataValidationArtifact
from networksecurity.entity.config_entity import DataValidationConfig
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.constant.training_pipeline import SCHEMA_FILE_PATH
from scipy.stats import ks_2samp
import pandas as pd 
import os,sys
from networksecurity.utils.main_utils.utils import read_yaml_file 


class DataValidation:
    def __init__(self,data_ingestion_artifacts:DataIngestionArtifact,
                 data_validation_config:DataIngestionArtifact):
        
        
        try:
            self.data_ingestion_artifact=self.data_ingestion_artifact
            self.data_validation_config=data_validation_config
            self._schema_config = read_yaml_file(SCHEMA_FILE_PATH)
        except Exception as e:
            raise NetworkSecurityException(e,sys) 
        
    @staticmethod
    def read_data(file_path)-> pd.DataFrame:
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise NetworkSecurityException(e,sys)
               
    def validation_number_of_column(self,dataframe:pd.DataFrame)->bool:
        try:
            number_of_columns=len(self._schema_config)
            logging.info(f"Required number of column:{number_of_columns}")
            logging.info(f"Data frame as columns:{len(dataframe.columns)}")
            if len(dataframe.columns)==number_of_columns:
                return True
            return False
        
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    def detect_dataset_drift(self,base_df,current_df,threshold=0.05)->bool:
        try:
            status=True
            report={}
            for column in base_df.columns:
                d1=base_df[column]
                d2=current_df[column]
                is_sample_dist=ks_2samp(d1,d2)
                
                if threshold<=is_sample_dist.pvalue:
                    if_found=False
                else:
                    is_found=True
                    status=False
                report.update({column:{
                    "p_value":float(is_sample_dist.pvalue),
                    "drift_status":is_found
                }})
        drift_report_file_path = self.data_validation_config.drift_report_file_path
        
        # create directory
        dir_path = os.path.dirname(drift_report_file_path)
        os.makedirs(dir_path,exist_ok=True)              

                
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    def initiate_data_vaildation(self)->DataValidationArtifact:
        try:
            train_file_path=self.data_ingestion_artifact.trained_file_path
            test_file_path=self.data_ingestion_artifact.test_file_path
            
            #Read the data from file struture 
            train_dataframe=DataValidation.read_data(train_file_path)
            test_dataframe=DataValidation.read_data(test_file_path)
            
            ## Validate number of columns
            
            status=self.validation_number_of_column(dataframe=train_dataframe)
            if not status:
                error_message=f"Train dataframe does not contain all colums \n"
            if not status:
                error_message=f" Test dataframe does not contain all colums \n"    
            
            ## lets check datadrift
               
        except Exception as e:
            raise NetworkSecurityException(e,sys)






