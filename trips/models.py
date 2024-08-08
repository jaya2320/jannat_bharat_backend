from django.db import models
from django.core.exceptions import ValidationError
from ckeditor.fields import RichTextField


class InquiryContact(models.Model):
    email = models.EmailField()
    mobile_number = models.CharField(max_length=15)
    def __str__(self):
        return f"{self.email}"

class Policies(models.Model):
    policy_name = models.CharField(max_length=100)
    why_us= RichTextField(blank=True, null=True)
    cancellation_policy=RichTextField(blank=True, null=True)
    terms_and_conditions = RichTextField()
    
    def __str__(self):
        return self.policy_name


class MustKnow(models.Model):
    trip = models.ForeignKey('Trip', related_name='mustKnow', on_delete=models.CASCADE)
    inclusions = RichTextField(blank=True, null=True)
    exclusions = RichTextField(blank=True, null=True)
    thingsToCarry = RichTextField(blank=True, null=True)

    def __str__(self):
        return "MustKnow"


class PickupDetails(models.Model):
    trip = models.ForeignKey('Trip', related_name='pickupDetails', on_delete=models.CASCADE)
    pickup_point = models.CharField(max_length=255)
    pickup_location = models.CharField(max_length=255)
    arrival_timing = models.CharField(max_length=10)
    departure_timing = models.CharField(max_length=10)
    quad_sharing_price = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)
    triple_sharing_price = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)
    double_sharing_price = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)
    single_price = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)
    # per_person_price = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)
    
    def __str__(self):
        return f"{self.pickup_point} at {self.arrival_timing}"


class Itinerary(models.Model):
    trip = models.ForeignKey('Trip', related_name='itineraries', on_delete=models.CASCADE)
    day = models.PositiveIntegerField()
    title = models.CharField(blank=True,max_length=200)
    details = RichTextField()

    def __str__(self):
        return f"Day {self.day} - {self.trip.title}"

    def clean(self):
        if self.day==None:
            raise ValidationError('Day is required.')
        if not self.details:
            raise ValidationError('Details is required.')


class Trip(models.Model):
    title = models.CharField(max_length=200)
    banner_image = models.ImageField(upload_to='banners/')
    overview= RichTextField()
    duration = models.PositiveIntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    type_of_group=models.CharField(max_length=20)
    policy_details=models.ForeignKey(Policies,on_delete=models.CASCADE, related_name='policies')
    inquiry_form = models.ForeignKey(InquiryContact,on_delete=models.CASCADE, related_name='inquiries')
    pdf = models.FileField(upload_to='uploads/', verbose_name='PDF', blank=True, null=True)

    def __str__(self):
        return self.title


'''
daywise itinerary:-
title (not required)

pickup_point:-
arrival time, departuretime, timings should be choose from time picker, pickuploaction is required
make price details, some notes as not required


inquiry form email and phone number to be picked from list

trip details should also include onetoone for why choose us? inclusion exclusion extra details
'''
