from .models import Trip
from .serializers import TripSerializer
from rest_framework import generics, filters

# Create your views here.
class TripDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

class TripListAPIView(generics.ListCreateAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['start_date']
