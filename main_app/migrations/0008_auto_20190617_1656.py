# Generated by Django 2.2 on 2019-06-17 16:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_auto_20190617_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 6, 17, 16, 56, 31, 95735), verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 6, 17, 16, 56, 31, 96544), verbose_name='Date'),
        ),
    ]
