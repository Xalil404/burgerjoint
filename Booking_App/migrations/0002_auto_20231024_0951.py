# Generated by Django 3.2.22 on 2023-10-24 09:51

import Booking_App.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Booking_App', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='done',
        ),
        migrations.AddField(
            model_name='booking',
            name='booking_date',
            field=models.DateTimeField(default=Booking_App.models.get_current_date),
        ),
        migrations.AddField(
            model_name='booking',
            name='email',
            field=models.EmailField(default='myemail@gmail.com', max_length=254),
        ),
        migrations.AddField(
            model_name='booking',
            name='meals_desired',
            field=models.CharField(choices=[('Burger', 'Burger'), ('Pizza', 'Pizza'), ('Fries', 'Fries'), ('Cheese Burger', 'Cheese Burger'), ('Cola', 'Cola'), ('Pepsi', 'Pepsi')], default='Burger', max_length=20),
        ),
        migrations.AddField(
            model_name='booking',
            name='number_of_people',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='booking',
            name='phone_number',
            field=models.CharField(default='085 123 3434', max_length=15),
        ),
    ]
