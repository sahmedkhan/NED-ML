from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlmodel import SQLModel, create_engine, Session, Field

# Define FastAPI app
app = FastAPI()

# Define data model for student information
class Student(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str
    date_of_birth: str
    sex: str
    email: str
    subject: str

# Database configuration
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)

# Create tables
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

# Function to get a database session
def get_session():
    with Session(engine) as session:
        yield session

# Endpoint to add student information
@app.post("/student/")
def add_student(student: Student, username: str, password: str):
    # Simple authentication
    if username != "admin" or password != "admin":
        raise HTTPException(status_code=401, detail="Unauthorized")

    with get_session() as session:
        session.add(student)
        session.commit()
    return {"message": "Student information added successfully"}

# Endpoint for reporting
@app.get("/report/")
def generate_report(username: str, password: str):
    # Simple authentication
    if username != "admin" or password != "admin":
        raise HTTPException(status_code=401, detail="Unauthorized")

    with get_session() as session:
        students = session.query(Student).all()

    report = "\n".join([f"Name: {student.name}, Date of Birth: {student.date_of_birth}, Sex: {student.sex}, Email: {student.email}, Subject: {student.subject}" for student in students])
    return {"report": report}