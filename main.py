from networkSecurity.components.data_ingestion import DataIngestion
from networkSecurity.components.data_validation import DataValidation
from networkSecurity.components.model_trainer import ModelTrainer
from networkSecurity.components.data_transformation import DataTransformation
from networkSecurity.exception.exception import NetworkSecurityException
from networkSecurity.logging.logger import logging
from networkSecurity.entity.config_entity import DataIngestionConfig, DataValidationConfig, DataTransformationConfig, ModelTrainerConfig
from networkSecurity.entity.config_entity import TrainingPipelineConfig

import sys

if __name__=='__main__':
    try:
        trainingpipelineconfig= TrainingPipelineConfig()
        dataingestionconfig = DataIngestionConfig(trainingpipelineconfig)
        data_ingestion =DataIngestion(dataingestionconfig)
        logging.info("Initiate the data ingestion.")
        dataingestionartifact = data_ingestion.initiate_data_ingestion()
        logging.info("Data ingestion Completed.")
        print(dataingestionartifact)
        data_validation_config= DataValidationConfig(trainingpipelineconfig)
        data_validation= DataValidation(dataingestionartifact, data_validation_config)
        logging.info("Initiate the data validation.")
        data_validation_artifact=data_validation.initiate_data_validation()
        logging.info("Data validation Completed.")
        data_transformation_config = DataTransformationConfig(trainingpipelineconfig)
        data_transformation = DataTransformation(data_validation_artifact,data_transformation_config)
        logging.info("Initiate the data transformation.")
        data_transformation_artifact= data_transformation.initiate_data_transformation()
        logging.info("Data transformation Completed.")
        print(data_transformation_artifact)

        logging.info("Model Training Started.")
        model_trainer_config = ModelTrainerConfig(trainingpipelineconfig)
        model_trainer= ModelTrainer(model_trainer_config=model_trainer_config, data_transformation_artifact=data_transformation_artifact)
        model_trainer_arifact = model_trainer.initiate_model_trainer()
        logging.info("Model Training artifact created.")

    except Exception as e:
        raise NetworkSecurityException(e,sys)