# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-04 21:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_news_download_time'),
    ]

    operations = [
        migrations.RunSQL(
            "alter table app_news alter column download_time set default current_timestamp"
        ),
    ]