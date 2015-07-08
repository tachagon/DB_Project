# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('group2', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='Section',
            field=models.IntegerField(max_length=10),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='viyanipon_testend',
            name='testend',
            field=models.CharField(max_length=6),
            preserve_default=True,
        ),
    ]
