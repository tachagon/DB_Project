# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('group4', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='withdrawcure',
            name='typeWithdraw',
        ),
        migrations.AddField(
            model_name='withdrawcure',
            name='childW1',
            field=models.CharField(default=b'', max_length=1),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='withdrawcure',
            name='childW2',
            field=models.CharField(default=b'', max_length=1),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='withdrawcure',
            name='fatherW',
            field=models.CharField(default=b'', max_length=1),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='withdrawcure',
            name='motherW',
            field=models.CharField(default=b'', max_length=1),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='withdrawcure',
            name='selfW',
            field=models.CharField(default=b'', max_length=1),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='withdrawcure',
            name='spouseW',
            field=models.CharField(default=b'', max_length=1),
            preserve_default=True,
        ),
    ]
