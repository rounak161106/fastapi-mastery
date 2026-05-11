from fastapi import FastAPI, Path, HTTPException, Query
#path is used to perform, validation, adding description to the api documentation
import json

app = FastAPI()

def get_data():
    with open('patients_data.json', 'r') as f:
        data = json.load(f)
    return data


#simple retrieving the data(implementing get request)
@app.get('/')
def home():
    return {'Message' : 'Patient Management System API'}

@app.get('/about')
def about():
    return {'Message' : "A fully functional api to manage patient's records"}

@app.get('/view')
def veeiew():
    return get_data()

@app.get('/view/{id}')
def view_id(id = Path(..., description="Id of the patient in the DB", example="P001")):
    data = get_data()
    if id in data:
        return data[id]
    raise HTTPException(status_code=404, detail="Patient not found")

@app.get('/sort')
def sort_patients(sortby : str = Query(...,description = "Sort on the basis of height, weight or bmi", example='height'), order: str = Query("asc", description = 'Specify the order asc or desc')):
    data = get_data()
    valid = ['height', 'weight', 'BMI']
    if sortby not in valid:
        raise HTTPException(status_code=400, detail=f"Select valid option from {valid}")
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail='Select either asc or desc')
    order = True if order == "desc" else False  
    sorted_data = sorted(data.values(), key = lambda x : x[sortby], reverse=order)
    return sorted_data

#adding new patient(implementing post request)