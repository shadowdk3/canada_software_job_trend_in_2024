import pytest
import sys
sys.path.append('..')
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200

def test_predict_datapoint(client):
    response = client.post('/predictdata', data={
        'job_title': 'Senior Business Analysts',
        'job_info': 'Computer ProgrammerAnalyst',
        'position': 'Data Officer',
        'employer': 'The City of Vancouver',
        'city': 'Berwick',
        'province': 'ON',
        'skill': 'Python',
        'seniority': 'Mid',
        'work_type': 'In-Person',
        'industry_type': 'Transportation',
        'min_salary': '50000',
        'max_salary': '80000'
    })
    assert response.status_code == 200

