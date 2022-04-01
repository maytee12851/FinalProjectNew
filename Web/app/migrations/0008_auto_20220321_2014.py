# Generated by Django 3.0 on 2022-03-21 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_profile_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='nickname',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, default='profilePic/avatarPic.jpg', null=True, upload_to='profilePic/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='sex',
            field=models.CharField(choices=[('ชาย', 'ชาย'), ('หญิง', 'หญิง'), ('เพศทางเลือก', 'เพศทางเลือก')], max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='surname',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='tel',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='profile',
            name='userType',
            field=models.CharField(choices=[('student', 'Student'), ('teacher', 'Teacher'), ('admin', 'Admin')], max_length=100),
        ),
        migrations.CreateModel(
            name='ProfileEducationTutor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(max_length=100)),
                ('schoolProgram', models.CharField(max_length=100)),
                ('schoolYear', models.CharField(max_length=4)),
                ('university', models.CharField(max_length=100)),
                ('degree', models.CharField(max_length=100)),
                ('faculty', models.CharField(max_length=100)),
                ('major', models.CharField(max_length=100)),
                ('universityYear', models.CharField(max_length=4)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Profile')),
            ],
        ),
    ]