# Generated by Django 3.0 on 2022-03-21 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20220321_2014'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profileeducationtutor',
            old_name='user',
            new_name='username',
        ),
    ]
