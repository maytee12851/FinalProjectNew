# Generated by Django 3.0 on 2022-04-19 12:22

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0060_auto_20220419_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yourselftutor',
            name='video',
            field=cloudinary.models.CloudinaryField(blank=True, default='#.mp4', max_length=255, null=True, verbose_name='video'),
        ),
    ]