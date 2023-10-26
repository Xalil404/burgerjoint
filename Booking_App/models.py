from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


def get_current_date():
    return timezone.now()

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=50, null=False, blank=False)
    phone_number = models.CharField(max_length=15, null=False, blank=False, default='085 123 3434')
    email = models.EmailField(null=False, blank=False, default='myemail@gmail.com')
    number_of_people = models.IntegerField(null=False, blank=False, default=1)
    booking_date = models.DateTimeField(
        null=False,
        blank=False,
        default=get_current_date  
    )
    booking_time = models.TimeField(
        null=False,
        blank=False,
        default=timezone.now 
    )
    meals_desired = models.CharField(
        max_length=80,
        choices=[
            ('CHARBURGER WITH CHEESE', 'CHARBURGER WITH CHEESE'),
            ('CHARBURGER', 'CHARBURGER'),
            ('DOUBLE CHAR WITH CHEESE', 'DOUBLE CHAR WITH CHEESE'),
            ('BBQ CHAR WITH CHEESE', 'BBQ CHAR WITH CHEESE'),
            ('PORTABELLA CHAR', 'PORTABELLA CHAR'),
            ('TERIYAKI CHAR', 'TERIYAKI CHAR'),
            ('GRILLED CHICKEN-WICH', 'GRILLED CHICKEN-WICH'),
            ('SPICY CRISPY CHICKEN', 'SPICY CRISPY CHICKEN'),
            ('CHICKEN CLUB', 'CHICKEN CLUB'),
            ('AHI TUNA FILET', 'AHI TUNA FILET'),
            ('VEGGIE BURGER', 'VEGGIE BURGER'),
            ('VEGGIE CHEESE BURGER', 'VEGGIE CHEESE BURGER'),
            ('CHICKEN CAESAR', 'CHICKEN CAESAR'),
            ('GARDEN SALAD', 'GARDEN SALAD'),
            ('10 PCS CRISPY', '10 PCS CRISPY'),
            ('FRENCH FRIES', 'FRENCH FRIES'),
            ('ONION RINGS', 'ONION RINGS'),
        ],
        null=False,
        blank=False,
        default='CHARBURGER'
    )

    def __str__(self):
        return self.name
