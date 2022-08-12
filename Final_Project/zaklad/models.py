from django.db import models
from django.contrib.auth.models import User


class Work_Type(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=180, unique=True)
    machine_usage = models.IntegerField(blank=False)




class Expanses(models.Model):
    name = models.CharField(max_length=120, unique=True, default='Obecne wydatki')
    actual = models.BooleanField(default=False)
    energy = models.FloatField(default=0)
    salary = models.FloatField(default=0)
    others = models.FloatField(default=0)



class Customers(models.Model):
    id = models.BigAutoField(primary_key=True)
    individual = models.BooleanField(default=True)
    name = models.CharField(max_length=60)
    surname = models.CharField(max_length=60, blank=True)
    telephone = models.IntegerField(blank=True)
    e_address = models.EmailField(blank=True)
    address = models.CharField(max_length=120, blank=True)


class Licences(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.CharField(max_length=120)
    serial_number = models.CharField(max_length=60, unique=True)
    realise_date = models.DateField()
    authority = models.CharField(max_length=120)
    owner = models.ForeignKey(Customers, on_delete=models.CASCADE)


class Orders(models.Model):
    id = models.BigAutoField(primary_key=True)
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    ready = models.BooleanField(default=False)
    concession = models.BooleanField(default=True)
    serial_number = models.CharField(max_length=25, blank=True)
    name = models.CharField(max_length=60, blank=True)
    producer = models.CharField(max_length=60, blank=True)
    production_year = models.IntegerField(blank=True)
    description = models.CharField(max_length=500)
    work_types = models.ManyToManyField(Work_Type)
    order_creation_date = models.DateField(auto_now_add=True)
    start_time = models.TimeField(default='00:00:00')
    stop_time = models.TimeField(default='00:00:00')
    work_time = models.IntegerField(default=0)
    cost = models.FloatField(default=100)



