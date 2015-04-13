# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HourlyEmployee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=80)),
                ('numberTaxpayment', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=50)),
                ('employmentRate', models.FloatField(default=0.0, max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Prof2Lang',
            fields=[
                ('profID', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=80)),
                ('shortName', models.CharField(max_length=3)),
                ('tell', models.CharField(max_length=15, blank=True)),
                ('email', models.EmailField(max_length=75, blank=True)),
                ('sahakornAccount', models.CharField(max_length=100, blank=True)),
                ('department', models.CharField(max_length=200)),
                ('faculty', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('section', models.CharField(max_length=7)),
                ('classroom', models.CharField(max_length=20)),
                ('startTime', models.TimeField()),
                ('endTime', models.TimeField()),
                ('date', models.CharField(max_length=1, choices=[(b'M', b'Monday'), (b'T', b'Tuesday'), (b'W', b'Wednesday'), (b'H', b'Thursday'), (b'F', b'Friday'), (b'S', b'Saturday')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('subjectID', models.CharField(max_length=9, serialize=False, primary_key=True)),
                ('subjectName', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Teach',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('prof', models.ForeignKey(to='group3.Prof2Lang')),
                ('section', models.ForeignKey(to='group3.Section')),
                ('subject', models.ForeignKey(to='group3.Subject')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('releaseDate', models.DateField(auto_now=True)),
                ('startTime', models.TimeField()),
                ('endTime', models.TimeField()),
                ('employee', models.ForeignKey(to='group3.HourlyEmployee')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='section',
            name='subject',
            field=models.ForeignKey(to='group3.Subject'),
            preserve_default=True,
        ),
    ]
