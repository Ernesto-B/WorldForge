#import pytest
#from unittest.mock import patch, MagicMock
#from fastapi.testclient import TestClient
#from app.gateway import app
#from random import randint
#
#client = TestClient(app)
#
#@pytest.fixture
#def test_world_success():
#    return {
#        "id": "test123",
#        "name": "Ernesto's Grand Adventure",
#        "description": "Ernesto finds out what, touching grass, means",
#        "created_at": "2025-04-20"
#    }
#
#@pytest.fixture
#def test_world_success():
#    return {
#        "id": "test123",
#        "name": "Ernesto's Grand Adventure",
#        "description": "Ernesto finds out what, touching grass, means",
#        "created_at": "2025-04-20"
#    }
#
#def test_create_world(test_world_success):
#    response = client.post("/api/worlds/create_world", json=test_world_success)
#    print(response.json())
#    print(response.status_code)
#    assert response.status_code == 200
#    
