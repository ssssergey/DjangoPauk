# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-05 19:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0008_auto_20160605_0023'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCountry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_time', models.DateTimeField()),
                ('checked', models.BooleanField(default=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Countries')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='news',
            name='download_time',
            field=models.DateTimeField(),
        ),
        migrations.AddField(
            model_name='countries',
            name='users',
            field=models.ManyToManyField(related_name='countries', through='app.UserCountry', to=settings.AUTH_USER_MODEL),
        ),
    ]
