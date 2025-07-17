from app import app

def test_home():
    tester = app.test_client()
    response = tester.get('/')
    assert response.status_code == 200
    assert b"Welcome to the Healthy Snacking API" in response.data

def test_about():
    tester = app.test_client()
    response = tester.get('/about')
    assert response.status_code == 200
    assert b"developer" in response.data

def test_suggest_snack():
    tester = app.test_client()
    response = tester.get('/suggest?mood=happy')
    assert response.status_code == 200
    json_data = response.get_json()
    assert "suggestions" in json_data
