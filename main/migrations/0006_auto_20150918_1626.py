# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20150918_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='agent',
            field=models.ForeignKey(to='main.Agent'),
        ),
    ]
