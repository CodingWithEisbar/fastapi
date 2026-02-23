'''
import os
from dotenv import load_dotenv
from fastapi import FastAPI


load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

print(f"Connecting to database at: {DATABASE_URL}")


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
                                 
'''
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models
import schemas
import crud
from database import engine, get_db

# Create the database tables if they don't exist
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI PostgreSQL CRUD")

@app.post("/items/", response_model=schemas.ItemResponse)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_item(db=db, item=item)

@app.get("/items/", response_model=list[schemas.ItemResponse])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items

@app.get("/items/{item_id}", response_model=schemas.ItemResponse)
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_item = crud.get_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@app.put("/items/{item_id}", response_model=schemas.ItemResponse)
def update_item(item_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)):
    db_item = crud.update_item(db, item_id=item_id, item=item)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@app.delete("/items/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    db_item = crud.delete_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item deleted successfully"}