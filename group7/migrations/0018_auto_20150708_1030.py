# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('group7', '0017_auto_20150708_0940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requisition',
            name='Requisition_Id',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
    ]
