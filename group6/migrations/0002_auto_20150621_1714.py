# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20150621_1618'),
        ('group6', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='approveprojectform',
            name='teacher',
        ),
        migrations.RemoveField(
            model_name='offerprojectform',
            name='teacher',
        ),
        migrations.RemoveField(
            model_name='researchprojectform',
            name='teacher',
        ),
        migrations.AddField(
            model_name='projectg6',
            name='teacher',
            field=models.ForeignKey(to='login.Teacher'),
            preserve_default=False,
        ),
    ]
