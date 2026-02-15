import sqlalchemy 
from pydantic import BaseModel 
from fastapi import FastAPI, Body


app = FastAPI()


@app.api_route("/{full_path:path}", methods=["GET"])
    # Log or handle the request as a default
    print(f"Default GET handler called for path: {full_path}")
    
    # You can return a default response or an error
    return {"message": f"Default GET operation for path: /{full_path}. No specific handler found."}


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