# Generated by Django 3.0 on 2022-04-11 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0051_rating_courseid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='courseId',
        ),
        migrations.AddField(
            model_name='rating',
            name='MycourseId',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.MyCourseStudent'),
        ),
    ]