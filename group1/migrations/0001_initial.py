# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0008_auto_20150709_1431'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('dept', models.CharField(max_length=200)),
                ('year', models.CharField(max_length=4)),
                ('number', models.CharField(max_length=10)),
                ('number2', models.CharField(max_length=10)),
                ('detail1', models.CharField(max_length=50)),
                ('detail2', models.CharField(max_length=50)),
                ('detail3', models.CharField(max_length=50)),
                ('detail4', models.CharField(max_length=50)),
                ('docfile', models.FileField(upload_to=b'documents/%Y')),
                ('added', models.CharField(max_length=50)),
                ('addby', models.CharField(max_length=50)),
                ('send_status', models.BooleanField(default=0)),
                ('category', models.ForeignKey(to='group1.Category')),
                ('userProfile', models.ManyToManyField(to='login.UserProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Document_modify',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('modified', models.CharField(max_length=50)),
                ('modifyby', models.CharField(max_length=50)),
                ('document', models.ForeignKey(to='group1.Document')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
