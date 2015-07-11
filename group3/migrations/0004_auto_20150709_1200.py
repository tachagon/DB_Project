# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('group3', '0003_auto_20150706_1222'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='subjectName_th',
            field=models.CharField(default=b'', max_length=200),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='teach',
            name='term',
            field=models.CharField(default=b'', max_length=1, choices=[(b'', b'\xe0\xb8\x81\xe0\xb8\xa3\xe0\xb8\xb8\xe0\xb8\x93\xe0\xb8\xb2\xe0\xb9\x80\xe0\xb8\xa5\xe0\xb8\xb7\xe0\xb8\xad\xe0\xb8\x81\xe0\xb8\xa0\xe0\xb8\xb2\xe0\xb8\x84\xe0\xb9\x80\xe0\xb8\xa3\xe0\xb8\xb5\xe0\xb8\xa2\xe0\xb8\x99'), (b'1', b'1'), (b'2', b'2'), (b'3', b'3')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='teach',
            name='year',
            field=models.CharField(default=b'', max_length=4),
            preserve_default=True,
        ),
    ]
