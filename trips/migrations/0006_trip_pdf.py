# Generated by Django 5.0.7 on 2024-08-08 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0005_alter_trip_policy_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
