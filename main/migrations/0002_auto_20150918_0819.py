# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='badges',
            field=models.ManyToManyField(to='main.Badge', null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='interests',
            field=models.ManyToManyField(related_name='interests', null=True, to='main.Category'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phoneNumber',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(null=True, upload_to=b'users'),
        ),
    ]
