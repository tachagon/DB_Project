# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('group6', '0006_categoriesproject_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoriesproject',
            name='project_catagories',
            field=models.CharField(default=datetime.datetime(2015, 7, 6, 8, 37, 44, 852840, tzinfo=utc), max_length=5),
            preserve_default=False,
        ),
    ]
