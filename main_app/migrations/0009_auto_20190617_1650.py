# Generated by Django 2.2 on 2019-06-17 16:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_auto_20190617_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 6, 17, 16, 50, 3, 776832), verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 6, 17, 16, 50, 3, 777752), verbose_name='Date'),
        ),
    ]
