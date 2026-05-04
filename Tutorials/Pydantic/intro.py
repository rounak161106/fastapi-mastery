from pydantic import BaseModel
from typing import List, Dict

class Patient(BaseModel):
    name : str
    age : int
    weight : float
    married : bool
    allergies : List[str]    #here we could have used the list keyword but that would have only validated whether the allergies field is a list or not but here we could even check whether the contents within the list is of str type
    contact : Dict[str, str]

def insert_patient(patient : Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact)
    print("inserted successfully")

patient_info = {"name" : "Rounak", "age" : "18", 'weight' : 74.2, 'married' : True, 'allergies' : ['pollen', 'dust'], 'contact' : {'email' : "abc@gmail.com", 'phone' : '7008961001'}}
patient_1 = Patient(**patient_info)

insert_patient(patient_1)