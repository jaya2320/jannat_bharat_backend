# trips/serializers.py
from rest_framework import serializers
from .models import Trip, Itinerary, MustKnow, PickupDetails, Policies, InquiryContact


class ItinerarySerializer(serializers.ModelSerializer):
    class Meta:
        model=Itinerary
        fields="__all__"

class MustKnowSerializer(serializers.ModelSerializer):
    class Meta:
        model=MustKnow
        fields="__all__"

class PoliciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Policies
        fields="__all__"

class PickupDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=PickupDetails
        fields="__all__"

class InquiryContactSerializer(serializers.ModelSerializer):
    class Meta:
        model=InquiryContact
        fields="__all__"

class TripSerializer(serializers.ModelSerializer):
    itineraries = ItinerarySerializer(many=True, read_only=True)
    mustKnow = MustKnowSerializer(many=True, read_only=True)
    pickupDetails= PickupDetailsSerializer(many=True,read_only=True)
    policy_details = PoliciesSerializer(read_only=True)
    inquiry_contact_details = InquiryContactSerializer(read_only=True)
    class Meta:
        model = Trip
        fields = ["id","title","banner_image","overview","duration","start_date","end_date","type_of_group"
                  ,"inquiry_contact_details","itineraries","mustKnow","pickupDetails","policy_details", "pdf"]



