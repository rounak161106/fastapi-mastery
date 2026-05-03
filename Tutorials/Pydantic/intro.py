from pydantic import BaseModel

class Patient(BaseModel):
    name : str
    age : int

def insert_patient(patient : Patient):
    print(patient.name)
    print(patient.age)
    print("inserted successfully")

patient_info = {"name" : "Rounak", "age" : "18"}
patient_1 = Patient(**patient_info)

insert_patient(patient_1)