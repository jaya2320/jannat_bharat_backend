# Generated by Django 5.0.7 on 2024-08-08 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0010_alter_trip_inquiry_form'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to='uploads/', verbose_name='PDF'),
        ),
    ]
