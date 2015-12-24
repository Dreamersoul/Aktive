# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20150918_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='userCount',
            field=models.IntegerField(default=0),
        ),
    ]
