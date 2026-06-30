from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def hellO():
    return {'msg' : 'Hello world'}

@app.get('/about')
def about():
    return {"msg" : "This is about section"}

@app.get('/user/{name}')
def user_details(name):
    return {"msg" : f"Hello {name}"}

