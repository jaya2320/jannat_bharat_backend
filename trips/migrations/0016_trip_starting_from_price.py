# Generated by Django 5.0.7 on 2024-08-12 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0015_alter_trip_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='starting_from_price',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=20),
        ),
    ]
