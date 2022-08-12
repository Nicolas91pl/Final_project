from rest_framework import serializers
from .models import Work_Type, Expanses, Customers, Licences, Orders


class WorkTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work_Type
        fields = ['id', "name", "machine_usage"]


class ExpansesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expanses
        fields = ['name', 'actual', 'energy', 'salary', 'others']


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = ['id', 'individual', 'name', 'surname',
                  'telephone', 'e_address', 'address']

class LicencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Licences
        fields = ['id', 'type', 'serial_number', 'realise_date', 'authority', 'owner']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ['id', 'customer', 'active', 'ready',
                  'concession', 'serial_number', 'name',
                  'producer', 'production_year', 'description',
                  'work_types', 'order_creation_date', 'start_time',
                  'stop_time', 'work_time', 'cost']

