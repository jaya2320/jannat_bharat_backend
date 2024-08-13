# trips/urls.py
from django.urls import path
from .views import TripListAPIView, TripDetailAPIView,send_email

urlpatterns = [
    path('getTrips', TripListAPIView.as_view()),  # URL for listing trips
    path('tripDetail/<int:pk>', TripDetailAPIView.as_view()),  # URL for trip details
     path('send-email/', send_email, name='send_email'),
]
