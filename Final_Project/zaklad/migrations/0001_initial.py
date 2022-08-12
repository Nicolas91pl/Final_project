# Generated by Django 4.0.5 on 2022-08-12 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('individual', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=60)),
                ('surname', models.CharField(blank=True, max_length=60)),
                ('telephone', models.IntegerField(blank=True)),
                ('e_address', models.EmailField(blank=True, max_length=254)),
                ('address', models.CharField(blank=True, max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Expanses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Obecne wydatki', max_length=120, unique=True)),
                ('actual', models.BooleanField(default=False)),
                ('energy', models.FloatField(default=0)),
                ('salary', models.FloatField(default=0)),
                ('others', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Work_Type',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=180, unique=True)),
                ('machine_usage', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('active', models.BooleanField(default=True)),
                ('ready', models.BooleanField(default=False)),
                ('concession', models.BooleanField(default=True)),
                ('serial_number', models.CharField(blank=True, max_length=25)),
                ('name', models.CharField(blank=True, max_length=60)),
                ('producer', models.CharField(blank=True, max_length=60)),
                ('production_year', models.IntegerField(blank=True)),
                ('description', models.CharField(max_length=500)),
                ('order_creation_date', models.DateField(auto_now_add=True)),
                ('start_time', models.TimeField(default='00:00:00')),
                ('stop_time', models.TimeField(default='00:00:00')),
                ('work_time', models.IntegerField(default=0)),
                ('cost', models.FloatField(default=100)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zaklad.customers')),
                ('work_types', models.ManyToManyField(to='zaklad.work_type')),
            ],
        ),
        migrations.CreateModel(
            name='Licences',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=120)),
                ('serial_number', models.CharField(max_length=60, unique=True)),
                ('realise_date', models.DateField()),
                ('authority', models.CharField(max_length=120)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zaklad.customers')),
            ],
        ),
    ]
