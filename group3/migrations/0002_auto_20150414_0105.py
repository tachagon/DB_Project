# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('group3', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teach',
            name='prof',
            field=models.ForeignKey(to='group3.Prof2Lang', blank=True),
            preserve_default=True,
        ),
    ]
