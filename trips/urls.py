# trips/urls.py
from django.urls import path
from . import views
from .views import TripListAPIView, TripDetailAPIView

urlpatterns = [
    path('getTrips/', TripListAPIView.as_view()),  # URL for listing trips
    path('tripDetail/<int:pk>', TripDetailAPIView.as_view()),  # URL for trip details
]