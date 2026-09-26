from fastapi import APIRouter, HTTPException

from app.models.employee import Employee
from app.schemas.employee import EmployeeCreate, EmployeeResponse
from app.services.employee_service import EmployeeService


router = APIRouter(
    prefix="/api/v1/employees",
    tags=["Employees"]
)

employee_service = EmployeeService()


@router.post("/", response_model=EmployeeResponse)
def create_employee(employee_data: EmployeeCreate):
    employee = Employee(
        id=len(employee_service.get_all_employees()) + 1,
        **employee_data.model_dump()
    )

    return employee_service.create_employee(employee)


@router.get("/", response_model=list[EmployeeResponse])
def get_all_employees():
    return employee_service.get_all_employees()


@router.get("/{employee_id}", response_model=EmployeeResponse)
def get_employee(employee_id: int):
    employee = employee_service.get_employee_by_id(employee_id)

    if employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return employee