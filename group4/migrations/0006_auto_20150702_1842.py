# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('group4', '0005_auto_20150702_1205'),
    ]

    operations = [
        migrations.RenameField(
            model_name='withdraw',
            old_name='stopData',
            new_name='stopDate',
        ),
        migrations.AlterField(
            model_name='child',
            name='family',
            field=models.ForeignKey(to='group4.Family'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='datafromweb',
            name='user',
            field=models.ForeignKey(to='login.UserProfile'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='withdraw',
            name='typeWithdraw',
            field=models.CharField(max_length=1, choices=[(b'0', b'\xe0\xb8\x95\xe0\xb8\x99\xe0\xb9\x80\xe0\xb8\xad\xe0\xb8\x87'), (b'1', b'\xe0\xb8\x9e\xe0\xb9\x88\xe0\xb8\xad'), (b'2', b'\xe0\xb9\x81\xe0\xb8\xa1\xe0\xb9\x88'), (b'3', b'\xe0\xb8\x84\xe0\xb8\xb9\xe0\xb9\x88\xe0\xb8\xaa\xe0\xb8\xa1\xe0\xb8\xa3\xe0\xb8\xaa'), (b'4', b'\xe0\xb8\xa5\xe0\xb8\xb9\xe0\xb8\x81')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='withdraw',
            name='user',
            field=models.ForeignKey(to='login.UserProfile'),
            preserve_default=True,
        ),
    ]
