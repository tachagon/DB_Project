# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('group4', '0002_auto_20150624_1850'),
    ]

    operations = [
        migrations.AddField(
            model_name='family',
            name='typeFamily',
            field=models.CharField(default=django.utils.timezone.now, max_length=1, choices=[(b'1', b'\xe0\xb8\x9e\xe0\xb9\x88\xe0\xb8\xad\xe0\xb9\x88'), (b'2', b'\xe0\xb9\x81\xe0\xb8\xa1\xe0\xb9\x88'), (b'3', b'\xe0\xb8\x84\xe0\xb8\xb9\xe0\xb9\x88\xe0\xb8\xaa\xe0\xb8\xa1\xe0\xb8\xa3\xe0\xb8\xaa'), (b'4', b'\xe0\xb8\xa5\xe0\xb8\xb9\xe0\xb8\x81')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='family',
            name='user',
            field=models.ForeignKey(to='login.UserProfile'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='withdraw',
            name='hospitalOf',
            field=models.CharField(max_length=1, choices=[(b'0', b'\xe0\xb8\x82\xe0\xb8\xad\xe0\xb8\x87\xe0\xb8\x97\xe0\xb8\xb2\xe0\xb8\x87\xe0\xb8\xa3\xe0\xb8\xb2\xe0\xb8\x8a\xe0\xb8\x81\xe0\xb8\xb2\xe0\xb8\xa3'), (b'1', b'\xe0\xb9\x80\xe0\xb8\xad\xe0\xb8\x81\xe0\xb8\x8a\xe0\xb8\x99')]),
            preserve_default=True,
        ),
    ]
