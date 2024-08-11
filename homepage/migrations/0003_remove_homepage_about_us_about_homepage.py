# Generated by Django 5.0.7 on 2024-08-10 22:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_homepage_galleryimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='about_us',
        ),
        migrations.AddField(
            model_name='about',
            name='homepage',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='about_us', to='homepage.homepage'),
            preserve_default=False,
        ),
    ]
