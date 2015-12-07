# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feeder', '0015_remove_restaurant_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='cat',
            field=models.CharField(max_length=100, db_index=True),
        ),
    ]
