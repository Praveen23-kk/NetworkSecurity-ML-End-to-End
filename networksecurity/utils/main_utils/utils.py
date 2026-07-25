import yaml
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
import os,sys
import numpy as np 
import dill
import pickle
from networksecurity.utils.main_utils import read_yaml_file

def read_yaml_file(file_path:str)-> dict:
    try:
        with open(file_path,"rb")as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise NetworkSecurityException(e,sys) from e    