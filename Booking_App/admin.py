from django.contrib import admin
from django import forms
from .models import Booking, Delivery, Meal


class MealsDesiredInlineFormset(forms.BaseInlineFormSet):
    model = Delivery.meals_desired.through
    extra = 1  


class MealsDesiredInline(admin.TabularInline):
    model = Delivery.meals_desired.through
    extra = 1  
    formset = MealsDesiredInlineFormset
    

class DeliveryAdmin(admin.ModelAdmin):
    inlines = [MealsDesiredInline]
    

# Register your models here.
admin.site.register(Booking)
admin.site.register(Delivery, DeliveryAdmin)
admin.site.register(Meal)
