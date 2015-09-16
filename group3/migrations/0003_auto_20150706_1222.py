# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('group3', '0002_work_day'),
    ]

    operations = [
        migrations.AddField(
            model_name='prof2lang',
            name='academic_position',
            field=models.CharField(default=django.utils.timezone.now, max_length=1, choices=[(b'0', b''), (b'1', b'\xe0\xb8\x9c\xe0\xb8\xb9\xe0\xb9\x89\xe0\xb8\x8a\xe0\xb9\x88\xe0\xb8\xa7\xe0\xb8\xa2\xe0\xb8\xa8\xe0\xb8\xb2\xe0\xb8\xaa\xe0\xb8\x95\xe0\xb8\xa3\xe0\xb8\xb2\xe0\xb8\x88\xe0\xb8\xb2\xe0\xb8\xa3\xe0\xb8\xa2\xe0\xb9\x8c'), (b'2', b'\xe0\xb8\xa3\xe0\xb8\xad\xe0\xb8\x87\xe0\xb8\xa8\xe0\xb8\xb2\xe0\xb8\xaa\xe0\xb8\x95\xe0\xb8\xa3\xe0\xb8\xb2\xe0\xb8\x88\xe0\xb8\xb2\xe0\xb8\xa3\xe0\xb8\xa2\xe0\xb9\x8c'), (b'3', b'\xe0\xb8\xa8\xe0\xb8\xb2\xe0\xb8\xaa\xe0\xb8\x95\xe0\xb8\xa3\xe0\xb8\xb2\xe0\xb8\x88\xe0\xb8\xb2\xe0\xb8\xa3\xe0\xb8\xa2\xe0\xb9\x8c')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='prof2lang',
            name='prefix_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=1, choices=[(b'0', b'\xe0\xb8\x99\xe0\xb8\xb2\xe0\xb8\xa2'), (b'1', b'\xe0\xb8\x99\xe0\xb8\xb2\xe0\xb8\x87'), (b'2', b'\xe0\xb8\x99\xe0\xb8\xb2\xe0\xb8\x87\xe0\xb8\xaa\xe0\xb8\xb2\xe0\xb8\xa7'), (b'3', b'\xe0\xb8\x94\xe0\xb8\xa3.')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='prof2lang',
            name='type',
            field=models.CharField(default=django.utils.timezone.now, max_length=1, choices=[(b'0', b'\xe0\xb8\xad\xe0\xb8\xb2\xe0\xb8\x88\xe0\xb8\xb2\xe0\xb8\xa3\xe0\xb8\xa2\xe0\xb9\x8c\xe0\xb9\x83\xe0\xb8\x99\xe0\xb8\xa0\xe0\xb8\xb2\xe0\xb8\x84\xe0\xb8\xa7\xe0\xb8\xb4\xe0\xb8\x8a\xe0\xb8\xb2'), (b'1', b'\xe0\xb8\xad\xe0\xb8\xb2\xe0\xb8\x88\xe0\xb8\xb2\xe0\xb8\xa3\xe0\xb8\xa2\xe0\xb9\x8c\xe0\xb8\x99\xe0\xb8\xad\xe0\xb8\x81\xe0\xb8\xa0\xe0\xb8\xb2\xe0\xb8\x84\xe0\xb8\xa7\xe0\xb8\xb4\xe0\xb8\x8a\xe0\xb8\xb2'), (b'2', b'\xe0\xb8\xad\xe0\xb8\xb2\xe0\xb8\x88\xe0\xb8\xb2\xe0\xb8\xa3\xe0\xb8\xa2\xe0\xb9\x8c\xe0\xb8\x9e\xe0\xb8\xb4\xe0\xb9\x80\xe0\xb8\xa8\xe0\xb8\xa9')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='prof2lang',
            name='department',
            field=models.CharField(default=b'', max_length=200, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='prof2lang',
            name='faculty',
            field=models.CharField(default=b'', max_length=200, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='prof2lang',
            name='sahakornAccount',
            field=models.CharField(default=True, max_length=100, blank=True),
            preserve_default=True,
        ),
    ]
