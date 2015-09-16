# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('group3', '0004_auto_20150709_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prof2lang',
            name='prefix_name',
            field=models.CharField(max_length=1, choices=[(b'0', b'\xe0\xb8\x99\xe0\xb8\xb2\xe0\xb8\xa2'), (b'1', b'\xe0\xb8\x99\xe0\xb8\xb2\xe0\xb8\x87'), (b'2', b'\xe0\xb8\x99\xe0\xb8\xb2\xe0\xb8\x87\xe0\xb8\xaa\xe0\xb8\xb2\xe0\xb8\xa7'), (b'3', b'\xe0\xb8\x94\xe0\xb8\xa3.'), (b'4', b'\xe0\xb8\xad\xe0\xb8\xb2\xe0\xb8\x88\xe0\xb8\xb2\xe0\xb8\xa3\xe0\xb8\xa2\xe0\xb9\x8c')]),
            preserve_default=True,
        ),
    ]
