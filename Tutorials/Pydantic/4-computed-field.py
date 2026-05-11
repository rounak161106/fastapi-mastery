#if we want to compute to add some field which is not provided by the user, but our business logic requires that field to be there then we can use computed_field decorator to add that field to the model, eg. if we want to calculate bmi based on height and weight of the patient and we want to add that bmi field to the model then we can use computed_field decorator to add that field to the model

from pydantic import BaseModel, computed_field, EmailStr
from typing import List, Dict, Optional

class Patient(BaseModel):
    name : str
    age : int
    email : EmailStr
    height : float
    weight : float 
    married : bool
    allergies : List[str]
    contact : Dict[str, str]

    @computed_field
    @property
    def bmi(self) -> float:
        return self.weight / (self.height ** 2)

def insert_patient(patient : Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.height)
    print(patient.bmi)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact)
    print(patient.email)
    print("inserted successfully")

patient_info = {"name" : "Rounak", 'weight' : 74.2, 'height' : 1.75, 'age' : '52', 'allergies' : ['pollen', 'dust'], 'contact' : {'phone' : '7008961001'}, 'email' : "abc@sbi.com", 'married' : False}
patient = Patient(**patient_info)
insert_patient(patient)