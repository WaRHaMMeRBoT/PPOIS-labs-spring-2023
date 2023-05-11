from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    course = Column(Integer, nullable=False)
    works_number = Column(Integer, nullable=False)
    completed_works = Column(Integer, nullable=False)
    programming_language = Column(String, nullable=False)
