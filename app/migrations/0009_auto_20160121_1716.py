# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-21 10:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20160121_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='bill_created',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 21, 10, 16, 50, 765320, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='hostprofile',
            name='host_create_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 21, 10, 16, 50, 765320, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='hostprofile',
            name='host_porn',
            field=models.CharField(max_length=30),
        ),
    ]
