from fastapi import FastAPI, Path
from typing import Optional
from pydantic import  BaseModel
app = FastAPI()

"""GET - GET AN INFORMATION
POST - CREATE SOMETHING NEW
PUT - UPDATE SOMETHING
DELETE - DELETE SOMETHING"""

students = { 
    1: {
        "name": "john",
        "age": 17,
        "class": "year 12"

    }
}

class Student(BaseModel):
    name: str
    age: int
    year: str

class UpdateStudent(BaseModel):
    name: Optional[str] =   None
    age: Optional[int] = None
    year: Optional[str] =  None

# GET
@app.get("/") # home page

def index():
    return {"name": "First Data"}

# Path parameter
@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path (description="The ID of the student you want to view", gt=0, lt=3)):
    return students[student_id]

# Query parameter
@app.get("/get-by-name")
def get_student(*, name: Optional[str] = None, test: int):
    for student_id in students:
        if students[student_id]['name'] == name:
            return students[student_id]
    return {"Data": "Not found"}

# Path and Query parameters combined
@app.get("/get-by-name/{student_id}")
def get_student(*,student_id: int, name: Optional[str] = None, test: int):
    for student_id in students:
        if students[student_id]['name'] == name:
            return students[student_id]
    return {"Data": "Not found"}

# POST
@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return{"Error": "Student exists"}
    
    students[student_id] = student
    return students[student_id]

#PUT
@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {"Error": "Student does not exist"}
    
    if student.name != None:
        students[student_id].name = student.name

    if student.age != None:
        students[student_id].age = student.age    
    
    if student.year != None:
        students[student_id].year = student.year

    return students[student_id]

# DELETE
@app.delete("/delete/{student_id}")
def delete_Student(student_id: int):
    if student_id not in students:
        return{"Error": "Student does not exist"}
    del students[student_id]
    return{"Message": "Student id deleted"}
