from app.models.employee import Employee


class EmployeeService:

    def __init__(self):
        self.employees: list[Employee] = []

    def create_employee(self, employee: Employee) -> Employee:
        self.employees.append(employee)
        return employee

    def get_all_employees(self) -> list[Employee]:
        return self.employees

    def get_employee_by_id(self, employee_id: int) -> Employee | None:
        for employee in self.employees:
            if employee.id == employee_id:
                return employee

        return None