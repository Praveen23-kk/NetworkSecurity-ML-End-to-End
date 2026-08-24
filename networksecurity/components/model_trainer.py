import os
import sys

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

from networksecurity.utils.ml_utils.model.estimater import NetworkModel
from networksecurity.utils.main_utils.utils import save_object,load_object


from networksecurity.utils.ml_utils.model.estimator import NetworkModel
from networksecurity.utils.main_utils.utils import save_object,load_object
from networksecurity.utils.main_utils.utils import load_numpy_array_data
from networksecurity.utils.ml_utils.metric.classification_metric import get_classification


class ModelTrainer:
    def __init__(self.model_trainer_config:ModelTrainer,data_transformation_artifact:DataTransformationArtifact):
        try:
            self.model_trainer_config = model_trainer_config
            self.data_transfomration_artifacts=data_transformation_artifact
            
        except Exception as e:
            raise NetworkSecurityException(e,sys)


    def initiate_model_trainer(seld)->ModelTrainerArtifacts:
        try:
            train_file_path = self.data_transformation_artifacts.transfomed_train_file_path
            test_file_path = self.data_transformation_artifact.transformed_test_file_path
            
            #loading training array and testing array
            train_arr = load_numpy_array_data(train_file_path)
            test_arr = load_numpy_array_data(test_file_path)
            
            x_train,y_train, x_test, y_test=(
                train_arr[:,:-1],
                train_arr[:,:-1],
                test_arr[:,:-1],
                test_arr[:,:-1],
            )
            
            model=self.train_model(x_train,y_train)
        except Exception as e:
            raise NetworkSecurityException(e,sys)
