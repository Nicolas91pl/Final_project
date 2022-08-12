import pytest
from zaklad import models

valid_data = {'type': 'Kolekcjonerska', 'serial_number': 'Ab-12546',
              'realise_date': '2005-10-08', 'authority': 'KSP Warszawa',
              'owner': 1}

unvalid_data = {'type': 158, 'serial_number': '', 'realise_date': '1995-05-08',
                'authority': 'KSP Warszawa', 'owner': 1}


@pytest.mark.django_db
def test_auth_admin_licences_list(client, admin_logged, created_db):
    response = client.get('/zmz/licences/')
    response1 = client.post('/zmz/licences/', valid_data)
    response2 = client.post('/zmz/licences/', unvalid_data)
    assert response.status_code == 200
    assert response1.status_code == 201
    assert response2.status_code == 400


@pytest.mark.django_db
def test_auth_user_licences_list(client, user_logged, created_db):
    response = client.get('/zmz/licences/')
    response1 = client.post('/zmz/licences/', valid_data)
    response2 = client.post('/zmz/licences/', unvalid_data)
    assert response.status_code == 200
    assert response1.status_code == 201
    assert response2.status_code == 400


# @pytest.mark.django_db
# def test_random_client_licences_list(client):
#     response = client.get('/zmz/licences/')
#     assert response.status_code == 403
#
#
# @pytest.mark.django_db
# def test_admin_licences_CRUD(client, admin_logged, created_db):
#     inst = models.Licences.objects.all().first()
#     inst.refresh_from_db()
#     response = client.get(f'/zmz/licences/{inst.id}')
#     response1 = client.get('/zmz/licences/0')
#     assert response.status_code == 200
#     assert response1.status_code == 400
#
#     response2 = client.put(f'/zmz/licences/{inst.id}', valid_data)
#     assert response2.status_code == 200
#     response3 = client.get(f'/zmz/licences/{inst.id}')
#     assert response3.data['type'] == 'Osobista'
#
#     response4 = client.delete(f'/zmz/licences/{inst.id}')
#     assert response4.status_code == 200
#     response5 = client.get(f'/zmz/licences/{inst.id}')
#     assert response5.status_code == 400
#
#
# @pytest.mark.django_db
# def test_user_licences_CRUD(client, user_logged, created_db):
#     inst = models.Licences.objects.all().first()
#     inst.refresh_from_db()
#     response = client.get(f'/zmz/licences/{inst.id}')
#     response1 = client.get('/zmz/licences/0')
#     assert response.status_code == 200
#     assert response1.status_code == 400
#
#     response2 = client.put(f'/zmz/licences/{inst.id}', valid_data)
#     assert response2.status_code == 200
#     response3 = client.get(f'/zmz/licences/{inst.id}')
#     assert response3.data['type'] == 'Osobista'
#
#     response4 = client.delete(f'/zmz/licences/{inst.id}')
#     assert response4.status_code == 200
#     response5 = client.get(f'/zmz/licences/{inst.id}')
#     assert response5.status_code == 400
