# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feeder', '0016_auto_20151207_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='city',
            field=models.CharField(max_length=20),
        ),
    ]
