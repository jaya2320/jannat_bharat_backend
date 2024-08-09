from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from ckeditor.fields import RichTextField

class About(models.Model):
    about_content = RichTextField()

    def __str__(self):
        return f"About.v{self.id}"

# save About in About.v1 in version format
@receiver(pre_save, sender=About)
def auto_generate_name(sender, instance, **kwargs):
    if instance.pk is None:  # Only assign when the instance is first created
        last_about_version = About.objects.all().order_by('id').last()
        if last_about_version:
            new_id = last_about_version.id + 1
        else:
            new_id = 1
        instance.id = str(new_id)
