from django.db import models
from ckeditor.fields import RichTextField


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


class Review(models.Model):
    homepage = models.ForeignKey(
        "HomePage", related_name="reviews", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)
    review = RichTextField()

    def __str__(self):
        return self.name


class HomePage(models.Model):

    def __str__(self):
        return "HomePage"
