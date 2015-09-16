# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('group5', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accept',
            name='StatusPetition',
        ),
        migrations.RemoveField(
            model_name='statuspetition',
            name='Internship',
        ),
        migrations.RemoveField(
            model_name='statuspetition',
            name='studentG5',
        ),
        migrations.DeleteModel(
            name='accept',
        ),
        migrations.DeleteModel(
            name='StatusPetition',
        ),
    ]
