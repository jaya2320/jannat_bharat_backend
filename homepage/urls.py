from django.urls import path
from .views import AboutContentAPIView, GalleryAPIView, ReviewAPIView

urlpatterns = [
    path('about/', AboutContentAPIView.as_view()), # URL to get about content
    path('gallery/', GalleryAPIView.as_view()), # URL to get gallery images
    path('reviews/', ReviewAPIView.as_view()), # URL to get reviews
]
