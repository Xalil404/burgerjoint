# Generated by Django 3.2.22 on 2023-12-19 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Booking_App', '0014_auto_20231218_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='meals_desired',
            field=models.ManyToManyField(to='Booking_App.Meal'),
        ),
    ]
