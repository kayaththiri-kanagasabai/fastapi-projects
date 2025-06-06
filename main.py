from fastapi import FastAPI   # import FastAPI from fastapi module
from pydantic import BaseModel,Field # import BaseModel from pydantic module


app = FastAPI()  # create an instance/object of ABI



@app.get("/")  # define a route for the root URL  (decorate the function with @app.get)


# simple python function
def index():
    return {'data':{'name':'vaaththiii'}}


@app.get('/about')  # define a route for the about URL
def about():
    return {'data':'about page'}