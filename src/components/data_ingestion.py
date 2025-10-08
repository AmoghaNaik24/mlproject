# data_ingestion.py

import os

# Ensure artifacts folder exists immediately
os.makedirs('artifacts', exist_ok=True)

import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

# Package imports
from src.exception import CustomException
from src.logger import logging
from src.components.data_transformation import DataTransformation, DataTransformationConfig
from src.components.model_trainer import ModelTrainer, ModelTrainerConfig

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', "train.csv")
    test_data_path: str = os.path.join('artifacts', "test.csv")
    raw_data_path: str = os.path.join('artifacts', "data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            # Safe CSV path for Windows
            csv_path = r'notebook\data\stud.csv'
            if not os.path.exists(csv_path):
                raise FileNotFoundError(f"CSV file not found at {csv_path}")

            # Read dataset
            df = pd.read_csv(csv_path)
            logging.info('Dataset read successfully')
            print("Dataset read successfully")

            # Save raw data
            print("Saving raw CSV...")
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            print("Raw CSV saved!")

            # Train-test split
            print("Splitting dataset...")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            print("Train-test split done!")

            # Save train and test sets
            print("Saving train CSV...")
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            print("Train CSV saved!")

            print("Saving test CSV...")
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            print("Test CSV saved!")

            logging.info("Ingestion of the data is completed")
            return self.ingestion_config.train_data_path, self.ingestion_config.test_data_path

        except Exception as e:
            raise CustomException(e, sys)

if __name__ == "__main__":
    try:
        # Data ingestion
        obj = DataIngestion()
        train_data, test_data = obj.initiate_data_ingestion()

        # Data transformation
        data_transformation = DataTransformation()
        train_arr, test_arr, _ = data_transformation.initiate_data_transformation(train_data, test_data)

        # Model training
        model_trainer = ModelTrainer()
        print(model_trainer.initiate_model_trainer(train_arr, test_arr))

    except Exception as e:
        print(f"Error occurred: {e}")
