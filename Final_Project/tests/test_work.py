import pytest
from rest_framework import status

valid_data = {
            'name': 'Frezowanie',
            'machine_usage': 70
        }
unvalid_data = {
            'name': True,
            'machine_usage': "babcia"
        }


@pytest.mark.django_db
def test_auth_admin_work_list(client, admin_logged):
    response = client.get('/zmz/work/')
    response1 = client.post('/zmz/work/', valid_data)
    response2 = client.post('/zmz/work/', unvalid_data)
    response3 = client.post('/zmz/work/', valid_data)
    assert response.status_code == 200
    assert response1.status_code == 201
    assert response2.status_code == 400
    assert response3.status_code == 400


@pytest.mark.django_db
def test_auth_user_work_list(client, user_logged):
    response = client.get('/zmz/work/')
    assert response.status_code == 403


@pytest.mark.django_db
def test_random_client_work_list(client):
    response = client.get('/zmz/work/')
    assert response.status_code == 403


@pytest.mark.django_db
def test_admin_work_CRUD(client, admin_logged, db_create):
    response = client.get('/zmz/work/Frezowanie')
    response1 = client.get('/zmz/work/dgihu')
    assert response.status_code == 200
    assert response1.status_code == 400

    response2 = client.put('/zmz/work/Frezowanie', {'name': 'Frezowanie', 'machine_usage': 75})
    assert response2.status_code == 200
    response3 = client.get('/zmz/work/Frezowanie')
    assert response3.data['machine_usage'] == 75

    response4 = client.delete('/zmz/work/Frezowanie')
    assert response4.status_code == 200
    response5 = client.get('/zmz/work/Frezowanie')
    assert response5.status_code == 400

