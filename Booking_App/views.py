from django.shortcuts import render, redirect 
from django.contrib.auth.decorators import login_required
from django.views import generic 
from django.conf import settings
from .models import Booking 

# Create your views here.
def get_home_page(request):
    return render(request, 'index.html')

@login_required
def booktable(request):
    bookings = Booking.objects.all()
    context = {
        'bookings': bookings
    }

    return render(request, 'booktable.html', {'bookings': bookings}) 

def addtable(request):
    if request.method == 'POST':
        name = request.POST.get('item_name')
        done = 'done' in request.POST
        Booking.objects.create(name=name, done=done)

        return redirect('booktable')
    return render(request, 'addtable.html')