# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('group5', '0003_auto_20150708_0029'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentg5',
            name='sex',
        ),
    ]
