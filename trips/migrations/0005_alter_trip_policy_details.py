# Generated by Django 5.0.7 on 2024-08-06 17:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0004_remove_mustknow_otherimportantthingstoremember_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='policy_details',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='policies', to='trips.policies'),
        ),
    ]
