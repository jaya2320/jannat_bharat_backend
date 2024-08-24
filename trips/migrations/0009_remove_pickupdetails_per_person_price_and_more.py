# Generated by Django 5.0.7 on 2024-08-08 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0008_alter_trip_pdf'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pickupdetails',
            name='per_person_price',
        ),
        migrations.AddField(
            model_name='policies',
            name='policy_name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
