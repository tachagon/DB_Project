# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('group4', '0002_auto_20150707_2219'),
    ]

    operations = [
        migrations.AddField(
            model_name='withdrawstudy',
            name='pricechild1',
            field=models.FloatField(default=0.0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='withdrawstudy',
            name='pricechild2',
            field=models.FloatField(default=0.0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='withdrawstudy',
            name='pricechild3',
            field=models.FloatField(default=0.0),
            preserve_default=True,
        ),
    ]
