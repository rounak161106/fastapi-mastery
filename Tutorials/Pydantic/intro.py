from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name : str = Field(max_length=50)
    # age : Optional[int] = Field(default=None,gt=5, lt=80)
    age : Annotated[str, Field(max_length=50, title="age of the patient", description="give the age", examples=[53,26])]
    linkedln : AnyUrl
    email : EmailStr
    weight : Annotated[float, Field(gt=0, strict=True)] #with sstrict we can prevent the float value coming in string format
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

patient_info = {"name" : "Rounak", 'weight' : 74.2, 'age' : '52','married' : True, 'allergies' : ['pollen', 'dust'], 'contact' : {'phone' : '7008961001'}, 'email' : "abc@gmail.com", 'linkedln' : 'http://linkedln.com/5135'}
patient_1 = Patient(**patient_info)

insert_patient(patient_1)