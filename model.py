import sqlalchemy 
from pydantic import BaseModel 
from fastapi import FastAPI, Body


app = FastAPI()

@app.get("/")
def root ():
    return {"Hello":"World"}


@app.get("/about")
def detail ():
    return {"This is about me"}


@app.get("/report")
def detail ():
    return {"This is about me"}


@app.post("/")
def addItem(task:str):
    newId = len(fakeDatabase.keys()) + 1
    fakeDatabase[newId] = {"task":task}
    return {"Data post successfully"}