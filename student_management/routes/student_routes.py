from fastapi import APIRouter, HTTPException, status
from pymongo import MongoClient
from bson.objectid import ObjectId  # Needed to handle MongoDB's ObjectId
from models import Student
from dotenv import load_dotenv
import os

load_dotenv()

router = APIRouter()
client = MongoClient(os.getenv("MONGO_URI"))
db = client.student_db  # Database name
collection = db.students  # Collection name

# Create a new student
@router.post("/students/", response_model=dict)
def create_student(student: Student):
    student_dict = student.dict()
    result = collection.insert_one(student_dict)
    if result.inserted_id:
        student_dict["_id"] = str(result.inserted_id)  # Convert ObjectId to string
        return {"message": "Student created successfully", "student": student_dict}
    raise HTTPException(status_code=500, detail="Failed to create student")

# Retrieve all students
@router.get("/students/", response_model=dict)
def get_students():
    students = list(collection.find({}, {"_id": 0}))  # Exclude MongoDB ObjectId
    return {"students": students}

# Retrieve a student by ID
@router.get("/students/{student_id}", response_model=dict)
def get_student(student_id: str):
    try:
        student = collection.find_one({"_id": ObjectId(student_id)})
        if student:
            student["_id"] = str(student["_id"])
            return {"student": student}
        raise HTTPException(status_code=404, detail="Student not found")
    except:
        raise HTTPException(status_code=400, detail="Invalid student ID")

# Delete a student
@router.delete("/students/{student_id}")
def delete_student(student_id: str):
    result = collection.delete_one({"_id": ObjectId(student_id)})
    if result.deleted_count == 1:
        return {"message": "Student deleted successfully"}
        raise HTTPException(status_code=404, detail="Student not found")