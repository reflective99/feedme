# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feeder', '0004_feedme_users'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Feedme_Users',
        ),
    ]
