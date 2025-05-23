from fastapi import FastAPI
from .database import engine, Base



app = FastAPI()


# Create database tables
@app.on_event("startup")
def create_tables():
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully!")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Leave and Attendance Management System"}
