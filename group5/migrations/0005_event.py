# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('group5', '0004_remove_studentg5_sex'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('NoEvent', models.IntegerField(default=0, serialize=False, primary_key=True)),
                ('stuID', models.CharField(max_length=13)),
                ('Event', models.IntegerField(default=0)),
                ('Date_now', models.DateField()),
                ('Date_acc', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
