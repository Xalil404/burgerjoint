from django.shortcuts import render
from django.views import generic 

# Create your views here.
def get_home_page(request):
    return render(request, 'index.html')
