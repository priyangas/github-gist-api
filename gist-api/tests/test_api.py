from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_get_gists_octocat():
    response = client.get("/users/octocat/gists")

    # Check API success
    assert response.status_code == 200

    # Check response is a list
    data = response.json()
    assert isinstance(data, list)

    # Optional: validate structure
    if len(data) > 0:
        assert "id" in data[0]
        assert "url" in data[0]
        assert "files" in data[0]