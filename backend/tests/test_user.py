import pytest
from unittest.mock import patch, MagicMock
from fastapi.testclient import TestClient
from app.gateway import app
from jose import jwt
import os

@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def fake_user_id():
    return "6bb63985-2218-4f1c-8049-4c3a976a7aa5"


@pytest.fixture
def fake_token(fake_user_id):
    secret = os.getenv("SUPABASE_JWT_SECRET", "test_secret_key")
    payload = {
        "sub": fake_user_id,
        "aud": "authenticated",
        "iss": f"{os.getenv('SUPABASE_URL', 'http://localhost')}/auth/v1",
    }
    token = jwt.encode(payload, secret, algorithm="HS256")
    return token


@pytest.fixture
def auth_client(client, fake_token):
    client.headers.update({"Authorization": f"Bearer {fake_token}"})
    return client


# ==============================================================================


def test_me_success(auth_client):
    response = auth_client.get("/api/users/me")
    print(response.json())
    assert response.status_code == 200
    assert "campaign_names" in response.json()
    assert "world_names" in response.json()


def test_me_unauthenticated(client):
    response = client.get("/api/users/me")
    print(response.json())
    assert response.status_code == 401
    assert "detail" in response.json()


def test_get_user_by_id(client):
    response = client.get(f"/api/users/6bb63985-2218-4f1c-8049-4c3a976a7aa5")
    print(response.json())
    assert response.status_code == 200
    assert "campaign_names" in response.json()
    assert "world_names" in response.json()


def test_user_by_id_failure(client):
    response = client.get(f"/api/users/RANDOM{fake_user_id}")
    print(response.json())
    assert response.status_code == 500
    assert "detail" in response.json()


def test_get_notifications_success(auth_client):
    response = auth_client.get("/api/users/notifications")
    print(response.json())
    assert response.status_code == 200
    # assert "world_notifications" in response.json()
    # assert "campaign_notifications" in response.json()


def test_get_notifications_failure(client):
    response = client.get("/api/users/notifications")
    print(response.json())
    assert response.status_code == 401
    assert "detail" in response.json()


def test_get_world_events(auth_client):
    response = auth_client.get("/api/users/events")
    print(response.json())
    assert response.status_code == 200
    # assert "world_events" in response.json()
    # assert "campaign_events" in response.json()


def test_get_world_events_failure(client):
    response = client.get("/api/users/events")
    print(response.json())
    assert response.status_code == 401
    assert "detail" in response.json()
