# Generated by Django 5.1.2 on 2024-11-22 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brands_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='brand_type',
            field=models.CharField(choices=[('BMW', 'Bmw'), ('MAZDA', 'Mazda'), ('TOYOTA', 'Toyota'), ('MERCEDES', 'Mercedes'), ('JEEP', 'Jeeb'), ('FORD', 'Ford'), ('DODGE', 'Dodge')], default='manufacturer', max_length=20),
        ),
    ]
