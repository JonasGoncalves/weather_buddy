import json


def test_no_cached_cities(client):
    response = client.get('/weather')
    assert response.status_code == 404
    response_data = json.loads(response.data)
    assert response_data['data'] is None


def test_city(client):
    response = client.get('/weather/houston')
    assert response.status_code == 200
    response_data = json.loads(response.data)
    assert response_data['data'] is not None


def test_city_2(client):
    response = client.get('/weather/new york')
    assert response.status_code == 200
    response_data = json.loads(response.data)
    assert response_data['data'] is not None


def test_existing_cached_cities(client):
    response = client.get('/weather')
    assert response.status_code == 200
    response_data = json.loads(response.data)
    assert response_data['data'] is not None


def test_no_existing_city(client):
    response = client.get('/weather/00000')
    assert response.status_code == 404
    response_data = json.loads(response.data)
    assert response_data['data'] is None
