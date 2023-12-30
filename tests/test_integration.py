import pytest
from app import app, db

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    client = app.test_client()

    with app.app_context():
        db.create_all()

    yield client

    with app.app_context():
        db.drop_all()

def test_index_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to the DevOps Interactive Dashboard" in response.data


