from pydantic import BaseModel,EmailStr, Field
from typing import Optional, Annotated

class Student(BaseModel):
    name: str = "nitish"
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(default=5, gt=0, lt=10,  description="represnt the student cgpa")
    # cgpa: Optional[float] = Field(default=None, gt=0, lt=10)




new_stundet = {'name': 'subhadip', 'email':"abcd@gmail.com", 'cgpa': 7}
student = Student(**new_stundet)

print(student)
student_dict = dict(student)
print(student_dict)