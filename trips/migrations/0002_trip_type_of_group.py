# Generated by Django 5.0.7 on 2024-07-24 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='type_of_group',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
