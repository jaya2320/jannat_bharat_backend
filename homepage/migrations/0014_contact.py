# Generated by Django 5.0.7 on 2024-08-12 08:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0013_delete_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(choices=[('Email', 'Email'), ('Phone', 'Phone'), ('Instagram', 'Instagram'), ('Facebook', 'Facebook')], max_length=100)),
                ('contact_value', models.CharField(max_length=100)),
                ('homepage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contact_us', to='homepage.homepage')),
            ],
        ),
    ]
