# Generated by Django 5.0.7 on 2024-08-11 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0013_delete_about_alter_trip_banner_image_alter_trip_pdf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='duration',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
