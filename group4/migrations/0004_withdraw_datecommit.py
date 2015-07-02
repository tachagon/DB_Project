# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('group4', '0003_auto_20150624_1915'),
    ]

    operations = [
        migrations.AddField(
            model_name='withdraw',
            name='dateCommit',
            field=models.DateTimeField(default=django.utils.timezone.now, auto_now=True),
            preserve_default=False,
        ),
    ]
