# Generated by Django 3.0 on 2022-04-11 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0049_auto_20220411_1229'),
    ]

    operations = [
        migrations.AddField(
            model_name='mycoursestudent',
            name='star',
            field=models.BooleanField(default=False),
        ),
    ]
