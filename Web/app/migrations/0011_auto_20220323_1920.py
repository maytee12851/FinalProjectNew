# Generated by Django 3.0 on 2022-03-23 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20220321_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileeducationtutor',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Profile'),
        ),
    ]