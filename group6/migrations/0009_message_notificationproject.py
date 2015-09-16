# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_auto_20150704_1334'),
        ('group6', '0008_auto_20150706_2304'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField()),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
                ('user', models.ForeignKey(to='login.UserProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NotificationProject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.ManyToManyField(to='group6.Message')),
                ('project', models.ForeignKey(to='group6.ProjectG6')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
