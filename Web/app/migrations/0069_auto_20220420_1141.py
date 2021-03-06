# Generated by Django 3.0 on 2022-04-20 04:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0068_auto_20220420_0056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileeducationtutor',
            name='degree',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='profileeducationtutor',
            name='faculty',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='profileeducationtutor',
            name='major',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='profileeducationtutor',
            name='school',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='profileeducationtutor',
            name='schoolProgram',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='profileeducationtutor',
            name='schoolYear',
            field=models.CharField(blank=True, max_length=4),
        ),
        migrations.AlterField(
            model_name='profileeducationtutor',
            name='university',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='profileeducationtutor',
            name='universityYear',
            field=models.CharField(blank=True, max_length=4),
        ),
        migrations.AlterField(
            model_name='profileeducationtutor',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='app.Profile'),
        ),
    ]
