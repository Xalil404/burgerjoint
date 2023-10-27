"""BurgerJoint URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from Booking_App.views import get_home_page, addtable, edit_booking, delete_booking  
from Booking_App.views import booktable, view_delivery, create_delivery, edit_delivery, delete_delivery

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_home_page, name='home'),
    path('accounts/', include('allauth.urls'), name='account'),
    path('booktable/', booktable, name='booktable'),
    path('addtable/', addtable, name='addtable'),
    path('edit_booking/<booking_id>', edit_booking, name='edit_booking'),
    path('delete/<booking_id>', delete_booking, name='delete_booking'),
    path('view_delivery/', view_delivery, name='view_delivery'),
    path('create_delivery/', create_delivery, name='create_delivery'),
    path('edit_delivery/<delivery_id>', edit_delivery, name='edit_delivery'),
    path('delete_delivery/<delivery_id>', delete_delivery, name='delete_delivery'),
]

#Code to serve static files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])

