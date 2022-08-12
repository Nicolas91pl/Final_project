from decimal import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Work_Type, Expanses, Customers, Licences, Orders
from .serializers import WorkTypeSerializer, ExpansesSerializer, CustomerSerializer, LicencesSerializer, OrderSerializer
from datetime import datetime

class WorkTypeApiView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, *args, **kwargs):
        work = Work_Type.objects.all()
        serializer = WorkTypeSerializer(work, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            'name': request.data.get('name'),
            'machine_usage': request.data.get('machine_usage')
        }
        serializer = WorkTypeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WorkTypeDetailApiView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get_object(self, work_name):
        try:
            return Work_Type.objects.get(name=work_name)
        except Work_Type.DoesNotExist:
            return None

    def get(self, request, work_name, *args, **kwargs):
        work_instance = self.get_object(work_name)
        if not work_instance:
            return Response(
                {"res": "Work with this name does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = WorkTypeSerializer(work_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, work_name, *args, **kwargs):
        work_instance = self.get_object(work_name)
        if not work_instance:
            return Response(
                {"res": "Work with this name does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'name': request.data.get('name'),
            'machine_usage': request.data.get('machine_usage'),
        }
        serializer = WorkTypeSerializer(instance=work_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, work_name, *args, **kwargs):
        work_instance = self.get_object(work_name)
        if not work_instance:
            return Response(
                {"res": "Work with this name does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        work_instance.delete()
        return Response(
            {"res": "Work type deleted!"},
            status=status.HTTP_200_OK
        )

class ExpansesListApiView(WorkTypeDetailApiView):
    permission_classes = [permissions.IsAdminUser]
    def get(self, request, *args, **kwargs):
        expanses = Expanses.objects.all()
        serializer = ExpansesSerializer(expanses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            'name': request.data.get('name'),
            'actual': request.data.get('actual'),
            'energy': request.data.get('energy'),
            'salary': request.data.get('salary'),
            'others': request.data.get('others')
        }
        serializer = ExpansesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ExpansesDetailApiView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get_object(self, expanses_name):
        try:
            return Expanses.objects.get(name=expanses_name)
        except Expanses.DoesNotExist:
            return None

    def get(self, request, expanses_name, *args, **kwargs):
        expanses_instance = self.get_object(expanses_name)
        if not expanses_instance:
            return Response(
                {"res": "Expanses with this name does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = ExpansesSerializer(expanses_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, expanses_name, *args, **kwargs):
        expanses_instance = self.get_object(expanses_name)
        if not expanses_instance:
            return Response(
                {"res": "Expanses with this name does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'name': request.data.get('name'),
            'actual': request.data.get('actual'),
            'energy': request.data.get('energy'),
            'salary': request.data.get('salary'),
            'others': request.data.get('others')
        }
        serializer = ExpansesSerializer(instance=expanses_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, expanses_name, *args, **kwargs):
        expanses_instance = self.get_object(expanses_name)
        if not expanses_instance:
            return Response(
                {"res": "Expanses with this name does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        expanses_instance.delete()
        return Response(
            {"res": "Expanses deleted!"},
            status=status.HTTP_200_OK
        )

class CustomersListApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, *args, **kwargs):
        customers = Customers.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            'individual': request.data.get('individual'),
            'name': request.data.get('name'),
            'surname': request.data.get('surname'),
            'telephone': request.data.get('telephone'),
            'e_address': request.data.get('e_address'),
            'address': request.data.get('address'),
            }
        serializer = CustomerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomerDetailApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, customer_id):
        try:
            return Customers.objects.get(id=customer_id)
        except Customers.DoesNotExist:
            return None

    def get(self, request, customer_id, *args, **kwargs):
        customer_instance = self.get_object(customer_id)
        if not customer_instance:
            return Response(
                {"res": "Customer does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = CustomerSerializer(customer_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, customer_id, *args, **kwargs):
        customer_instance = self.get_object(customer_id)
        if not customer_instance:
            return Response(
                {"res": "Customer does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'individual': request.data.get('individual'),
            'name': request.data.get('name'),
            'surname': request.data.get('surname'),
            'telephone': request.data.get('telephone'),
            'e_address': request.data.get('e_address'),
            'address': request.data.get('address'),
        }
        serializer = CustomerSerializer(instance=customer_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, customer_id, *args, **kwargs):
        customer_instance = self.get_object(customer_id)
        if not customer_instance:
            return Response(
                {"res": "Customer does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        customer_instance.delete()
        return Response(
            {"res": "Customer deleted!"},
            status=status.HTTP_200_OK
        )

class LicencesListApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, *args, **kwargs):
        licences = Licences.objects.all()
        serializer = LicencesSerializer(licences, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            'type': request.data.get('type'),
            'serial_number': request.data.get('serial_number'),
            'realise_date': request.data.get('realise_date'),
            'authority': request.data.get('authority'),
            'owner': request.data.get('owner'),
            }
        serializer = LicencesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LicenceDetailApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, licence_id):
        try:
            return Licences.objects.get(id=licence_id)
        except Licences.DoesNotExist:
            return None

    def get(self, request, licence_id, *args, **kwargs):
        licence_instance = self.get_object(licence_id)
        if not licence_instance:
            return Response(
                {"res": "Licence does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = LicencesSerializer(licence_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, licence_id, *args, **kwargs):
        licence_instance = self.get_object(licence_id)
        if not licence_instance:
            return Response(
                {"res": "Licence does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'type': request.data.get('type'),
            'serial_number': request.data.get('serial_number'),
            'realise_date': request.data.get('realise_date'),
            'authority': request.data.get('authority'),
            'owner': request.data.get('owner'),
        }
        serializer = LicencesSerializer(instance=licence_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, licence_id, *args, **kwargs):
        licence_instance = self.get_object(licence_id)
        if not licence_instance:
            return Response(
                {"res": "Licence does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        licence_instance.delete()
        return Response(
            {"res": "Licence deleted!"},
            status=status.HTTP_200_OK
        )

class OrdersListApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, *args, **kwargs):
        orders = Orders.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            'customer': request.data.get('customer'),
            'active': request.data.get('active'),
            'ready': request.data.get('ready'),
            'concession': request.data.get('concession'),
            'serial_number': request.data.get('serial_number'),
            'name': request.data.get('name'),
            'producer': request.data.get('producer'),
            'production_year': request.data.get('production_year'),
            'description': request.data.get('description'),
            'work_types': request.data.get('work_types'),
            'cost': request.data.get('cost'),
            }
        serializer = OrderSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderDetailApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, order_id):
        try:
            return Orders.objects.get(id=order_id)
        except Orders.DoesNotExist:
            return None

    def get(self, request, order_id, *args, **kwargs):
        order_instance = self.get_object(order_id)
        if not order_instance:
            return Response(
                {"res": "Order does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = OrderSerializer(order_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # def start_work(self, request, order_id, *args, **kwargs):
    #     order_instance = self.get_object(order_id)
    #     if not order_instance:
    #         return Response(
    #             {"res": "Order does not exists"},
    #             status=status.HTTP_400_BAD_REQUEST
    #         )
    #     data = {'start_time': datetime.now().time()}
    #     serializer = OrderSerializer(instance=order_instance, data=data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #
    # def stop_work(self, request, order_id, *args, **kwargs):
    #     order_instance = self.get_object(order_id)
    #     if not order_instance:
    #         return Response(
    #             {"res": "Order does not exists"},
    #             status=status.HTTP_400_BAD_REQUEST
    #         )
    #
    #     stop_time = datetime.now().time()
    #     start_time = order_instance.start_time
    #     s1 = str(stop_time).split(':')
    #     s2 = str(start_time).split(':')
    #     work_time = order_instance.work_time
    #     work_time += int(s1[0]) - int(s2[0])
    #     if int(s1[1]) - int(s2[1]) < 0:
    #         result = 60 - int(s1[1]) - int(s2[1])
    #         if result < 20:
    #             work_time = work_time - 1
    #     elif int(s1[1]) - int(s2[1]) > 30:
    #         work_time = work_time + 1
    #
    #     data = {'stop_time': stop_time,
    #             'work_time': work_time}
    #     serializer = OrderSerializer(instance=order_instance, data=data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, order_id, *args, **kwargs):
        order_instance = self.get_object(order_id)
        if not order_instance:
            return Response(
                {"res": "Order does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        order_instance = self.get_object(order_id)
        if not order_instance:
            return Response(
                {"res": "Order does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        expanses_instance = Expanses.objects.get(name='Obecne')
        getcontext().prec = 4
        work_list = order_instance.work_types
        mid_others_cost = Decimal((float(expanses_instance.salary) + float(expanses_instance.others)) / 165)
        mid_energy_cost = Decimal(float(expanses_instance.energy) / 165)
        mid_machine_usage = 57
        # for i in work_list:
        #     mid_machine_usage += Work_Type.objects.get(id=i).machine_usage
        # mid_machine_usage = Decimal(mid_machine_usage / 100 / len(work_list))
        cost = Decimal(((mid_machine_usage * mid_energy_cost) + mid_others_cost) * int(order_instance.work_time))
        data = {
            'customer': request.data.get('customer'),
            'active': request.data.get('active'),
            'ready': request.data.get('ready'),
            'concession': request.data.get('concession'),
            'serial_number': request.data.get('serial_number'),
            'name': request.data.get('name'),
            'producer': request.data.get('producer'),
            'production_year': request.data.get('production_year'),
            'description': request.data.get('description'),
            'work_types': request.data.get('work_types'),
            'order_creation_date': request.data.get('order_creation_date'),
            'start_time': request.data.get('start_time'),
            'stop_time': request.data.get('stop_time'),
            'work_time': request.data.get('work_time'),
            'cost': cost,
        }
        serializer = OrderSerializer(instance=order_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, order_id, *args, **kwargs):
        order_instance = self.get_object(order_id)
        if not order_instance:
            return Response(
                {"res": "Order does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        order_instance.delete()
        return Response(
            {"res": "Order deleted!"},
            status=status.HTTP_200_OK
        )
