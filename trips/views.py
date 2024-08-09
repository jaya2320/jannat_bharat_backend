from .models import Trip
from .serializers import TripSerializer
from rest_framework import generics, filters
from django.utils import timezone

# Create your views here.
class TripDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

class TripListAPIView(generics.ListCreateAPIView):
    serializer_class = TripSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['start_date']

    # return only the trips with start start date > today's date
    def get_queryset(self):
        today = timezone.now().date()  # Get today's date without time
        return Trip.objects.filter(start_date__gt=today)

