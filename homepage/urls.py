from django.urls import path
from .views import (
    BannerImagesAPIView,
    AboutContentAPIView,
    GalleryAPIView,
    ReviewAPIView,
    ContactAPIView,
)

urlpatterns = [
    path("banners/", BannerImagesAPIView.as_view()),  # URL to get banner images
    path("about/", AboutContentAPIView.as_view()),  # URL to get about content
    path("gallery/", GalleryAPIView.as_view()),  # URL to get gallery images
    path("reviews/", ReviewAPIView.as_view()),  # URL to get reviews
    path("contacts/", ContactAPIView.as_view()),  # URL to get contacts
]
