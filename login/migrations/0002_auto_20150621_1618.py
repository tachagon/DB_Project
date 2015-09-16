# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Officer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('position', models.CharField(max_length=100)),
                ('userprofile', models.OneToOneField(to='login.UserProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('std_id', models.CharField(max_length=13)),
                ('scheme', models.CharField(max_length=1, choices=[(b'0', b'\xe0\xb8\xab\xe0\xb8\xa5\xe0\xb8\xb1\xe0\xb8\x81\xe0\xb8\xaa\xe0\xb8\xb9\xe0\xb8\x95\xe0\xb8\xa3\xe0\xb8\x9b\xe0\xb8\xa3\xe0\xb8\xb1\xe0\xb8\x9a\xe0\xb8\x9b\xe0\xb8\xa3\xe0\xb8\xb8\xe0\xb8\x87 Cpr.E 54'), (b'1', b'\xe0\xb8\xab\xe0\xb8\xa5\xe0\xb8\xb1\xe0\xb8\x81\xe0\xb8\xaa\xe0\xb8\xb9\xe0\xb8\x95\xe0\xb8\xa3\xe0\xb8\x9b\xe0\xb8\xa3\xe0\xb8\xb1\xe0\xb8\x9a\xe0\xb8\x9b\xe0\xb8\xa3\xe0\xb8\xb8\xe0\xb8\x87 EE 51'), (b'2', b'\xe0\xb8\xab\xe0\xb8\xa5\xe0\xb8\xb1\xe0\xb8\x81\xe0\xb8\xaa\xe0\xb8\xb9\xe0\xb8\x95\xe0\xb8\xa3\xe0\xb8\x9b\xe0\xb8\xa3\xe0\xb8\xb1\xe0\xb8\x9a\xe0\xb8\x9b\xe0\xb8\xa3\xe0\xb8\xb8\xe0\xb8\x87 ECE 55')])),
                ('main', models.CharField(max_length=1, choices=[(b'0', b'Cpr.E'), (b'1', b'G'), (b'2', b'U'), (b'3', b'C')])),
                ('userprofile', models.OneToOneField(to='login.UserProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('shortname', models.CharField(max_length=3)),
                ('position', models.CharField(max_length=100)),
                ('userprofile', models.OneToOneField(to='login.UserProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='address',
            field=models.TextField(default=datetime.datetime(2015, 6, 21, 9, 17, 2, 830000, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='department',
            field=models.CharField(default=datetime.datetime(2015, 6, 21, 9, 17, 16, 721000, tzinfo=utc), max_length=1, choices=[(b'0', b''), (b'1', b'\xe0\xb8\xa7\xe0\xb8\xb4\xe0\xb8\xa8\xe0\xb8\xa7\xe0\xb8\x81\xe0\xb8\xa3\xe0\xb8\xa3\xe0\xb8\xa1\xe0\xb9\x84\xe0\xb8\x9f\xe0\xb8\x9f\xe0\xb9\x89\xe0\xb8\xb2\xe0\xb9\x81\xe0\xb8\xa5\xe0\xb8\xb0\xe0\xb8\x84\xe0\xb8\xad\xe0\xb8\xa1\xe0\xb8\x9e\xe0\xb8\xb4\xe0\xb8\xa7\xe0\xb9\x80\xe0\xb8\x95\xe0\xb8\xad\xe0\xb8\xa3\xe0\xb9\x8c')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='faculty',
            field=models.CharField(default=datetime.datetime(2015, 6, 21, 9, 17, 26, 924000, tzinfo=utc), max_length=1, choices=[(b'0', b''), (b'1', b'\xe0\xb8\xa7\xe0\xb8\xb4\xe0\xb8\xa8\xe0\xb8\xa7\xe0\xb8\x81\xe0\xb8\xa3\xe0\xb8\xa3\xe0\xb8\xa1\xe0\xb8\xa8\xe0\xb8\xb2\xe0\xb8\xaa\xe0\xb8\x95\xe0\xb8\xa3\xe0\xb9\x8c')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='firstname_en',
            field=models.CharField(default=datetime.datetime(2015, 6, 21, 9, 17, 37, 503000, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='firstname_th',
            field=models.CharField(default=datetime.datetime(2015, 6, 21, 9, 17, 54, 331000, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='lastname_en',
            field=models.CharField(default=datetime.datetime(2015, 6, 21, 9, 18, 2, 97000, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='lastname_th',
            field=models.CharField(default=datetime.datetime(2015, 6, 21, 9, 18, 5, 769000, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='office',
            field=models.TextField(default=datetime.datetime(2015, 6, 21, 9, 18, 7, 753000, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='tel',
            field=models.CharField(default=datetime.datetime(2015, 6, 21, 9, 18, 10, 316000, tzinfo=utc), max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='type',
            field=models.CharField(default=datetime.datetime(2015, 6, 21, 9, 18, 12, 644000, tzinfo=utc), max_length=1, choices=[(b'0', b'Student'), (b'1', b'Teacher'), (b'2', b'Officer')]),
            preserve_default=False,
        ),
    ]
