from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.employee import Employee
from app.schemas.employee import EmployeeCreate


class EmployeeService:

    @staticmethod
    def create_employee(db: Session, employee_data: EmployeeCreate) -> Employee:
        employee = Employee(
            employee_id=employee_data.employee_id,
            name=employee_data.name,
            email=employee_data.email,
            department=employee_data.department,
            role=employee_data.role
        )

        db.add(employee)
        db.commit()
        db.refresh(employee)

        return employee

    @staticmethod
    def get_all_employees(db: Session) -> list[Employee]:
        result = db.execute(select(Employee))
        return list(result.scalars().all())

    @staticmethod
    def get_employee_by_id(db: Session, employee_id: int) -> Employee | None:
        return db.get(Employee, employee_id)