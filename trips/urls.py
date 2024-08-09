# trips/urls.py
from django.urls import path
from .views import TripListAPIView, TripDetailAPIView, AboutContentAPIView

urlpatterns = [
    path('getTrips', TripListAPIView.as_view()),  # URL for listing trips
    path('tripDetail/<int:pk>', TripDetailAPIView.as_view()),  # URL for trip details
    path('about/<int:pk>', AboutContentAPIView.as_view()), # URL to get, update & delete about content
]
