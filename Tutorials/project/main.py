from fastapi import FastAPI
import json

app = FastAPI()

def get_data():
    with open('patients_data.json', 'r') as f:
        data = json.load(f)

    return data

@app.get('/')
def home():
    return {'Message' : 'Patient Management System API'}

@app.get('/about')
def about():
    return {'Message' : "A fully functional api to manage patient's records"}

@app.get('/view')
def view():
    return get_data()