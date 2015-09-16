# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('group7', '0018_auto_20150708_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderinfo',
            name='Cost',
            field=models.FloatField(),
            preserve_default=True,
        ),
    ]
