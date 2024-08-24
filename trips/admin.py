from django.contrib import admin
from .models import Trip, InquiryContact, Policies, PickupDetails, Itinerary, MustKnow
from django.core.exceptions import ValidationError

class ItineraryInline(admin.TabularInline):
    model = Itinerary
    extra = 1  # One extra blank form by default
    can_delete = False  # Disable the delete option

    def has_add_permission(self, request, obj=None):
        if obj and obj.duration and self.model.objects.filter(trip=obj).count() >= obj.duration:
            return False
        return True

    def save_model(self, request, obj, form, change):
        if obj.pk:  # If the trip already exists
            itineraries = Itinerary.objects.filter(trip=obj)
            if itineraries.count() < obj.duration:
                raise ValidationError(f'Trip must have exactly {obj.duration} itineraries.')
        super().save_model(request, obj, form, change)

class MustKnowInline(admin.StackedInline):
    model = MustKnow
    extra = 1  # One extra blank form
    max_num = 1  # Limit to only one form
    can_delete = False  # Disable the delete option

    def has_add_permission(self, request, obj=None):
        # Allow adding only if there's no itinerary
        if obj and self.model.objects.filter(trip=obj).count() >= 1:
            return False
        return True

class PickUpDetailsInline(admin.TabularInline):
    model = PickupDetails
    extra = 1


class TripAdmin(admin.ModelAdmin):
    inlines = [ItineraryInline,PickUpDetailsInline,MustKnowInline]
    list_display=("title","start_date","end_date","duration")

class InquiryContactAdmin(admin.ModelAdmin):
    list_display=("email","mobile_number")

admin.site.register(Trip, TripAdmin)
admin.site.register(InquiryContact,InquiryContactAdmin)
admin.site.register(Policies)

