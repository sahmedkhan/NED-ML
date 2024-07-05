from sqlmodel import Session, SQLModel, create_engine
from models import Student

DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL)

def create_student(student_data):
    with Session(engine) as session:
        student = Student(**student_data)
        session.add(student)
        session.commit()
        session.refresh(student)
        return student