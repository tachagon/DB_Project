# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0009_auto_20150711_2123'),
        ('group2', '0003_auto_20150708_0332'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('state', models.CharField(max_length=40, blank=True)),
                ('std_id', models.ForeignKey(to='login.Student')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='course',
            name='Department_ID',
        ),
        migrations.RemoveField(
            model_name='course',
            name='Describe',
        ),
        migrations.RemoveField(
            model_name='section',
            name='Teacher_ID',
        ),
        migrations.AddField(
            model_name='grade',
            name='check',
            field=models.CharField(max_length=20, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='section',
            name='T_lastname',
            field=models.CharField(max_length=30, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='section',
            name='T_name',
            field=models.CharField(max_length=30, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='section',
            name='shortname',
            field=models.CharField(max_length=60, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='Course_ID',
            field=models.IntegerField(max_length=15, serialize=False, primary_key=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='Course_Name',
            field=models.CharField(max_length=100, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='Credit',
            field=models.IntegerField(max_length=10, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='grade',
            name='Grade',
            field=models.CharField(max_length=3),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='section',
            name='Section',
            field=models.IntegerField(max_length=10, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='section',
            name='classroom',
            field=models.CharField(max_length=20, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='section',
            name='date',
            field=models.CharField(max_length=9, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='section',
            name='st_endTime',
            field=models.CharField(max_length=11, blank=True),
            preserve_default=True,
        ),
    ]
