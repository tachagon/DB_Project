# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20150621_1618'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApproveProjectForm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('course', models.CharField(max_length=200)),
                ('semesterEnd', models.CharField(max_length=200)),
                ('yearEnd', models.CharField(max_length=200)),
                ('credit', models.IntegerField(default=3)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OfferProjectForm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('priceOfMaterial', models.FloatField(default=0.0)),
                ('priceOfOther', models.FloatField(default=0.0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectG6',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_thai', models.CharField(max_length=200)),
                ('name_eng', models.CharField(max_length=200)),
                ('yearOfEducation', models.IntegerField(default=1)),
                ('objective', models.TextField()),
                ('reason', models.TextField()),
                ('scope', models.TextField()),
                ('benefit', models.TextField()),
                ('student', models.ManyToManyField(to='login.Student')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ResearchProjectForm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numberOfPeople', models.IntegerField(default=1)),
                ('project', models.ForeignKey(to='group6.ProjectG6')),
                ('teacher', models.ForeignKey(to='login.Teacher')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='offerprojectform',
            name='project',
            field=models.ForeignKey(to='group6.ProjectG6'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='offerprojectform',
            name='teacher',
            field=models.ForeignKey(to='login.Teacher'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='approveprojectform',
            name='project',
            field=models.ForeignKey(to='group6.ProjectG6'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='approveprojectform',
            name='student',
            field=models.ForeignKey(to='login.Student'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='approveprojectform',
            name='teacher',
            field=models.ForeignKey(to='login.Teacher'),
            preserve_default=True,
        ),
    ]
