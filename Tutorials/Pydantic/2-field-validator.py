# field_validator are used when we want to perform some custom validation on the fields of the model according to our business requirements and also converts the data into the desired format before performing any operations

from pydantic import BaseModel, field_validator, EmailStr
from typing import List, Dict, Optional

class Patient(BaseModel):
    name : str
    age : int
    email : EmailStr
    weight : float 
    married : bool
    allergies : List[str]
    contact : Dict[str, str]

    @field_validator('email')
    @classmethod
    def validate_email(cls, value):
        valid_domains = ['hdfc.com', 'icici.com', 'sbi.com']
        domain = value.split('@')[-1]
        if domain not in valid_domains:
            raise ValueError(f"Email domain must be one of {valid_domains}")
        return value
    
    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        return value.title()  #this will convert the first letter of each word in the name to uppercase and rest to lowercase
    
    @field_validator('age', mode='after') #by default the validation is done in after mode which means that the data is first converted to the desired type and then the validation is performed but in some cases we might want to perform the validation before the data is converted to the desired type and for that we can use the mode parameter of the field_validator decorator and set it to before, eg. if we send age = '43' in the input data then before converting it to int we can check whether the age is a valid number or not and if it is not a valid number then we can raise a validation error but this was not possible if the mode was after because in that case the age would have been first converted to int and then the validation would have been performed and if the age was not a valid number then it would have raised a validation error while converting the age to int and we would not have been able to raise a custom validation error with a custom message
    @classmethod
    def validate_age(cls, value):
        if value < 0 or value > 120:
            raise ValueError("Age must be between 0 and 120")
        return value
    

def insert_patient(patient : Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact)
    print(patient.email)
    print("inserted successfully")

patient_info = {"name" : "Rounak", 'weight' : 74.2, 'age' : '52', 'allergies' : ['pollen', 'dust'], 'contact' : {'phone' : '7008961001'}, 'email' : "abc@sbi.com", 'married' : False}
patient = Patient(**patient_info)
insert_patient(patient)