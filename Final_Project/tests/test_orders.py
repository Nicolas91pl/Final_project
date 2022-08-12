# import pytest
# from zaklad import models
#
#
# unvalid_data = {'customer': 1, 'active': 'moze', 'ready': False,
#                                  'concession': False, 'serial_number': '007ZS', 'name': 'Grzmiący kij',
#                                  'producer': 'Vinetu', 'production_year': 1890, 'description': 'Luneta 400x',
#                                  'work_types': ['babala']}
#
#
# @pytest.mark.django_db
# def test_auth_admin_orders_list(client, admin_logged, db_create):
#     owner = models.Customers.objects.all().first()
#     owner_id = owner.id
#     wt1 = models.Work_Type.objects.all().first()
#     wt1_id = wt1.id
#     wt2 = models.Work_Type.objects.all().last()
#     wt2_id = wt2.id
#     response = client.get('/zmz/orders/')
#     response1 = client.post('/zmz/orders/', {'customer': owner_id, 'active': True, 'ready': False,
#                                  'concession': False, 'serial_number': '005-abc', 'name': 'Dymiący',
#                                  'producer': 'Vinetu', 'production_year': 1910, 'description': 'Kolimator',
#                                  'work_types': [wt1_id, wt2_id]})
#     response2 = client.post('/zmz/orders/', unvalid_data)
#     response3 = client.post('/zmz/orders/', {'customer': owner_id, 'active': True, 'ready': False,
#                                  'concession': False, 'serial_number': '005-abc', 'name': 'Dymiący',
#                                  'producer': 'Vinetu', 'production_year': 1910, 'description': 'Kolimator',
#                                  'work_types': [wt1_id, wt2_id]})
#     assert response.status_code == 200
#     assert response1.status_code == 201
#     assert response2.status_code == 400
#     assert response3.status_code == 400
#
#
# @pytest.mark.django_db
# def test_auth_user_orders_list(client, user_logged, db_create):
#     owner = models.Customers.objects.all().first()
#     owner_id = owner.id
#     wt1 = models.Work_Type.objects.all().first()
#     wt1_id = wt1.id
#     wt2 = models.Work_Type.objects.all().last()
#     wt2_id = wt2.id
#     response = client.get('/zmz/orders/')
#     response1 = client.post('/zmz/orders/', {'customer': owner_id, 'active': True, 'ready': False,
#                                  'concession': False, 'serial_number': '005-abc', 'name': 'Dymiący',
#                                  'producer': 'Vinetu', 'production_year': 1910, 'description': 'Kolimator',
#                                  'work_types': [wt1_id, wt2_id]})
#     response2 = client.post('/zmz/orders/', unvalid_data)
#     response3 = client.post('/zmz/orders/', {'customer': owner_id, 'active': True, 'ready': False,
#                                  'concession': False, 'serial_number': '005-abc', 'name': 'Dymiący',
#                                  'producer': 'Vinetu', 'production_year': 1910, 'description': 'Kolimator',
#                                  'work_types': [wt1_id, wt2_id]})
#     assert response.status_code == 200
#     assert response1.status_code == 201
#     assert response2.status_code == 400
#     assert response3.status_code == 400
#
#
# @pytest.mark.django_db
# def test_random_client_orders_list(client, db_create):
#     response = client.get('/zmz/orders/')
#     assert response.status_code == 403
#
#
# @pytest.mark.django_db
# def test_admin_orders_CRUD(client, admin_logged, db_create,):
#     owner = models.Customers.objects.all().first()
#     owner_id = owner.id
#     wt1 = models.Work_Type.objects.all().first()
#     wt1_id = wt1.id
#     wt2 = models.Work_Type.objects.all().last()
#     wt2_id = wt2.id
#     models.Orders.objects.create(customer=owner_id, active=True, ready=False,
#                                  concession=False, serial_number='007ZS', name='Grzmiący kij',
#                                  producer='Vinetu', production_year=1890, description='Luneta 400x',
#                                  work_types=[wt1_id, wt2_id])
#     order = models.Orders.objects.all().first()
#     order_id = order.id
#     response = client.get(f'/zmz/orders/{order_id}')
#     response1 = client.get('/zmz/orders/dgihu')
#     assert response.status_code == 200
#     assert response1.status_code == 400
#
#     response2 = client.put('/zmz/orders/1', {'customer': owner_id, 'active': True, 'ready': False,
#                                  'concession': False, 'serial_number': '005-abc', 'name': 'Dymiący',
#                                  'producer': 'Vinetu', 'production_year': 1910, 'description': 'Kolimator',
#                                  'work_types': [wt1_id, wt2_id]})
#     assert response2.status_code == 200
#     response3 = client.get(f'/zmz/orders/{order_id}')
#     assert response3.data['production_year'] == 1910
#
#     response4 = client.delete(f'/zmz/orders/{order_id}')
#     assert response4.status_code == 200
#     response5 = client.get(f'/zmz/orders/{order_id}')
#     assert response5.status_code == 400
#
# @pytest.mark.django_db
# def test_user_orders_CRUD(client, user_logged, db_create):
#     owner = models.Customers.objects.all().first()
#     owner_id = owner.id
#     wt1 = models.Work_Type.objects.all().first()
#     wt1_id = wt1.id
#     wt2 = models.Work_Type.objects.all().last()
#     wt2_id = wt2.id
#     models.Orders.objects.create(customer=owner_id, active=True, ready=False,
#                                  concession=False, serial_number='007ZS', name='Grzmiący kij',
#                                  producer='Vinetu', production_year=1890, description='Luneta 400x',
#                                  work_types=[wt1_id, wt2_id])
#     order = models.Orders.objects.all().first()
#     order_id = order.id
#     response = client.get(f'/zmz/orders/{order_id}')
#     response1 = client.get('/zmz/orders/dgihu')
#     assert response.status_code == 200
#     assert response1.status_code == 400
#
#     response2 = client.put(f'/zmz/orders/{order_id}', {'customer': owner_id, 'active': True, 'ready': False,
#                                  'concession': False, 'serial_number': '005-abc', 'name': 'Dymiący',
#                                  'producer': 'Vinetu', 'production_year': 1910, 'description': 'Kolimator',
#                                  'work_types': [wt1_id, wt2_id]})
#     assert response2.status_code == 200
#     response3 = client.get(f'/zmz/orders/{order_id}')
#     assert response3.data['production_year'] == 1910
#
#     response4 = client.delete(f'/zmz/orders/{order_id}')
#     assert response4.status_code == 200
#     response5 = client.get(f'/zmz/orders/{order_id}')
#     assert response5.status_code == 400
#
