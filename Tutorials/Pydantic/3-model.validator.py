# model_validator are used when we want to perform some custom validations on more than one field of the model or we want to perform some validation on the entire model according to our business requirements and also converts the data into the desired format before performing any operations, eg. if we have a case where we want to ensure that if the age of the parient is greater than 60 then the patient should have an emergency phone number

from pydantic import BaseModel, model_validator, EmailStr
from typing import List, Dict, Optional

class Patient(BaseModel):
    name : str
    age : int
    email : EmailStr
    weight : float 
    married : bool
    allergies : List[str]
    contact : Dict[str, str]

    @model_validator(mode='after')
    @classmethod
    def validate_emergency_contact(cls, model):
        if model.age>60 and 'emergency_phone' not in model.contact:
                raise ValueError("Patients above 60 must have an emergency phone number in the contact details")
        return model

def insert_patient(patient : Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact)
    print(patient.email)
    print("inserted successfully")

patient_info = {"name" : "Rounak", 'weight' : 74.2, 'age' : '32', 'allergies' : ['pollen', 'dust'], 'contact' : {'phone' : '7008961001',}, 'email' : "abc@sbi.com", 'married' : False}
patient = Patient(**patient_info)
insert_patient(patient)