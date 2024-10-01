import pytest 
from webapp.app import app

@pytest.fixture()
def client():
    return app.test_client()

def test_home_subtraction(client):
    response = client.get('/?a=50&b=45')
    assert response.status_code == 200
    assert b'The difference is 5' in response.data

def test_multiplication(client):
    response = client.get('/multiply?a=3&b=11')
    assert response.status_code == 200
    assert b'The product is 33' in response.data

def test_division(client):
    response = client.get('/divide?a=60&b=3')
    assert response.status_code == 200
    assert b'The quotient is 20' in response.data

