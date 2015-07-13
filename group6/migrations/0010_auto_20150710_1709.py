# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_auto_20150704_1334'),
        ('group6', '0009_message_notificationproject'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notificationproject',
            name='message',
        ),
        migrations.AddField(
            model_name='message',
            name='noti',
            field=models.ForeignKey(to='group6.NotificationProject'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='notificationproject',
            name='officer',
            field=models.ForeignKey(to='login.Officer'),
            preserve_default=False,
        ),
    ]
