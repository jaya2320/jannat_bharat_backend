# trips/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('getTrips/', views.trip_list),  # URL for listing trips
    path('<int:pk>/', views.trip_detail),  # URL for trip details
]