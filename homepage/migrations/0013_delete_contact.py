# Generated by Django 5.0.7 on 2024-08-12 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0012_alter_contact_contact_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contact',
        ),
    ]
