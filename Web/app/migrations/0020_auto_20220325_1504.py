# Generated by Django 3.0 on 2022-03-25 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_auto_20220325_1503'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='courseTime',
            new_name='courseHours',
        ),
    ]