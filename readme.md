# Canada Software Job Trend in 2024

## Setup Environment

- Install required package

`pip install -r requirements.txt`

## Summary

- [Data Ingestion](#data-ingestion)
- [Data Transformation](#data-transformation)
- [Model Trainer](#model-trainer)
- [Flask](#flask)
- [Pytest](#pytest)
- [EDA](#eda)

## Project Structure

### [Data Ingestion](https://github.com/shadowdk3/canada_software_job_trend_in_2024/blob/master/src/components/data_ingestion.py)

- Read data from a CSV file using `Pandas`
- Modify the function to handle different data formats or sourse
- Preprocessing steps can be added within the function as needed
- In this example, we split the CSV file into test and train data set

### [Data Transformation](https://github.com/shadowdk3/canada_software_job_trend_in_2024/blob/master/src/components/data_transformation.py)

- encapsulates a specific data transformation task such as cleaning data, scaling features, encoding categorical variables, or feature engineering
- These functions are designed to take input data, perform the desired transformation, and return the transformed data
- The use of popular libraries like `Pandas` and `scikit-learn` (for StandardScaler) makes it easier to work with and manipulate the data effectively
- The functions are designed to be modular and reusable, allowing you to call them as needed in your data analysis pipeline

### [Model Trainer](https://github.com/shadowdk3/canada_software_job_trend_in_2024/blob/master/src/components/model_trainer.py)

- Training and evaluating regression models for a data analysis project
- Initializes, trains, evaluates, and selects the best performing regression model from a set of algorithms
- This file is crucial for automating the model training process and ensuring the selection of the best model for predictive analytics tasks

### [Flask](https://github.com/shadowdk3/canada_software_job_trend_in_2024/blob/master/app.py)

- Flask is a lightweight Python web framework that is commonly used for developing web applications
- Flask can serve as the backend system that exposes the ML model's functionality over HTTP

![](/ref/flask.png)

## Test

### [Pytest](https://github.com/shadowdk3/canada_software_job_trend_in_2024/blob/master/tests/test_app.py)

- Testing framework for Python that makes it easy to write simple and scalable tests
- `pytest` is widely used in the Python community due to its simplicity, flexibility, and powerful features, making it a popular choice for writing tests for Python projects of any size

## [EDA](https://github.com/shadowdk3/canada_software_job_trend_in_2024/blob/master/notebook/EDA_Canada_Software_Job_Trend_2024.ipynb)

The puroise of this project is to master the exploratory data analsis (EDA) in Canada Software Job Trend in 2024

### Library

- numpy
- pandas
- seaborn
- matplotlib

### Data

https://www.kaggle.com/datasets/amanbhattarai695/data-analyst-job-roles-in-canada/data

- Job Title: A generalized job title that encapsulates the role.
- Job Info: The exact job title as listed on the job sites.
- Position: The specific role or category the job falls under.
- Employer: The name of the hiring company.
- City: The job's location.
- Province: The abbreviated province name corresponding to the city.
- Skill: The programming languages and tools required for the job.
- Seniority: The job's seniority level (Senior, Mid, Junior, any).
- Work Type: Specifies if the job is Remote, In-person, or Hybrid.
- Industry Type: The industry to which the employer belongs.
- Min Salary: The lowest salary listed (as a float).
- Max Salary: The highest salary listed (as a float).
- Average Salary: The mean salary (as a float).

### Visualize

#### Visualize the salary with the job title 

![](/ref/visualize_job_title.png)

#### Visualize top 10 job title 

![](/ref/top_10_job_title.png)

#### Visualize the salary with the job Infomation

![](/ref/top_10_job_info.png)

#### Visualize the salary with position

![](/ref/visualize_position.png)

#### Visualize the salary with employer

![](/ref/top_10_employer.png)

#### Visualize the salary with city

![](/ref/top_10_city.png)

#### Visualize the salary with Province

![](/ref/visualize_province.png)

#### Visualize the salary with Skill

![](/ref/top_10_skill.png)

#### Visualize the salary with Seniority

![](/ref/visualize_seniority.png)

#### Visualize the salary with Work Type

![](/ref/visualize_work_type.png)

#### Visualize the salary with Industry Type

![](/ref/visualize_industry_type.png)

#### Salary Box Plot

![Average Salary](/ref/boxplot_avg_salary.png)
![Maximum Salary](/ref/boxplot_max_salary.png)
![Minimum Salary](/ref/boxplot_min_salary.png)

### Conclusions

- Salary data range: $30,240.56 to $180,000.00, with an average of $78,434.73.
- Distribution skew: Average aligns with 75th percentile, indicating right-skewed distribution.
- Job titles: Average salaries range from $66,000 to over $90,000; specialized roles command higher pay.
- Geographic trends: Quebec has highest average at $131,093.33; varied averages across regions.
- Industry disparities: Legal, Retail, Consulting offer competitive salaries; Real Estate, Travel show lower averages.
- Impact of skills and seniority: Skills like Bilingual, Tableau, Python, and senior roles lead to higher salaries.
- Work types and salaries: In-Person work type has highest average; Remote work type follows closely.
- Industry influences: Technology, Healthcare offer above $80,000 average salaries.
- Dataset overview: 1796 data points; mean salary $78,434.73, standard deviation $18,026.99.