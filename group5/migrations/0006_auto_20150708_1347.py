# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('group5', '0005_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='Date',
            fields=[
                ('studentID', models.CharField(max_length=13, serialize=False, primary_key=True)),
                ('DateEnd', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='accept',
            name='StatusPetition',
        ),
        migrations.DeleteModel(
            name='accept',
        ),
    ]
