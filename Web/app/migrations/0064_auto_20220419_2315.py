# Generated by Django 3.0 on 2022-04-19 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0063_auto_20220419_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='idcard',
            field=models.ImageField(blank=True, default='idCard/idcard.jpg', null=True, upload_to='idCard/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, default='https://res.cloudinary.com/hbciv0xpi/image/upload/v1650380834/media/profilePic/avatarPic_pekm5b.jpg', null=True, upload_to='profilePic/'),
        ),
    ]