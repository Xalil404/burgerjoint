from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'phone_number', 'email', 'number_of_people', 'booking_date', 'booking_time', 'meals_desired']
        widgets = {
            'booking_date': forms.DateInput(attrs={'type': 'date'}),
            'user': forms.HiddenInput(),
        }
