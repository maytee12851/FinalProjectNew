# Generated by Django 3.0 on 2022-04-13 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0052_auto_20220412_0158'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='userRating',
            field=models.DecimalField(blank=True, decimal_places=1, default=0, max_digits=5, null=True),
        ),
    ]
