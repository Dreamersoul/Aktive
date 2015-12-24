# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20150918_0821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='badges',
            field=models.OneToOneField(null=True, blank=True, to='main.Badge'),
        ),
    ]
