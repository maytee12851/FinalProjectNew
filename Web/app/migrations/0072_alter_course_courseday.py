# Generated by Django 3.2.8 on 2022-04-23 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0071_auto_20220422_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='courseDay',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
