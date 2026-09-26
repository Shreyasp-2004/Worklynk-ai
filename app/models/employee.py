from pydantic import BaseModel, EmailStr

class Employee(BaseModel):
    id: int
    employee_id: str
    name: str
    email: EmailStr
    department: str
    role: str