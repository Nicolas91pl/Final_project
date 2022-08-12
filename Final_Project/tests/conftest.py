import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from zaklad import models

@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def user():
    user = User.objects.create_user(username='DiegoM', password='LegendaryG0l')
    return user

@pytest.fixture
def admin_user():
    admin_user = User.objects.create_superuser(username='Elvis', password='Live4ever')
    return admin_user

@pytest.fixture
def admin_logged(client, admin_user):
    client.post('/api-auth/login/', dict(username='Elvis', password='Live4ever'))
    return client

@pytest.fixture
def user_logged(client, user):
    client.post('/api-auth/login/', dict(username='DiegoM', password='LegendaryG0l'))
    return client

@pytest.fixture
def created_db(client):
    client.post('/zmz/work/', {'name': 'Frezowanie', 'machine_usage': 70})
    client.post('/zmz/work/', {'name': 'Czyszczenie', 'machine_usage': 30})
    client.post('/zmz/expanses/', {'name': 'Obecne', 'actual': True, 'energy': 3000, 'salary': 40000, 'others': 10000})
    client.post('/zmz/customers/', {'individual': True, 'name': "Kevin", 'surname': 'Sam',
                                    'telephone': 123456789, 'e_address': '', 'address': ''})
    client.post('/zmz/licences/', {'type': 'Sportowa', 'serial_number': 'AAL-009675',
                                   'realise_date': '1995-05-08', 'authority': 'KSP Warszawa',
                                   'owner': 1})
    client.post('/zmz/orders/', {'customer': 1, 'active': True, 'ready': False,
                                 'concession': False, 'serial_number': '007ZS', 'name': 'Grzmiący kij',
                                 'producer': 'Vinetu', 'production_year': 1890, 'description': 'Luneta 400x',
                                 'work_types': [1, 2]})

    return client
