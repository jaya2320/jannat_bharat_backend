from .models import About
from .serializers import AboutSerializer
from rest_framework import generics
    
class AboutContentAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer
