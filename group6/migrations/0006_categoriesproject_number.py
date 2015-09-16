# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('group6', '0005_categoriesproject'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoriesproject',
            name='number',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
    ]
