# Generated by Django 5.1.2 on 2024-11-22 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='photo',
            field=models.ImageField(default='images/defult.jpg', upload_to='images/'),
        ),
    ]
