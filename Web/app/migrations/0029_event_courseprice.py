# Generated by Django 3.0 on 2022-03-30 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0028_event_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='coursePrice',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
