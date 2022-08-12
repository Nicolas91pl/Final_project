import pytest
from rest_framework import status

valid_data = {
            'name': 'Obecne', 'actual': True, 'energy': 8000,
            'salary': 40000, 'others': 7000
        }
unvalid_data = {
            'name': 63528, 'actual': 'może', 'energy': True,
            'salary': 40000, 'others': 7000
        }

@pytest.mark.django_db
def test_auth_admin_expanses_list(client, admin_logged):
    response = client.get('/zmz/expanses/')
    response1 = client.post('/zmz/expanses/', valid_data)
    response2 = client.post('/zmz/expanses/', unvalid_data)
    response3 = client.post('/zmz/expanses/', valid_data)
    assert response.status_code == 200
    assert response1.status_code == 201
    assert response2.status_code == 400
    assert response3.status_code == 400


@pytest.mark.django_db
def test_auth_user_expanses_list(client, user_logged):
    response = client.get('/zmz/expanses/')
    assert response.status_code == 403


@pytest.mark.django_db
def test_random_client_expanses_list(client):
    response = client.get('/zmz/expanses/')
    assert response.status_code == 403


@pytest.mark.django_db
def test_admin_expanses_CRUD(client, admin_logged, created_db):
    response = client.get('/zmz/expanses/Obecne')
    response1 = client.get('/zmz/expanses/dgihu')
    assert response.status_code == 200
    assert response1.status_code == 400

    response2 = client.put('/zmz/expanses/Obecne', valid_data)
    assert response2.status_code == 200
    response3 = client.get('/zmz/expanses/Obecne')
    assert response3.data['energy'] == 8000

    response4 = client.delete('/zmz/expanses/Obecne')
    assert response4.status_code == 200
    response5 = client.get('/zmz/expanses/Obecne')
    assert response5.status_code == 400

