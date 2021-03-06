# Generated by Django 3.0 on 2022-04-19 14:55

import cloudinary_storage.storage
import cloudinary_storage.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0062_auto_20220419_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yourselftutor',
            name='video',
            field=models.FileField(blank=True, default='#.mp4', null=True, storage=cloudinary_storage.storage.VideoMediaCloudinaryStorage(), upload_to='Video/', validators=[cloudinary_storage.validators.validate_video]),
        ),
    ]
