import pytest
from fastapi.testclient import TestClient
from app.gateway import app
from random import randint

client = TestClient(app)

@pytest.fixture
def login_data_success():
    return {
        "email": "test@test.com",
        "password": "test",
    }

@pytest.fixture
def login_data_fail():
    return {
        "email": "BADtest@test.com",
        "password": "test",
    }

def generate_random_email():
    random_uid = str(randint(1, 99999))
    rest = "@gmail.com"
    email = "test" + random_uid + rest
    return email

@pytest.fixture
def register_data_success():
    return {
        "email": generate_random_email(),
        "password": "test-test"
    }

@pytest.fixture
def register_data_fail():
    return {
        "email": generate_random_email(),
        "password": "not>6"
    }

def test_login_correct(login_data_success):
    response = client.post("/api/auth/login", json=login_data_success)
    assert response.status_code == 200
    assert "user" in response.json()

def test_login_fail(login_data_fail):
    response = client.post("/api/auth/login", json=login_data_fail)
    assert response.status_code == 500
    assert "detail" in response.json()

def test_register_success(register_data_success):
    response = client.post("/api/auth/register", json=register_data_success)
    assert response.status_code == 200

def test_register_fail(register_data_success):
    response = client.post("/api/auth/register", json=register_data_fail)
    assert response.status_code == 400
    assert "detail" in response.json()
