# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('group7', '0016_auto_20150703_0137'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requisition',
            name='Date',
        ),
        migrations.RemoveField(
            model_name='requisition',
            name='Moreabout',
        ),
        migrations.AlterField(
            model_name='requisition',
            name='Status_of',
            field=models.ForeignKey(to='group7.Order'),
            preserve_default=True,
        ),
    ]
