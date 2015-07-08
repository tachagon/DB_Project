# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('group2', '0002_auto_20150708_0051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='Grade',
            field=models.CharField(default=b'0', max_length=3, choices=[(b'0', b' '), (b'1', b'A'), (b'2', b'B+'), (b'3', b'B'), (b'4', b'C+'), (b'5', b'C'), (b'6', b'D+'), (b'7', b'D'), (b'8', b'F'), (b'9', b'Fa'), (b'10', b'Fe'), (b'11', b'S'), (b'12', b'U'), (b'13', b'I'), (b'14', b'Ip'), (b'15', b'W'), (b'16', b'AUD')]),
            preserve_default=True,
        ),
    ]
