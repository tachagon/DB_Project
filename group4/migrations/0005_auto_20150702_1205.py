# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('group4', '0004_withdraw_datecommit'),
    ]

    operations = [
        migrations.CreateModel(
            name='Olddate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='datafromweb',
            name='date',
            field=models.CharField(max_length=255),
            preserve_default=True,
        ),
    ]
