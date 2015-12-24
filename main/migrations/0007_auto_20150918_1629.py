# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20150918_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='users',
            field=models.ManyToManyField(to='main.Profile', blank=True),
        ),
    ]
