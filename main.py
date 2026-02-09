import os
from dotenv import load_dotenv
from fastapi import FastAPI


load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

print(f"Connecting to database at: {DATABASE_URL}")
