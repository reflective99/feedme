# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feeder', '0014_auto_20151207_2300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='categories',
        ),
    ]
