from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
#class Booking(models.Model):
#    name = models.CharField(max_length=50, null=False, blank=False)
#    done = models.BooleanField(null=False, blank=False, default=False) 
#
#    def __str__(self):
#        return self.name

def get_current_date():
    return timezone.now()

class Booking(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    phone_number = models.CharField(max_length=15, null=False, blank=False, default='085 123 3434')
    email = models.EmailField(null=False, blank=False, default='myemail@gmail.com')
    number_of_people = models.IntegerField(null=False, blank=False, default=1)
    booking_date = models.DateTimeField(
        null=False,
        blank=False,
        default=get_current_date  
    )
    meals_desired = models.CharField(
        max_length=20,
        choices=[
            ('Burger', 'Burger'),
            ('Pizza', 'Pizza'),
            ('Fries', 'Fries'),
            ('Cheese Burger', 'Cheese Burger'),
            ('Cola', 'Cola'),
            ('Pepsi', 'Pepsi'),
            # Add more menu items here
        ],
        null=False,
        blank=False,
        default='Burger'
    )

    def __str__(self):
        return self.name
