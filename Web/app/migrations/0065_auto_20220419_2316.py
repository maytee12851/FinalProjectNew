# Generated by Django 3.0 on 2022-04-19 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0064_auto_20220419_2315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, default='profilePic/avatarPic.jpg', null=True, upload_to='profilePic/'),
        ),
    ]