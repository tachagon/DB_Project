# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('group3', '0002_auto_20150414_0105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teach',
            name='prof',
            field=models.ForeignKey(blank=True, to='group3.Prof2Lang', null=True),
            preserve_default=True,
        ),
    ]
