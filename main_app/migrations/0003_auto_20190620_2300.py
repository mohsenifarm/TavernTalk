# Generated by Django 2.2 on 2019-06-20 23:00

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20190620_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 6, 20, 23, 0, 55, 491709), verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='profile_photo',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Profile'),
        ),
    ]
