# Generated by Django 3.2.8 on 2022-04-23 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0073_auto_20220424_0001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(max_length=900),
        ),
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='yourselftutor',
            name='facebook',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='yourselftutor',
            name='line',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
