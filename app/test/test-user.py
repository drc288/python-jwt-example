from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_user():
    response = client.post(
        "/api/auth/signup",
        json={
            "name": "testuser",
            "email": "user@email.com",
            "password": "password"
        },
    )
    res = response.json()
    assert response.status_code == 200
    assert res == {"access_token": res.get("access_token")}

