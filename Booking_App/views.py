from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.conf import settings
from .models import Booking, Delivery
from .forms import BookingForm, DeliveryForm


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


@login_required
def addtable(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()

        return redirect('booktable')
    form = BookingForm()
    context = {
        'form': form
    }
    return render(request, 'addtable.html', context)


@login_required
def edit_booking(request, booking_id):
    item = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=item)
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


@login_required
def view_delivery(request):
    deliveries = Delivery.objects.filter(user=request.user)
    context = {
        'deliveries': deliveries,
    }

    return render(request, 'view_delivery.html', context)


@login_required
def create_delivery(request):
    if request.method == 'POST':
        form = DeliveryForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()

        return redirect('view_delivery')
    form = DeliveryForm()
    context = {
        'form': form
    }
    return render(request, 'create_delivery.html', context)


@login_required
def edit_delivery(request, delivery_id):
    item = get_object_or_404(Delivery, id=delivery_id)
    if request.method == 'POST':
        form = DeliveryForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('view_delivery')
    form = DeliveryForm(instance=item)
    context = {
        'form': form
    }
    return render(request, 'edit_delivery.html', context)


def delete_delivery(request, delivery_id):
    delivery = get_object_or_404(Delivery, id=delivery_id)
    delivery.delete()
    return redirect('view_delivery')
