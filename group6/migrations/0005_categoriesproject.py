# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_auto_20150702_1652'),
        ('group6', '0004_stepintimeline_numberofprocess'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriesProject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('project_catagories', models.CharField(max_length=5, null=True)),
                ('project', models.ForeignKey(to='group6.ProjectG6')),
                ('teacher', models.ManyToManyField(to='login.Teacher')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
