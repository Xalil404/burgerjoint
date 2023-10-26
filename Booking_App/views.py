from django.shortcuts import render, redirect, get_object_or_404 
from django.contrib.auth.decorators import login_required
from django.views import generic 
from django.conf import settings
from .models import Booking 
from .forms import BookingForm    


# Create your views here.
def get_home_page(request):
    return render(request, 'index.html')

@login_required
def booktable(request):
    bookings = Booking.objects.filter(user=request.user)
    context = {
        'bookings': bookings
    }

    return render(request, 'booktable.html', {'bookings': bookings}) 


def addtable(request):
    if request.method == 'POST':
        form=BookingForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()

        return redirect('booktable')
    form=BookingForm()
    context={
        'form': form
    }
    return render(request, 'addtable.html', context)


def edit_booking(request, booking_id):
    item = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST':
        form  = BookingForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('booktable')
    form = BookingForm(instance=item)
    context = {
        'form': form
    }
    return render(request, 'edit_booking.html', context)


def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    booking.delete()
    return redirect('booktable')
