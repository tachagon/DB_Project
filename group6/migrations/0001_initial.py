# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
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
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StudentG6',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('student_id', models.CharField(max_length=13)),
                ('firstname_thai', models.CharField(max_length=200)),
                ('lastname_thai', models.CharField(max_length=200)),
                ('firstname_eng', models.CharField(max_length=200)),
                ('lastname_eng', models.CharField(max_length=200)),
                ('course', models.CharField(max_length=200)),
                ('department', models.CharField(max_length=200)),
                ('main', models.CharField(max_length=200)),
                ('year_admission', models.IntegerField(default=1)),
                ('address', models.TextField()),
                ('tel', models.CharField(max_length=200)),
                ('workplace', models.TextField()),
                ('field_name', models.OneToOneField(to='login.UserProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TeacherG6',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstname_thai', models.CharField(max_length=200)),
                ('lastname_thai', models.CharField(max_length=200)),
                ('firstname_eng', models.CharField(max_length=200)),
                ('lastname_eng', models.CharField(max_length=200)),
                ('symbol_name', models.CharField(max_length=3)),
                ('department', models.CharField(max_length=200)),
                ('address', models.TextField()),
                ('workplace', models.TextField()),
                ('tel', models.CharField(max_length=200)),
                ('tel_con', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='researchprojectform',
            name='teacher',
            field=models.ForeignKey(to='group6.TeacherG6'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='projectg6',
            name='student',
            field=models.ManyToManyField(to='group6.StudentG6'),
            preserve_default=True,
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
            field=models.ForeignKey(to='group6.TeacherG6'),
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
            field=models.ForeignKey(to='group6.StudentG6'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='approveprojectform',
            name='teacher',
            field=models.ForeignKey(to='group6.TeacherG6'),
            preserve_default=True,
        ),
    ]
