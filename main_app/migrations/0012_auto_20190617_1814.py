# Generated by Django 2.2.2 on 2019-06-17 18:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_auto_20190617_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 6, 17, 18, 14, 18, 994886), verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateField(verbose_name='Date'),
        ),
    ]