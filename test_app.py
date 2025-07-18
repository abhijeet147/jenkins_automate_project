import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_homepage(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"<form" in response.data  # Basic check for form presence

def test_post_missing_fields(client):
    response = client.post('/', data={})
    assert response.status_code == 400
    assert b"Please provide both mood and time" in response.data

def test_post_valid_input(client):
    response = client.post('/', data={'mood': 'happy', 'time': 'morning'})
    assert response.status_code == 200
    assert b"Suggest Snacks" in response.data or b"snack" in response.data

def test_about_route(client):
    response = client.get('/about')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['project'] == "Have Healthy Snacks API"
    assert json_data['developer'] == "Abhijeet Kamthe"
