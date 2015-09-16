# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0009_auto_20150711_2123'),
        ('group2', '0006_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Viyanipon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Teacher', models.CharField(max_length=100, blank=True)),
                ('Offer_th', models.CharField(max_length=200, blank=True)),
                ('Offer_en', models.CharField(max_length=200, blank=True)),
                ('Test', models.CharField(max_length=20, blank=True)),
                ('Advance_Test', models.CharField(max_length=20, blank=True)),
                ('Protect_Test', models.CharField(max_length=20, blank=True)),
                ('std_id', models.ForeignKey(to='login.Student')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
