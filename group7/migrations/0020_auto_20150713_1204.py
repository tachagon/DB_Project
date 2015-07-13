# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('group7', '0019_auto_20150713_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderinfo',
            name='Amount',
            field=models.FloatField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='Cost_total',
            field=models.FloatField(),
            preserve_default=True,
        ),
    ]
