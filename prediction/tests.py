import pytest
from django.urls import reverse
from http import HTTPStatus


@pytest.fixture
def data():
    return {
        'sold_plu_4046' : 5,
        'sold_plu_4225' : 6,
        'sold_plu_4770': 8,
        'small_bags': 4,
        'large_bags': 0,
        'xlarge_bags': 0,
        'organic': 'on',
        'region': 'Albany'
    }

def test_method_not_allowed(client):
    response = client.get(reverse('predict'))
    assert response.status_code == HTTPStatus.METHOD_NOT_ALLOWED
    
def test_empty(client):
    response = client.post(reverse('predict'))
    assert response.status_code == HTTPStatus.BAD_REQUEST

def test_invalid_data(client, data):
    data['sold_plu_4046'] = 'not number'

    response = client.post(reverse('predict'), data)
    assert response.status_code == HTTPStatus.BAD_REQUEST

def test_missing_field(client, data):
    del data['sold_plu_4046']

    response = client.post(reverse('predict'), data)
    assert response.status_code == HTTPStatus.BAD_REQUEST

def test_valid(client, data):
    response = client.post(reverse('predict'), data)
    assert response.status_code == HTTPStatus.OK
    assert "1019" in response.content.decode('utf-8')