# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('group7', '0009_auto_20150702_1445'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='Projectg7',
        ),
        migrations.RemoveField(
            model_name='orderinfo',
            name='Order',
        ),
        migrations.DeleteModel(
            name='Orderinfo',
        ),
        migrations.RemoveField(
            model_name='requisition',
            name='Status_of',
        ),
        migrations.DeleteModel(
            name='Requisition',
        ),
        migrations.RemoveField(
            model_name='status_of',
            name='Order',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='Status_Of',
        ),
    ]
