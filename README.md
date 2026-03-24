# Flask API Service Starter

This is a minimal Flask API service starter based on [Google Cloud Run Quickstart](https://cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-service).

## Getting Started

Server should run automatically when starting a workspace. To run manually, run:
```sh
./devserver.sh
```

## To run code
Using command 
```sh
uvicorn main:app --reload
```
---

# FastAPI PostgreSQL CRUD Project

This is a lightweight and robust RESTful API built with Python, [FastAPI](https://fastapi.tiangolo.com/), and SQLAlchemy. It provides standard CRUD (Create, Read, Update, Delete) operations connected to a PostgreSQL database.

## 🏗️ How It Works

The project follows a standard layered architecture to separate concerns:
1. **`database.py`**: Handles the connection to PostgreSQL and manages database sessions. It reads the `DATABASE_URL` from your environment.
2. **`models.py`**: Contains SQLAlchemy ORM classes representing the physical tables in the PostgreSQL database.
3. **`schemas.py`**: Contains Pydantic models. These dictate what data the API expects to receive (Validation) and what it will return (Serialization).
4. **`crud.py`**: The bridge between the API and the database. It houses the reusable functions that perform the actual SQL queries (via SQLAlchemy).
5. **`main.py`**: The entry point. It initializes the FastAPI app, creates the database tables on startup, and defines the API endpoints (Routes).

## 📋 Prerequisites

Before running this project, ensure you have the following installed:
* **Python 3.8+**
* **PostgreSQL server** running locally or remotely.

## 🚀 Setup & Installation

### 1. Clone the repository
Navigate to your desired folder and clone the project.
```bash
git clone <repository-url>
cd fastapi-postgres-crud