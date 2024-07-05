# models.py

from sqlmodel import SQLModel, Field

class Student(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str
    dob: str
    sex: str
    email: str
    subject: str