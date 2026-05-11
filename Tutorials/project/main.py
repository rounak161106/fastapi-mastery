from fastapi import FastAPI, Path, HTTPException, Query #path is used to perform, validation, adding description to the api documentation(similarly the query)
from pydantic import BaseModel, computed_field, Field
from typing import Annotated, Literal, Optional
import json
from fastapi.responses import JSONResponse

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
        
class PatientUpdate(BaseModel):
    name : Annotated[str, Field(default=None, description="Name of the patient", examples=['xyz'])]
    city : Annotated[str, Field(default=None, description="City of the patient", examples=['Barbil'])]
    age : Annotated[int, Field(default=None, description="Age of the patient", examples=[19], gt=0, lt=120)]
    gender : Annotated[Literal['Male', 'Female', 'Others'], Field(default=None, description="Gender of the patient")]
    height : Annotated[float, Field(default=None,gt=0, description="Height of the patient(in metres)", examples=[1.85])]
    weight : Annotated[float, Field(default=None,gt=0, description="Weight of the patient(in kgs)", examples=[65.6])]

def get_data():
    with open('patients_data.json', 'r') as f:
        data = json.load(f)
    return data

def save_data(data):
    with open('patients_data.json', 'w') as f:
        json.dump(data, f)

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
    save_data(data)
    return JSONResponse(status_code=201, content = {'message' : 'Patient created successfully'})        

#updating patient(implementing put request)
@app.put('/edit/{patient_id}')
def update_patient(patient_update : PatientUpdate, patient_id : str = Path(..., description="Id of the patient", examples=['P001'])):
    data = get_data()
    if patient_id not in data:
        raise HTTPException(status_code=404, detail="Patient not found")
    this_patient_info = data[patient_id]
    updated_patient_info = patient_update.model_dump(exclude_unset=True)
    for key, value in updated_patient_info.items():
        this_patient_info[key] = value

    this_patient_info["id"] = patient_id
    patient_pyd_obj = Patient(**this_patient_info)
    this_patient_info = patient_pyd_obj.model_dump(exclude='id')
    data[patient_id] = this_patient_info
    save_data(data)
    return JSONResponse(status_code=200, content={"Message" : "Patient Updated"})

#deleting patient(implementing delete request)
@app.delete('/delete/{patient_id}')
def delete_patient(patient_id : str = Path(..., description="Id of the patient")):
    data = get_data()
    if patient_id not in data:
        raise HTTPException(status_code=404, detail="Patient not found")
    del data[patient_id]
    save_data(data)
    return JSONResponse(status_code=200, content={'message' :'Patient deleted'})