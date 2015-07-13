# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('group5', '0007_accept'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accept',
            name='StatusPetition',
        ),
        migrations.DeleteModel(
            name='accept',
        ),
        migrations.DeleteModel(
            name='Event',
        ),
        migrations.AddField(
            model_name='statuspetition',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='statuspetition',
            name='updated_at',
            field=models.DateTimeField(default=django.utils.timezone.now, auto_now=True),
            preserve_default=False,
        ),
    ]
