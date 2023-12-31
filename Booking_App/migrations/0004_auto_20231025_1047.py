# Generated by Django 3.2.22 on 2023-10-25 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Booking_App', '0003_auto_20231025_1035'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='meals_desired',
        ),
        migrations.AddField(
            model_name='booking',
            name='meals_desired',
            field=models.CharField(choices=[('CHARBURGER WITH CHEESE', 'CHARBURGER WITH CHEESE'), ('CHARBURGER', 'CHARBURGER'), ('DOUBLE CHAR WITH CHEESE', 'DOUBLE CHAR WITH CHEESE'), ('BBQ CHAR WITH CHEESE', 'BBQ CHAR WITH CHEESE'), ('PORTABELLA CHAR', 'PORTABELLA CHAR'), ('TERIYAKI CHAR', 'TERIYAKI CHAR'), ('GRILLED CHICKEN-WICH', 'GRILLED CHICKEN-WICH'), ('SPICY CRISPY CHICKEN', 'SPICY CRISPY CHICKEN'), ('CHICKEN CLUB', 'CHICKEN CLUB'), ('AHI TUNA FILET', 'AHI TUNA FILET'), ('VEGGIE BURGER', 'VEGGIE BURGER'), ('VEGGIE CHEESE BURGER', 'VEGGIE CHEESE BURGER'), ('CHICKEN CAESAR', 'CHICKEN CAESAR'), ('GARDEN SALAD', 'GARDEN SALAD'), ('10 PCS CRISPY', '10 PCS CRISPY'), ('FRENCH FRIES', 'FRENCH FRIES'), ('ONION RINGS', 'ONION RINGS')], default='Burger', max_length=80),
        ),
        migrations.DeleteModel(
            name='Meal',
        ),
    ]
