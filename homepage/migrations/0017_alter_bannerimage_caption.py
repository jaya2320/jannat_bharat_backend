# Generated by Django 5.0.7 on 2024-08-12 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0016_bannerimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bannerimage',
            name='caption',
            field=models.CharField(max_length=255),
        ),
    ]
