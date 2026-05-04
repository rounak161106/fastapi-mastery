from pydantic import BaseModel
from typing import List

class Patient(BaseModel):
    name : str
    age : int
    weight : float
    married : bool
    allergies : List[str]
    contact : dict

def insert_patient(patient : Patient):
    print(patient.name)
    print(patient.age)
    print("inserted successfully")

patient_info = {"name" : "Rounak", "age" : "18"}
patient_1 = Patient(**patient_info)

insert_patient(patient_1)