from pydantic import BaseModel, EmailStr, AnyUrl, Field  #field is for data validation and also for adding extra information to the api documentation
from typing import List, Dict, Optional, Annotated #working without annotated is fine but with annotated, we can combine the type as well as the field function to add extra information and validation to the api documentation in a more cleaner way

# step 1 : create a model mainly the schema for the data we want to validate
class Patient(BaseModel):
    name : str = Field(max_length=50)
    # age : Optional[int] = Field(default=None,gt=5, lt=80)
    age : Annotated[str, Field(max_length=50, title="age of the patient", description="give the age", examples=[53,26])]
    linkedln : AnyUrl
    email : EmailStr
    weight : Annotated[float, Field(gt=0, strict=True)] #with strict we can prevent the float value coming in string format(normally without strict, if we pass weight as "74.2" it will be converted to float but with strict it will raise a validation error)
    married : Optional[bool] = False           #here optional is not necessary because we have already given a default value to the married field but it is still a good practice to use optional for better readability and understanding of the code
    allergies : Optional[List[str]] = Field(max_length=5)   #here we could have used the list keyword but that would have only validated whether the allergies field is a list or not but here we could even check whether the contents within the list is of str type
    contact : Dict[str, str] = Field(max_length=2,description="contact details of the patient in key value pair format")

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

patient_info = {"name" : "Rounak", 'weight' : 74.2, 'age' : '52', 'allergies' : ['pollen', 'dust'], 'contact' : {'phone' : '7008961001'}, 'email' : "abc@gmail.com", 'linkedln' : 'http://linkedln.com/5135'}

# step 2 : create an instance of the model and pass the data to
patient_1 = Patient(**patient_info)

# step 3 : use the model instance to access the data and perform operations
insert_patient(patient_1)