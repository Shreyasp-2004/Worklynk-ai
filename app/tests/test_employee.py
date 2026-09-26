from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_create_employee():
    response = client.post(
        "/api/v1/employees/",
        json={
            "employee_id": "EMP001",
            "name": "Rahul Sharma",
            "email": "rahul@company.com",
            "department": "Engineering",
            "role": "Software Engineer"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["employee_id"] == "EMP001"
    assert data["name"] == "Rahul Sharma"
    assert data["email"] == "rahul@company.com"


def test_get_all_employees():
    response = client.get("/api/v1/employees/")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_employee_not_found():
    response = client.get("/api/v1/employees/999")

    assert response.status_code == 404