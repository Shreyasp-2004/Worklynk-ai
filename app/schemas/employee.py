from pydantic import BaseModel, EmailStr


class EmployeeCreate(BaseModel):
    employee_id: str
    name: str
    email: EmailStr
    department: str
    role: str


class EmployeeResponse(EmployeeCreate):
    id: int