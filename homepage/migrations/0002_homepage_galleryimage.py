# Generated by Django 5.0.7 on 2024-08-10 22:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_us', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='homepage', to='homepage.about')),
            ],
        ),
        migrations.CreateModel(
            name='GalleryImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='homepage/gallery_images/')),
                ('caption', models.CharField(blank=True, max_length=255)),
                ('homepage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery_images', to='homepage.homepage')),
            ],
        ),
    ]
