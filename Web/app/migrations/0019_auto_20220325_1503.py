# Generated by Django 3.0 on 2022-03-25 08:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_auto_20220324_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yourselftutor',
            name='introduce',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='yourselftutor',
            name='video',
            field=models.FileField(blank=True, default='#.mp4', null=True, upload_to='Video/'),
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(choices=[('ภาษาอังกฤษ', 'ภาษาอังกฤษ'), ('ภาษาเกาหลี', 'ภาษาเกาหลี'), ('ภาษาจีน', 'ภาษาจีน'), ('ภาษาญี่ปุ่น', 'ภาษาญี่ปุ่น'), ('ภาษาเยอรมัน', 'ภาษาเยอรมัน')], max_length=100)),
                ('courseTitle', models.CharField(max_length=100)),
                ('courseDesc', models.TextField()),
                ('courseTime', models.CharField(blank=True, max_length=2, null=True)),
                ('coursePrice', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Profile')),
            ],
        ),
    ]
