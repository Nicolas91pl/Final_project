import pytest

from zaklad import models

valid_data = {
            'individual': True, 'name': 'Zenek', 'surname': 'Kielon',
            'telephone': 400000098, 'e_address': '', 'address': ''
        }
unvalid_data = {
            'individual': 1547, 'name': True, 'surname': 'Kielon',
            'telephone': 400000098, 'e_address': '', 'address':''
        }


@pytest.mark.django_db
def test_auth_admin_customers_list(client, admin_logged):
    response = client.get('/zmz/customers/')
    response1 = client.post('/zmz/customers/', valid_data)
    response2 = client.post('/zmz/customers/', unvalid_data)
    assert response.status_code == 200
    assert response1.status_code == 201
    assert response2.status_code == 400


@pytest.mark.django_db
def test_auth_user_customers_list(client, user_logged):
    response = client.get('/zmz/customers/')
    response1 = client.post('/zmz/customers/', valid_data)
    response2 = client.post('/zmz/customers/', unvalid_data)
    assert response.status_code == 200
    assert response1.status_code == 201
    assert response2.status_code == 400


@pytest.mark.django_db
def test_random_client_customers_list(client):
    response = client.get('/zmz/customers/')
    assert response.status_code == 403


@pytest.mark.django_db
def test_admin_customers_CRUD(client, admin_logged, created_db):
    inst = models.Customers.objects.all().first()
    inst.refresh_from_db()
    response = client.get(f'/zmz/customers/{inst.id}')
    response1 = client.get('/zmz/customers/0')
    assert response.status_code == 200
    assert response1.status_code == 400

    response2 = client.put(f'/zmz/customers/{inst.id}', valid_data)
    assert response2.status_code == 200
    response3 = client.get(f'/zmz/customers/{inst.id}')
    assert response3.data['name'] == 'Zenek'

    response4 = client.delete(f'/zmz/customers/{inst.id}')
    assert response4.status_code == 200
    response5 = client.get(f'/zmz/customers/{inst.id}')
    assert response5.status_code == 400


@pytest.mark.django_db
def test_user_customers_CRUD(client, user_logged, created_db):
    inst = models.Customers.objects.all().first()
    inst.refresh_from_db()
    response = client.get(f'/zmz/customers/{inst.id}')
    response1 = client.get('/zmz/customers/0')
    assert response.status_code == 200
    assert response1.status_code == 400

    response2 = client.put(f'/zmz/customers/{inst.id}', valid_data)
    assert response2.status_code == 200
    response3 = client.get(f'/zmz/customers/{inst.id}')
    assert response3.data['name'] == 'Zenek'

    response4 = client.delete(f'/zmz/customers/{inst.id}')
    assert response4.status_code == 200
    response5 = client.get(f'/zmz/customers/{inst.id}')
    assert response5.status_code == 400
