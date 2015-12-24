# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20150918_0819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='endDate',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='activity',
            name='startDate',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='badges',
            field=models.ManyToManyField(to='main.Badge', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='interests',
            field=models.ManyToManyField(related_name='interests', null=True, to='main.Category', blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phoneNumber',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(null=True, upload_to=b'users', blank=True),
        ),
    ]
