from django import forms
from .models import Booking, Delivery
from django.contrib import admin


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'phone_number', 'email', 'number_of_people', 'booking_date', 'booking_time', 'meals_desired']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter your name'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Enter your phone number'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email'}),
            'number_of_people': forms.NumberInput(attrs={'placeholder': 'Enter the number of people'}),
            'booking_date': forms.DateInput(attrs={'type': 'date'}),
            'booking_time': forms.Select(choices=[(f"{hour:02d}:{minute:02d}", f"{hour:02d}:{minute:02d}") for hour in range(10, 18) for minute in range(0, 60, 15)], attrs={'class': 'form-select'}),
            'user': forms.HiddenInput(),
        }


class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = ['name', 'phone_number', 'address', 'city', 'booking_date', 'meals_desired', 'additional_information']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter your name'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Enter your phone number'}),
            'address': forms.TextInput(attrs={'placeholder': 'Enter your address'}),
            'city': forms.TextInput(attrs={'placeholder': 'Enter your city'}),
            'additional_information': forms.Textarea(attrs={'placeholder': 'Enter additional information'}),
            'booking_date': forms.DateInput(attrs={'type': 'date'}),
            'user': forms.HiddenInput(),
        }
        labels = {
            'meals_desired': 'Meals Desired (Press Control on Windows or Command on Mac to select multiple items)',
        }
