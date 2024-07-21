from django.shortcuts import render, get_object_or_404
from .models import Trip
from .serializers import TripSerializer
from rest_framework import generics

# Create your views here.
class TripDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

class TripListAPIView(generics.ListCreateAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
