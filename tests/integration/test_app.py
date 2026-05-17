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

def test_GET_new_duty_form_renders_form(client):
    response = client.get("/duties/new")
    assert response.status_code == 200
    assert b'<form' in response.data
    assert b'action="/duties"' in response.data
    assert b'method="post"' in response.data
    assert b'name="name"' in response.data
    assert b'name="description"' in response.data

def test_POST_duties_creates_duty(client, repo):
    response = client.post(
        "/duties",
        data={"name": "D3", "description": "Desc 3"},
    )
    assert response.status_code == 302
    assert any(d.name == "D3" for d in repo.all())

def test_POST_duties_duplicate_name_does_not_create(client, repo):
    repo.add("D1", "Original description")

    response = client.post(
        "/duties",
        data={"name": "D1", "description": "Different description"},
    )

    assert response.status_code == 302
    duties = [d for d in repo.all() if d.name == "D1"]
    assert len(duties) == 1


