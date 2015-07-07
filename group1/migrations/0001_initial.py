# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('code_name', models.IntegerField(serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('code_name', models.CharField(max_length=10, serialize=False, primary_key=True)),
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
                ('year', models.CharField(max_length=4)),
                ('number', models.CharField(max_length=10)),
                ('number2', models.CharField(max_length=10)),
                ('detail1', models.CharField(max_length=50)),
                ('detail2', models.CharField(max_length=50)),
                ('detail3', models.CharField(max_length=50)),
                ('detail4', models.CharField(max_length=50)),
                ('docfile', models.FileField(upload_to=b'static/documents/%Y')),
                ('category', models.ForeignKey(to='group1.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('code_name', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=50)),
                ('department', models.ForeignKey(to='group1.Department')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='document',
            name='personal',
            field=models.ManyToManyField(to='group1.Personal'),
            preserve_default=True,
        ),
    ]
