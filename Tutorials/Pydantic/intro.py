from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional

class Patient(BaseModel):
    name : str = Field(max_length=50)
    age : Optional[int] = Field(default : None,gt=5, lt=80)
    linkedln : AnyUrl
    email : EmailStr
    weight : float = Field(gt=0)
    married : bool
    allergies : List[str] = Field(max_length=5)   #here we could have used the list keyword but that would have only validated whether the allergies field is a list or not but here we could even check whether the contents within the list is of str type
    contact : Dict[str, str]

def insert_patient(patient : Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact)
    print(patient.email)
    print(patient.linkedln)
    print("inserted successfully")

patient_info = {"name" : "Rounak", 'weight' : 74.2, 'married' : True, 'allergies' : ['pollen', 'dust'], 'contact' : {'phone' : '7008961001'}, 'email' : "abc@gmail.com", 'linkedln' : 'http://linkedln.com/5135'}
patient_1 = Patient(**patient_info)

insert_patient(patient_1)