from flask import Flask, request, render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredicPipeline

application = Flask(__name__)

app = application

## Route for a home page

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html')
    else:
        data=CustomData(
            job_title = request.form.get('job_title'),
            job_info = request.form.get('job_info'),
            position = request.form.get('position'),
            employer = request.form.get('employer'),
            city = request.form.get('city'),
            province = request.form.get('province'),
            skill = request.form.get('skill'),
            seniority = request.form.get('seniority'),
            work_type = request.form.get('work_type'),
            industry_type = request.form.get('industry_type'),
            min_salary = float(request.form.get('min_salary')),
            max_salary = float(request.form.get('max_salary')),
        )
        pred_df = data.get_data_as_data_frame()
        print(pred_df)

        predict_pipeline = PredicPipeline()
        results = predict_pipeline.predict(pred_df)
        return render_template('home.html', results=results[0])

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)