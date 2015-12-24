# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20150918_1040'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='badges',
            new_name='badge',
        ),
    ]
