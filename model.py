import sqlalchemy 
from pydantic import BaseModel  #Validate dữ liệu đầu vào từ API
from fastapi import FastAPI, Body
from typing import Boolean, Column, ForeignKey, Integer, String
from database import Base


app = FastAPI()


class productType (Base):
    __tablename__ = "productType"

    id= Column(Integer, primary_key=True, index=True)
    product_type_name= Column(String, index=True)

class product (Base):
    __tablename__ = "product"
    id= Column(Integer, primary_key=True, index=True)
    product_type_id= Column(Integer, ForeignKey("productType.id"))
    product_name=Column(String, index=True)
    price=Column(Integer)
    unit=Column(Integer) 
