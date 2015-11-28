# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feeder', '0003_auto_20151106_0341'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedme_Users',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=20)),
            ],
        ),
    ]
