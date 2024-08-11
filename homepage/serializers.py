from rest_framework import serializers
from .models import About, GalleryImage, Review


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = "__all__"


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryImage
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"
