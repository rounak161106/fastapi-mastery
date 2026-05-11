from fastapi import FastAPI, Path, HTTPException, Query #path is used to perform, validation, adding description to the api documentation(similarly the query)
from pydantic import BaseModel, computed_field, Field
from typing import Annotated, Literal
import json

app = FastAPI()

class Patient(BaseModel):
    id : Annotated[str, Field(...,description="Id of the patient", examples=['P001'])]
    name : Annotated[str, Field(..., description="Name of the patient", examples=['xyz'])]
    city : Annotated[str, Field(..., description="City of the patient", examples=['Barbil'])]
    age : Annotated[int, Field(..., description="Age of the patient", examples=[19], gt=0, lt=120)]
    gender : Annotated[Literal['Male', 'Female', 'Others'], Field(..., description="Gender of the patient")]
    height : Annotated[float, Field(...,gt=0, description="Height of the patient(in metres)", examples=[1.85])]
    weight : Annotated[float, Field(...,gt=0, description="Weight of the patient(in kgs)", examples=[65.6])]

    @computed_field
    @property
    def bmi(self) -> float:
        return round(self.weight / (self.height**2),2)
        
    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return "Underweight"
        elif self.bmi < 25:
            return "Normal"
        elif self.bmi < 30:
            return "Overweight"
        else:
            return "Obesity"

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
def view():
    return get_data()

@app.get('/view/{id}')
def view_id(id = Path(..., description="Id of the patient in the DB", examples=["P001"])):
    data = get_data()
    if id in data:
        return data[id]
    raise HTTPException(status_code=404, detail="Patient not found")

@app.get('/sort')
def sort_patients(sortby : str = Query(...,description = "Sort on the basis of height, weight or bmi", examples=['height']), order: str = Query("asc", description = 'Specify the order asc or desc')):
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
@app.post('/create')
def create_patient(patient : Patient):
    #load existing data
    data = get_data()
    #check if that patient id already exists
    if(patient.id in data):
        raise HTTPException(status_code=400, detail="Patient already exists")
    
    #new patient add to database
    data[patient.id] = patient.model_dump(exclude=['id'])
    return {'msg' : 'Added successfully'}