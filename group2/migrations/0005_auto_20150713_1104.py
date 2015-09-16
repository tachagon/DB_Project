# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('group2', '0004_auto_20150713_1021'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='viyanipon_name',
            name='viyaniponh_name',
        ),
        migrations.AddField(
            model_name='viyanipon_name',
            name='name',
            field=models.CharField(default=datetime.datetime(2015, 7, 13, 4, 4, 7, 374000, tzinfo=utc), max_length=20),
            preserve_default=False,
        ),
    ]
