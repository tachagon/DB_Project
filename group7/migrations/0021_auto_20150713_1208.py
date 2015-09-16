# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('group7', '0020_auto_20150713_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderinfo',
            name='Amount',
            field=models.IntegerField(),
            preserve_default=True,
        ),
    ]
