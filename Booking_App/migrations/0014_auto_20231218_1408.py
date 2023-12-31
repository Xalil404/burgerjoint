# Generated by Django 3.2.22 on 2023-12-18 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Booking_App', '0013_alter_meal_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='booking',
            name='number_of_people',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='booking',
            name='phone_number',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='phone_number',
            field=models.CharField(max_length=15),
        ),
    ]
