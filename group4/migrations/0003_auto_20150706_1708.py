# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('group4', '0002_auto_20150706_1248'),
    ]

    operations = [
        migrations.AddField(
            model_name='withdrawcure',
            name='orderchildW1',
            field=models.CharField(default=b'', max_length=1),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='withdrawcure',
            name='orderchildW2',
            field=models.CharField(default=b'', max_length=1),
            preserve_default=True,
        ),
    ]
