from django.urls import path
from .views import AboutContentAPIView

urlpatterns = [
    path('<int:pk>', AboutContentAPIView.as_view()), # URL to get, update & delete about content
]
