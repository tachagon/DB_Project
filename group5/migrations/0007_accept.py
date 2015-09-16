# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('group5', '0006_auto_20150708_1347'),
    ]

    operations = [
        migrations.CreateModel(
            name='accept',
            fields=[
                ('No_accept', models.IntegerField(default=0, serialize=False, primary_key=True)),
                ('accept_status', models.CharField(max_length=20)),
                ('Date', models.DateField()),
                ('StatusPetition', models.ForeignKey(to='group5.StatusPetition')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
