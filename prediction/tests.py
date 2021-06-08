import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_method_not_allowed(client):
    response = client.get(reverse('predict'))
    assert response.status_code == 405 
    
@pytest.mark.django_db
def test_empty(client):
    response = client.post(reverse('predict'))
    assert response.status_code == 400

@pytest.mark.django_db
def test_invalid_data(client):
    data = {
        'sold_plu_4046' : 'not number',
        'sold_plu_4225' : 6,
        'sold_plu_4770': 8,
        'small_bags': 4,
        'large_bags': 0,
        'xlarge_bags': 0,
        'organic': 'on',
        'region': 'Albany'
    }
    response = client.post(reverse('predict'), data)
    assert response.status_code == 400

@pytest.mark.django_db
def test_missing_field(client):
    data = {
        'sold_plu_4225' : 6,
        'sold_plu_4770': 8,
        'small_bags': 4,
        'large_bags': 0,
        'xlarge_bags': 0,
        'organic': 'on',
        'region': 'Albany'
    }
    response = client.post(reverse('predict'), data)
    assert response.status_code == 400

@pytest.mark.django_db
def test_valid(client):
    data = {
        'sold_plu_4046' : 5,
        'sold_plu_4225' : 6,
        'sold_plu_4770': 8,
        'small_bags': 4,
        'large_bags': 0,
        'xlarge_bags': 0,
        'organic': 'on',
        'region': 'Albany'
    }
    response = client.post(reverse('predict'), data)
    assert response.status_code == 200
    assert "1019" in response.content.decode('utf-8')