import pytest
from unittest.mock import patch, MagicMock
from fastapi.testclient import TestClient
from app.gateway import app
from random import randint
import os
from jose import jwt

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
def auth_client(client, fake_token, fake_db):
    client.headers.update({"Authorization": f"Bearer {fake_token}"})
    from app.db.supabaseDB import get_db
    app.dependency_overrides[get_db] = lambda: fake_db

    yield client    # Test runs here

    app.dependency_overrides.clear  # Reset state of fake_db

# ==================================================

@pytest.fixture
def test_world_success():
   return {
       "name": "Ernesto's Grand Adventure",
       "description": "Ernesto finds out what, touching grass, means",
   }

@pytest.fixture
def test_world_fail():
   return {
       "name": "Ernesto's Grand Adventure but the title is way to long for this to be an actual valid input because the limit is 100 characters and this is already way over that limit",
       "description": "Ernesto finds out what, touching grass, means",
   }

# def test_create_world(auth_client, test_world_success):
#    response = auth_client.post("/api/worlds/create_world", json=test_world_success)
#    print(response.json())
#    print(response.status_code)
#    assert response.status_code == 200

# # Test for a name over 100 characters
# def test_long_world_name(auth_client, test_world_fail):
#    response = auth_client.post("/api/worlds/create_world", json=test_world_fail)
#    print(response.json())
#    print(response.status_code)
#    assert response.status_code == 400
   
