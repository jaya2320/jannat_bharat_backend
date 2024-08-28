from django.db import models
from django.core.exceptions import ValidationError
from ckeditor.fields import RichTextField

class Visit(models.Model):
    count = models.PositiveIntegerField(default=0)


class BannerImage(models.Model):
    homepage = models.ForeignKey(
        "HomePage", related_name="banner_images", on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="homepage/banner_images/")
    # caption = models.CharField(max_length=255)

    def __str__(self):
        return f"Banner Image {self.id}"


class About(models.Model):
    about_content = RichTextField()
    homepage = models.ForeignKey(
        "HomePage", related_name="about_us", on_delete=models.CASCADE
    )

    def __str__(self):
        return "About"


class GalleryImage(models.Model):
    homepage = models.ForeignKey(
        "HomePage", related_name="gallery_images", on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="homepage/gallery_images/")
    caption = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Image {self.id}"


ALLOWED_RATING_VALUES = {1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5}


def validate_allowed_rating_value(value):
    if value not in ALLOWED_RATING_VALUES:
        raise ValidationError(f"Value must be one of {ALLOWED_RATING_VALUES}.")


def validate_review_length(value):
    if len(value.split(" ")) >= 100:
        raise ValidationError('Content is too long. Please limit to 100 words.')


class Review(models.Model):
    homepage = models.ForeignKey(
        "HomePage", related_name="reviews", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)
    review = RichTextField(validators=[validate_review_length])
    rating = models.FloatField(validators=[validate_allowed_rating_value])

    def __str__(self):
        return self.name


ALLOWED_CONTACT_TYPE_VALUES = [
    ("Email", "Email"),
    ("Phone", "Phone"),
    ("Instagram", "Instagram"),
    ("Facebook", "Facebook"),
    ("Whatsapp", "Whatsapp")
]


class Contact(models.Model):
    homepage = models.ForeignKey(
        "HomePage", related_name="contact_us", on_delete=models.CASCADE
    )
    contact_name = models.CharField(
        max_length=100, choices=ALLOWED_CONTACT_TYPE_VALUES, unique=True
    )
    contact_value = models.CharField(max_length=100)

    def __str__(self):
        return self.contact_value


class HomePage(models.Model):

    def __str__(self):
        return "HomePage"
