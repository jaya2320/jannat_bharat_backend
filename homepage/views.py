from rest_framework import generics
from django.http import Http404
from .models import About, GalleryImage, Review
from .serializers import AboutSerializer, GallerySerializer, ReviewSerializer


class AboutContentAPIView(generics.RetrieveAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer

    def get_object(self, queryset=None):
        # Retrieve the first instance or return None if the queryset is empty
        instance = About.objects.all().first()

        if instance is None:
            raise Http404("Please add About content")

        return instance


class GalleryAPIView(generics.ListCreateAPIView):
    queryset = GalleryImage.objects.all()
    serializer_class = GallerySerializer


class ReviewAPIView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
