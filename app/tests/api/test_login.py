from typing import Dict

from fastapi.testclient import TestClient


def test_get_access_token(client: TestClient) -> None:
    login_data = {
        "username": "luis@gmail.com",
        "password": "123",
    }
    r = client.post("/login", data=login_data)
    tokens = r.json()
    assert r.status_code == 200
    assert "access_token" in tokens
    assert tokens["access_token"]