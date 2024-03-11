from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('check_availability', views.check_availability, name='check_availability'),
    path('submit_booking/', views.submit_booking, name='submit_booking'),
]