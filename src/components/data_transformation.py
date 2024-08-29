import sys
from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from src.exception import CustomException
from src.logger import logging
import os

from src.utils import save_object
from scipy.sparse import csr_matrix

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts', "preprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()

    def get_data_transformer_object(self):
        '''
        This function is responsible for data transformation
        '''
        try:
            numerical_columns = ["Min_Salary", "Max_Salary"]
            categorical_columns = [
                "Job Title",
                # "Job Title",
                # "Position",
                # "Employer",
                # "City",
                # "Province",
                # "Skill",
                "Seniority",
                "Work Type",
                "Industry Type",
            ]

            num_pipeline = Pipeline(
                steps = [
                    ("imputer", SimpleImputer(strategy="median")),
                    ("scaler", StandardScaler(with_mean=False))
                ]
            )

            cat_pipeline=Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="most_frequent")),
                    ("one_hot_encoder", OneHotEncoder()),
                    ("scaler", StandardScaler(with_mean=False))
                ]
            )

            logging.info(f"Categorical columns: {categorical_columns}")
            logging.info(f"Numerical columns: {numerical_columns}")
                             
            preprocessor=ColumnTransformer(
                [
                    ("num_pipeline", num_pipeline, numerical_columns),
                    ("cat_pipelines", cat_pipeline, categorical_columns)
                ]
            )

            return preprocessor
        
        except Exception as e:
            raise CustomException(e, sys)
        
    def initiate_data_transformation(self, train_path, test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info("Read train and test data completed")
            logging.info("Obtaining preprocessing object")

            preprocessing_obj=self.get_data_transformer_object()

            target_column_name = "Avg_Salary"
            numerical_columns = ["Min_Salary", "Max_Salary"]

            input_feature_train_df = train_df.drop(columns = [target_column_name], axis=1)
            target_feature_train_df = train_df[target_column_name]

            input_feature_test_df = test_df.drop(columns=[target_column_name], axis=1)
            target_feature_test_df = test_df[target_column_name]

            logging.info(
                f"Applying preprocessing object on training dataframe and testing dataframe."
            )

            input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessing_obj.transform(input_feature_test_df)

            if isinstance(input_feature_train_arr, csr_matrix):
                rows, cols = input_feature_train_arr.nonzero()
                data = input_feature_train_arr.data

                mapped_feature_train_arr = np.zeros(input_feature_train_arr.shape)

                for row, col, value in zip(rows, cols, data):
                    mapped_feature_train_arr[row, col] = value

                input_feature_train_arr = mapped_feature_train_arr

            if isinstance(input_feature_test_arr, csr_matrix):
                rows, cols = input_feature_test_arr.nonzero()
                data = input_feature_test_arr.data

                mapped_feature_test_arr = np.zeros(input_feature_test_arr.shape)

                for row, col, value in zip(rows, cols, data):
                    mapped_feature_test_arr[row, col] = value

                input_feature_test_arr = mapped_feature_test_arr

            print(type(input_feature_train_arr))
            print(type(input_feature_test_arr))
            print(input_feature_train_arr)
            print("------------------------------")
            print("Shapes before concatenation:")
            print("input_feature_train_arr shape: %s", input_feature_train_arr.shape)
            print("target_feature_train_df shape: %s", np.array(target_feature_train_df).shape)
            print("------------------------------")
            print(target_feature_train_df)
            
            train_arr = np.c_[
                input_feature_train_arr, np.array(target_feature_train_df)
            ]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            logging.info(f"Saved preprocessing object.")

            save_object(
                file_path = self.data_transformation_config.preprocessor_obj_file_path,
                obj = preprocessing_obj
            )

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,
            )

        except Exception as e:
            raise CustomException(e, sys)