# sometimes we want to have nested models in our application, for example if we want to have an address model which contains the street, city, state and zip code of the patient and we want to use that address model in our patient model then we can create a separate address model and use that address model in our patient model, this way we can keep our code organized and also we can reuse the address model in other models if needed

from pydantic import BaseModel, Field
from typing import List, Dict, Optional

class Address(BaseModel):
    street : str
    city : str
    state : str
    zip_code : str

class Patient(BaseModel):
    name : str
    age : int
    gender : str
    address : Address   

address_dict = {"street" : "123 Main St", "city" : "New York", "state" : "NY", "zip_code" : "10001"}

address1 = Address(**address_dict)  

patient_dict = {"name" : "Rounak", "age" : 30, "gender" : "Male", "address" : address1}
patient = Patient(**patient_dict)

def print_patient_details(patient : Patient):
    print(patient)
    print(patient.name)
    print(patient.age)
    print(patient.gender)
    print(patient.address.street)   
    print(patient.address.city)
    print(patient.address.state)
    print(patient.address.zip_code)

print_patient_details(patient)