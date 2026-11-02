
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_prediction():
    response = client.post(
        "/predict",
        json={"study_hours": 5}
    )

    assert response.status_code == 200

    data = response.json()
    assert data["study_hours"] == 5
    assert "predicted_score" in data
    assert 0 <= data["predicted_score"] <= 100


def test_invalid_study_hours():
    response = client.post(
        "/predict",
        json={"study_hours": 11}
    )

    assert response.status_code == 422
