import pytest
from rest_framework import status

valid_data = {'customer': 1, 'active': True, 'ready': False,
                                 'concession': False, 'serial_number': '005-abc', 'name': 'Dymiący',
                                 'producer': 'Vinetu', 'production_year': 1910, 'description': 'Kolimator',
                                 'work_types': [1, 2]}

unvalid_data = {'customer': 1, 'active': 'moze', 'ready': False,
                                 'concession': False, 'serial_number': '007ZS', 'name': 'Grzmiący kij',
                                 'producer': 'Vinetu', 'production_year': 1890, 'description': 'Luneta 400x',
                                 'work_types': ['babala']}


@pytest.mark.django_db
def test_auth_admin_orders_list(client, admin_logged, created_db):
    response = client.get('/zmz/orders/')
    response1 = client.post('/zmz/orders/', valid_data)
    response2 = client.post('/zmz/orders/', unvalid_data)
    response3 = client.post('/zmz/orders/', valid_data)
    assert response.status_code == 200
    assert response1.status_code == 201
    assert response2.status_code == 400
    assert response3.status_code == 400


@pytest.mark.django_db
def test_auth_user_orders_list(client, user_logged, created_db):
    response = client.get('/zmz/orders/')
    response1 = client.post('/zmz/orders/', valid_data)
    response2 = client.post('/zmz/orders/', unvalid_data)
    response3 = client.post('/zmz/orders/', valid_data)
    assert response.status_code == 200
    assert response1.status_code == 201
    assert response2.status_code == 400
    assert response3.status_code == 400


@pytest.mark.django_db
def test_random_client_orders_list(client, created_db):
    response = client.get('/zmz/orders/')
    assert response.status_code == 403


@pytest.mark.django_db
def test_admin_orders_CRUD(client, admin_logged, created_db):
    response = client.get('/zmz/orders/1')
    response1 = client.get('/zmz/orders/dgihu')
    assert response.status_code == 200
    assert response1.status_code == 400

    response2 = client.put('/zmz/orders/1', valid_data)
    assert response2.status_code == 200
    response3 = client.get('/zmz/orders/1')
    assert response3.data['realise_date'] == '2005-10-08'

    response4 = client.delete('/zmz/orders/1')
    assert response4.status_code == 200
    response5 = client.get('/zmz/orders/1')
    assert response5.status_code == 400

@pytest.mark.django_db
def test_user_orders_CRUD(client, user_logged, created_db):
    response = client.get('/zmz/orders/1')
    response1 = client.get('/zmz/orders/dgihu')
    assert response.status_code == 200
    assert response1.status_code == 400

    response2 = client.put('/zmz/orders/1', valid_data)
    assert response2.status_code == 200
    response3 = client.get('/zmz/orders/1')
    assert response3.data['realise_date'] == '2005-10-08'

    response4 = client.delete('/zmz/orders/1')
    assert response4.status_code == 200
    response5 = client.get('/zmz/orders/1')
    assert response5.status_code == 400

