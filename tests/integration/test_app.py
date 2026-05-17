import pytest

from app import create_app
from duty import DutyRepository

@pytest.fixture
def repo(tmp_path):
    return DutyRepository(filepath=tmp_path / "duties.json")

@pytest.fixture
def client(repo):
    
    app = create_app(repo)
    return app.test_client()

def test_GET_duties_returns_200(client):
    response = client.get("/duties")
    assert response.status_code == 200

def test_GET_duties_shows_existing_duty(client, repo):
    repo.add("D1", "Desc 1")
    response = client.get("/duties")
    assert b"D1" in response.data

def test_GET_duties_shows_multiple_existing_duties(client, repo):
    repo.add("D2", "Desc 2")
    repo.add("D3", "Desc 3")

    response = client.get("/duties")
    assert "D2" in response.text
    assert "D3" in response.text
