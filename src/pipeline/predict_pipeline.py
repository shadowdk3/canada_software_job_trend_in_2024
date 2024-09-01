import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object

class PredicPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            model_path = 'artifacts/model.pkl'
            preprocessor_path = 'artifacts/preprocessor.pkl'
            model = load_object(file_path = model_path)
            preprocessor = load_object(file_path = preprocessor_path)
            data_scaled = preprocessor.transform(features)
            preds = model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise CustomException(e, sys)

class CustomData:
    def __init__(self,
        job_title: str,
        job_info: str,
        position: str,
        employer: str,
        city: str,
        province: str,
        skill: str,
        seniority: str,
        work_type: str,
        industry_type: str,
        min_salary: float,
        max_salary: float):

        self.job_title = job_title
        self.job_info = job_info
        self.position = position
        self.employer = employer
        self.city = city
        self.province = province
        self.skill = skill
        self.seniority = seniority
        self.work_type = work_type
        self.industry_type = industry_type
        self.min_salary = min_salary
        self.max_salary = max_salary

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "Job Title": [self.job_title],
                "Job Info": [self.job_info],
                "Position": [self.position],
                "Employer": [self.employer],
                "City": [self.city],
                "Province": [self.province],
                "Skill": [self.skill],
                "Seniority": [self.seniority],
                "Work Type": [self.work_type],
                "Industry Type": [self.industry_type],
                "Min_Salary": [self.min_salary],
                "Max_Salary": [self.max_salary],
            }

            return pd.DataFrame(custom_data_input_dict)
        
        except Exception as e:
            raise CustomException(e, sys)



