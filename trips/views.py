from .models import Trip
from .serializers import TripSerializer
from rest_framework import generics, filters
from django.utils import timezone
from django.core.mail import send_mail
from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.conf import settings

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


@api_view(['POST'])
def send_email(request):
    data = request.data
    subject = data.get('subject', 'No Subject')
    message = data.get('message', '')
    recipient_list = [data.get('email')]

    try:
        send_mail(
                    subject,
                    message,
                    settings.EMAIL_HOST_USER,
                    recipient_list,
                )
        return JsonResponse({'message': 'Email sent successfully!'}, status=200)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

