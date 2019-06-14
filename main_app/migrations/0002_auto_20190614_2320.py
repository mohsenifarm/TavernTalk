# Generated by Django 2.2.2 on 2019-06-14 23:20

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateField(default=datetime.datetime(2019, 6, 14, 23, 20, 56, 302205), verbose_name='Date')),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Proflie_photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=300)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Date')),
                ('location', models.CharField(max_length=200)),
                ('note', models.TextField(max_length=500)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Game')),
            ],
        ),
        migrations.CreateModel(
            name='Game_photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=300)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Game')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=150)),
                ('date', models.DateField(default=datetime.datetime(2019, 6, 14, 23, 20, 56, 304308), verbose_name='Date')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Game')),
            ],
        ),
        migrations.CreateModel(
            name='Character_sheet_photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=300)),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Character')),
            ],
        ),
        migrations.CreateModel(
            name='Character_photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=300)),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Character')),
            ],
        ),
        migrations.AddField(
            model_name='character',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Game'),
        ),
    ]