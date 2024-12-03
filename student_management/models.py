from pydantic import BaseModel, Field
from typing import Optional

class Student(BaseModel):
    name: str = Field(..., example="John Doe")
    age: int = Field(..., example=20)
    course: str = Field(..., example="Computer Science")
    email: Optional[str] = Field(None, example="john.doe@example.com")