# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('group6', '0007_auto_20150706_1537'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoriesproject',
            name='semester',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='categoriesproject',
            name='year',
            field=models.CharField(default=datetime.datetime(2015, 7, 6, 16, 4, 45, 307308, tzinfo=utc), max_length=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='categoriesproject',
            name='number',
            field=models.CharField(max_length=2),
            preserve_default=True,
        ),
    ]
