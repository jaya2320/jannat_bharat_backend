# Generated by Django 5.0.7 on 2024-08-10 22:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_remove_homepage_about_us_about_homepage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='homepage',
        ),
        migrations.AddField(
            model_name='homepage',
            name='about_us',
            field=models.OneToOneField(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='homepage', to='homepage.about'),
            preserve_default=False,
        ),
    ]
