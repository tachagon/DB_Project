# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('group5', '0002_auto_20150708_0028'),
    ]

    operations = [
        migrations.CreateModel(
            name='accept',
            fields=[
                ('No_accept', models.IntegerField(default=0, serialize=False, primary_key=True)),
                ('accept_status', models.CharField(max_length=20)),
                ('Date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Estimate',
            fields=[
                ('studentID', models.CharField(max_length=13, serialize=False, primary_key=True)),
                ('image_estimate', models.ImageField(upload_to=b'group5/image_estimate')),
                ('image_time', models.ImageField(upload_to=b'group5/image_time')),
            ],
        ),
        migrations.CreateModel(
            name='StatusPetition',
            fields=[
                ('NoPetition', models.IntegerField(default=0, serialize=False, primary_key=True)),
                ('StatusPetition', models.CharField(max_length=50)),
                ('Date', models.DateField()),
                ('Date2', models.DateField()),
                ('send', models.CharField(max_length=20)),
                ('to', models.CharField(max_length=100)),
                ('Internship', models.ForeignKey(to='group5.Internship')),
                ('studentG5', models.ForeignKey(to='group5.studentG5')),
            ],
        ),
        migrations.AddField(
            model_name='accept',
            name='StatusPetition',
            field=models.ForeignKey(to='group5.StatusPetition'),
        ),
    ]
