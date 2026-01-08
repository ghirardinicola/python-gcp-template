"""Tests for main application."""

from fastapi.testclient import TestClient

from my_app.main import app

client = TestClient(app)


def test_health():
    """Test health endpoint returns healthy status."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_root():
    """Test root endpoint returns hello message."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}
