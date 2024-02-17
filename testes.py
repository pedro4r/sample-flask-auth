import pytest
import requests

# CRUD
BASE_URL = 'http://127.0.0.1:5000'
tasks = []

def test_create_user():
    newUser = {
        "username": "newUserName",
        "password": "newpassword"
    }
    response = requests.post(f"{BASE_URL}/user", json=newUser)
    assert response.status_code == 200
    response_json = response.json()
    assert "message" in response_json
    assert "id" in response_json