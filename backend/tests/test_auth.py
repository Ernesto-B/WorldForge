import pytest
from unittest.mock import patch, MagicMock
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


def test_login_success(login_data_success):
    # Expecting this to pass since the provided user/password exists
    response = client.post("/api/auth/login", json=login_data_success)
    print(response.json())
    print(response.status_code)
    assert response.status_code == 200
    assert "user" in response.json()

def test_login_fail(login_data_fail):
    # Expecting this to fail since the user provided does not exist
    response = client.post("/api/auth/login", json=login_data_fail)
    print(response.json())
    print(response.status_code)
    assert response.status_code == 500
    assert "detail" in response.json()

@patch("app.services.register.create_client")
def test_register_success(mock_create_client, register_data_success):
    # Expecting this to pass since email is valid and len(password)>6
    mock_supabase = MagicMock()
    mock_supabase.auth.sign_up.return_value = MagicMock(
        user={"id": "123", "email": "mock@test.com"},
        session={"access_token": "fake_token"},
        error=None
    )
    mock_create_client.return_value = mock_supabase

    response = client.post("/api/auth/register", json=register_data_success)
    print(response.json())
    print(response.status_code)
    assert response.status_code == 200

def test_register_fail(register_data_fail):
    # Expecting this to fail since len(password)<6
    response = client.post("/api/auth/register", json=register_data_fail)
    print(response.json())
    print(response.status_code)
    assert response.status_code == 400
    assert "detail" in response.json()
