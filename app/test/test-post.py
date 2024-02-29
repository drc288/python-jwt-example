from fastapi.testclient import TestClient
from app.api.endpoints.posts import posts
from main import app

client = TestClient(app)

def test_read_all_posts_unauthorized():
    response = client.get("/api/posts/")
    assert response.status_code == 403
    assert response.json() == {"detail": "Not authenticated"}

def test_read_all_posts():
    response_secure = client.post(
        "/api/auth/signup",
        json={
            "name": "testuser",
            "email": "user@email.com",
            "password": "password"
        },
    )
    response = client.get("/api/posts/", headers={"Authorization": f"Bearer {response_secure.json().get('access_token')}"})
    assert response.status_code == 200
    assert response.json() == {"data": posts}
