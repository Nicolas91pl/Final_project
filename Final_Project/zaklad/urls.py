from django.urls import path, include
from .views import (WorkTypeApiView, WorkTypeDetailApiView, ExpansesListApiView, ExpansesDetailApiView,
                    CustomersListApiView, CustomerDetailApiView, LicencesListApiView, LicenceDetailApiView,
                    OrdersListApiView, OrderDetailApiView)

urlpatterns = [
    path('work/', WorkTypeApiView.as_view(), name='Work_Type_List'),
    path('work/<str:work_name>', WorkTypeDetailApiView.as_view()),
    path('expanses/', ExpansesListApiView.as_view()),
    path('expanses/<str:expanses_name>', ExpansesDetailApiView.as_view()),
    path('customers/', CustomersListApiView.as_view()),
    path('customers/<int:customer_id>', CustomerDetailApiView.as_view()),
    path('licences/', LicencesListApiView.as_view()),
    path('licences/<int:licence_id>', LicenceDetailApiView.as_view()),
    path('orders/', OrdersListApiView.as_view()),
    path('orders/<int:order_id>', OrderDetailApiView.as_view()),

]
