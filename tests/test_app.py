import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home_page(client):
    """Test the home page for correct HTTP response."""
    response = client.get('/')
    assert response.status_code == 200

def test_submit_page(client):
    """Test the submit route for correct HTTP response."""
    response = client.post('/submit', data={'userData': 'test', 'devOpsFeature': 'CI/CD'})
    assert response.status_code == 200
    assert b"Your data has been successfully recorded!" in response.data
