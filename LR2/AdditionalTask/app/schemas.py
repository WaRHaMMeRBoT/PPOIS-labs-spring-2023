from pydantic import BaseModel
from typing import List


class StudentCreateModel(BaseModel):
    full_name: str
    course: int
    works_number: int
    completed_works: int
    programming_language: str


class StudentModel(BaseModel):
    id: int
    full_name: str
    course: int
    works_number: int
    completed_works: int
    programming_language: str


class StudentListModel(BaseModel):
    students: List[StudentCreateModel]
