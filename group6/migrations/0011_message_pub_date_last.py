# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('group6', '0010_auto_20150710_1709'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='pub_date_last',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 10, 19, 19, 2, 429580, tzinfo=utc), verbose_name=b'last edit'),
            preserve_default=False,
        ),
    ]
