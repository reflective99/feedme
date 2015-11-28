# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeder', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='categories',
            field=models.CharField(default='American (New)', max_length=100),
            preserve_default=False,
        ),
    ]