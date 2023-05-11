from fastapi import APIRouter
from app.schemas import StudentCreateModel, StudentModel, StudentListModel
from app.orm_commands import add_new_student, get_students, get_student_by_id, delete_student_by_id

router = APIRouter(
    prefix="/students",
    tags=["students"],
)


@router.post(path="/create-student", summary="Endpoint for creating students")
async def create_student(data: StudentCreateModel):
    student = {
        "full_name": data.full_name,
        "course": data.course,
        "works_number": data.works_number,
        "completed_works": data.completed_works,
        "programming_language": data.programming_language
    }
    add_new_student(student)
    return {
        "data": "new student was created"
    }


@router.get(path="/get-student/{id}", summary="Getting data about definite student", response_model=StudentModel)
async def get_student_info(id: int):
    student = get_student_by_id(id)
    return student


@router.get(path="/all-students", summary="Getting data about all the students")
async def get_all_data():
    students = get_students()
    return students


@router.delete(path="/delete-student/{id}", summary="Deleting student by id")
async def delete_student(id: int):
    delete_student_by_id(id)
    return {
        "data": "Student was deleted"
    }
