import pytest
from unittest.mock import patch, MagicMock
from fastapi.testclient import TestClient
from app.gateway import app
from jose import jwt
import os
from app.db.models import Notification, WorldEvent, UserCampaignRole, Campaign, World

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
def fake_db():
    mock_db = MagicMock()

    # Fake objects
    fake_campaign = MagicMock(id=1, name="Mock Campaign", world_id=1)
    fake_world = MagicMock(id=1, name="Mock World", created_by="user123")
    fake_notification = MagicMock(id=1, title="Notification")
    fake_world_event = MagicMock(id=1, title="World Event")

    def query_side_effect(model):
        if model == UserCampaignRole:
            query_mock = MagicMock()
            # Here we simulate different behavior based on user_id
            def filter_by_side_effect(**kwargs):
                user_id = kwargs.get('user_id')
                if user_id.startswith("RANDOM"):
                    # Simulate "user not found"
                    filtered_query_mock = MagicMock()
                    filtered_query_mock.all.return_value = []
                    return filtered_query_mock
                else:
                    # Normal case: user exists
                    filtered_query_mock = MagicMock()
                    filtered_query_mock.all.return_value = [MagicMock(campaign_id=1, world_id=1)]
                    return filtered_query_mock

            query_mock.filter_by.side_effect = filter_by_side_effect
            return query_mock
        elif model == Campaign:
            query_mock = MagicMock()
            query_mock.filter.return_value.all.return_value = [fake_campaign]
            return query_mock
        elif model == World:
            query_mock = MagicMock()
            query_mock.filter.return_value.all.return_value = [fake_world]
            return query_mock
        elif model == Notification:
            query_mock = MagicMock()
            query_mock.filter.return_value.limit.return_value.offset.return_value = [fake_notification]
            return query_mock
        elif model == WorldEvent:
            query_mock = MagicMock()
            query_mock.filter.return_value.limit.return_value.offset.return_value = [fake_world_event]
            return query_mock
        else:
            return MagicMock()

    mock_db.query.side_effect = query_side_effect

    return mock_db

@pytest.fixture
def auth_client(client, fake_token, fake_db):
    client.headers.update({"Authorization": f"Bearer {fake_token}"})
    from app.db.supabaseDB import get_db
    app.dependency_overrides[get_db] = lambda: fake_db

    yield client    # Test runs here

    app.dependency_overrides.clear  # Reset state of fake_db



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
    response = client.get(f"/api/users/{fake_user_id}")
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
    assert "world_notifications" or "campaign_notifications" in response.json()


def test_get_notifications_failure(client):
    response = client.get("/api/users/notifications")
    print(response.json())
    assert response.status_code == 401
    assert "detail" in response.json()


def test_get_world_events(auth_client):
    response = auth_client.get("/api/users/events")
    print(response.json())
    assert response.status_code == 200
    # assert "campaign_events" in response.json()


def test_get_world_events_failure(client):
    response = client.get("/api/users/events")
    print(response.json())
    assert response.status_code == 401
    assert "detail" in response.json()
