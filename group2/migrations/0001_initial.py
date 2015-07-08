# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_auto_20150704_1334'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('Course_ID', models.IntegerField(max_length=10, serialize=False, primary_key=True)),
                ('Course_Name', models.CharField(max_length=100)),
                ('Credit', models.CharField(max_length=10)),
                ('Describe', models.CharField(max_length=1000, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('Department_ID', models.IntegerField(max_length=10, serialize=False, primary_key=True)),
                ('Department_Name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.IntegerField(max_length=10)),
                ('term', models.IntegerField(max_length=1)),
                ('Grade', models.CharField(default=b'0', max_length=3, choices=[(b'0', b' '), (b'1', b'A'), (b'2', b'B+'), (b'3', b'B'), (b'4', b'C+'), (b'5', b'B'), (b'6', b'D+'), (b'7', b'D'), (b'8', b'F'), (b'9', b'Fa'), (b'11', b'Fe'), (b'12', b'S'), (b'13', b'U'), (b'14', b'I'), (b'15', b'Ip'), (b'16', b'W'), (b'17', b'AUD')])),
                ('Course_ID', models.ForeignKey(to='group2.Course')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='scheme',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('scheme', models.CharField(max_length=1, choices=[(b'0', b'\xe0\xb9\x84\xe0\xb8\xa1\xe0\xb9\x88\xe0\xb8\xa1\xe0\xb8\xb5\xe0\xb9\x83\xe0\xb8\x99\xe0\xb8\xab\xe0\xb8\xa5\xe0\xb8\xb1\xe0\xb8\x81\xe0\xb8\xaa\xe0\xb8\xb9\xe0\xb8\x95\xe0\xb8\xa3'), (b'1', b'\xe0\xb8\x9b\xe0\xb8\xa3\xe0\xb8\xb4\xe0\xb8\x8d\xe0\xb8\x8d\xe0\xb8\xb2\xe0\xb9\x82\xe0\xb8\x97_\xe0\xb8\xab\xe0\xb8\xa5\xe0\xb8\xb1\xe0\xb8\x81\xe0\xb8\xaa\xe0\xb8\xb9\xe0\xb8\x95\xe0\xb8\xa32\xe0\xb8\x9b\xe0\xb8\xb5_\xe0\xb9\x81\xe0\xb8\x9c\xe0\xb8\x99_\xe0\xb8\x81_\xe0\xb9\x80\xe0\xb9\x80\xe0\xb8\x9a\xe0\xb8\x9a_\xe0\xb8\x81_2_\xe0\xb8\x9b\xe0\xb8\x81\xe0\xb8\x95\xe0\xb8\xb4'), (b'2', b'\xe0\xb8\x9b\xe0\xb8\xa3\xe0\xb8\xb4\xe0\xb8\x8d\xe0\xb8\x8d\xe0\xb8\xb2\xe0\xb9\x82\xe0\xb8\x97_\xe0\xb8\xab\xe0\xb8\xa5\xe0\xb8\xb1\xe0\xb8\x81\xe0\xb8\xaa\xe0\xb8\xb9\xe0\xb8\x95\xe0\xb8\xa32\xe0\xb8\x9b\xe0\xb8\xb5_\xe0\xb9\x81\xe0\xb8\x9c\xe0\xb8\x99_\xe0\xb8\x81_\xe0\xb9\x80\xe0\xb9\x80\xe0\xb8\x9a\xe0\xb8\x9a_\xe0\xb8\x81_2_\xe0\xb8\xaa\xe0\xb8\xab\xe0\xb8\x81\xe0\xb8\xb4\xe0\xb8\x88\xe0\xb8\xa8\xe0\xb8\xb6\xe0\xb8\x81\xe0\xb8\xa9\xe0\xb8\xb2'), (b'3', b'\xe0\xb8\x9b\xe0\xb8\xa3\xe0\xb8\xb4\xe0\xb8\x8d\xe0\xb8\x8d\xe0\xb8\xb2\xe0\xb9\x80\xe0\xb8\xad\xe0\xb8\x81_\xe0\xb8\xab\xe0\xb8\xa5\xe0\xb8\xb1\xe0\xb8\x81\xe0\xb8\xaa\xe0\xb8\xb9\xe0\xb8\x95\xe0\xb8\xa33\xe0\xb8\x9b\xe0\xb8\xb5_\xe0\xb9\x81\xe0\xb8\x9a\xe0\xb8\x9a_1.1'), (b'4', b'\xe0\xb8\x9b\xe0\xb8\xa3\xe0\xb8\xb4\xe0\xb8\x8d\xe0\xb8\x8d\xe0\xb8\xb2\xe0\xb9\x80\xe0\xb8\xad\xe0\xb8\x81_\xe0\xb8\xab\xe0\xb8\xa5\xe0\xb8\xb1\xe0\xb8\x81\xe0\xb8\xaa\xe0\xb8\xb9\xe0\xb8\x95\xe0\xb8\xa33\xe0\xb8\x9b\xe0\xb8\xb5_\xe0\xb9\x81\xe0\xb8\x9a\xe0\xb8\x9a_2.1'), (b'5', b'\xe0\xb8\x9b\xe0\xb8\xa3\xe0\xb8\xb4\xe0\xb8\x8d\xe0\xb8\x8d\xe0\xb8\xb2\xe0\xb9\x80\xe0\xb8\xad\xe0\xb8\x81_\xe0\xb8\xab\xe0\xb8\xa5\xe0\xb8\xb1\xe0\xb8\x81\xe0\xb8\xaa\xe0\xb8\xb9\xe0\xb8\x95\xe0\xb8\xa34\xe0\xb8\x9b\xe0\xb8\xb5_\xe0\xb9\x81\xe0\xb8\x9a\xe0\xb8\x9a_1.2'), (b'6', b'\xe0\xb8\x9b\xe0\xb8\xa3\xe0\xb8\xb4\xe0\xb8\x8d\xe0\xb8\x8d\xe0\xb8\xb2\xe0\xb9\x80\xe0\xb8\xad\xe0\xb8\x81_\xe0\xb8\xab\xe0\xb8\xa5\xe0\xb8\xb1\xe0\xb8\x81\xe0\xb8\xaa\xe0\xb8\xb9\xe0\xb8\x95\xe0\xb8\xa34\xe0\xb8\x9b\xe0\xb8\xb5_\xe0\xb9\x81\xe0\xb8\x9a\xe0\xb8\x9a_2.2')])),
                ('Course_ID', models.ForeignKey(to='group2.Course')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Section', models.IntegerField(max_length=7)),
                ('classroom', models.CharField(max_length=20)),
                ('st_endTime', models.CharField(max_length=11)),
                ('date', models.CharField(max_length=1, choices=[(b'M', b'Monday'), (b'T', b'Tuesday'), (b'W', b'Wednesday'), (b'H', b'Thursday'), (b'F', b'Friday'), (b'S', b'Saturday')])),
                ('Course_ID', models.ForeignKey(to='group2.Course')),
                ('Teacher_ID', models.ForeignKey(to='login.Teacher')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Teacher_Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Course_ID', models.ForeignKey(to='group2.Course')),
                ('Section', models.ForeignKey(to='group2.Section')),
                ('shortname', models.ForeignKey(to='login.Teacher')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='viyanipon_adviser',
            fields=[
                ('std_id', models.CharField(max_length=13, serialize=False, primary_key=True)),
                ('teach_name', models.CharField(max_length=6)),
                ('adviser', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='viyanipon_name',
            fields=[
                ('std_id', models.CharField(max_length=13, serialize=False, primary_key=True)),
                ('viyaniponh_name', models.CharField(max_length=6)),
                ('name_thai', models.CharField(max_length=200)),
                ('name_eng', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='viyanipon_project',
            fields=[
                ('std_id', models.CharField(max_length=13, serialize=False, primary_key=True)),
                ('project_name', models.CharField(max_length=6)),
                ('name_day', models.IntegerField(max_length=2)),
                ('name_month', models.CharField(max_length=50)),
                ('name_year', models.IntegerField(max_length=4)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='viyanipon_test',
            fields=[
                ('std_id', models.CharField(max_length=13, serialize=False, primary_key=True)),
                ('test', models.CharField(max_length=6)),
                ('test_day', models.IntegerField(max_length=2)),
                ('test_month', models.CharField(max_length=50)),
                ('test_year', models.IntegerField(max_length=4)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='viyanipon_testend',
            fields=[
                ('std_id', models.CharField(max_length=13, serialize=False, primary_key=True)),
                ('testend', models.CharField(max_length=20)),
                ('testend_day', models.IntegerField(max_length=2)),
                ('testend_month', models.CharField(max_length=50)),
                ('testend_year', models.IntegerField(max_length=4)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='grade',
            name='Section',
            field=models.ForeignKey(to='group2.Section'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='grade',
            name='std_id',
            field=models.ForeignKey(to='login.Student'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='course',
            name='Department_ID',
            field=models.ForeignKey(to='group2.Department'),
            preserve_default=True,
        ),
    ]
