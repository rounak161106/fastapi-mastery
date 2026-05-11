from pydantic import BaseModel
class Address(BaseModel):
    street : str
    city : str
    state : str
    zip_code : str

class Patient(BaseModel):
    name : str
    age : int = None
    gender : str
    address : Address   

address_dict = {"street" : "123 Main St", "city" : "New York", "state" : "NY", "zip_code" : "10001"}

address1 = Address(**address_dict)  

patient_dict = {"name" : "Rounak", "gender" : "Male", "address" : address1}
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

# print_patient_details(patient)

temp = patient.model_dump()  #model_dump is used to convert the model instance into a dictionary format which can be easily serialized and stored in a database or sent over the network
print(temp)

temp2 = patient.model_dump_json()  #model_dump_json is used to convert the model instance into a json format which can be easily serialized and stored in a database or sent over the network
print(temp2)    

temp3 = patient.model_dump_json(indent=6)  #with indent we can make the json output more readable and organized
print(temp3)    

temp4 = patient.model_dump(exclude=['gender'])  #with exclude(or include) we can exclude/include  some fields from the json output which we don't want to include in the json output
print(temp4)

temp5 = patient.model_dump(exclude_unset=True)  #with exclude_unset we can exclude the fields which are not set by the user and have default values in the model, this is useful when we want to only include the fields which are provided by the user in the json output
print(temp5)