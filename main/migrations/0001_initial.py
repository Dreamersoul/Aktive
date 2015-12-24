# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('location', geoposition.fields.GeopositionField(max_length=42, null=True)),
                ('userCount', models.IntegerField()),
                ('startDate', models.DateTimeField(null=True)),
                ('endDate', models.DateTimeField(null=True)),
                ('price', models.FloatField(null=True)),
                ('isActivity', models.BooleanField()),
                ('image', models.ImageField(upload_to=b'activity')),
            ],
        ),
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phoneNumber', models.CharField(max_length=30)),
                ('website', models.CharField(max_length=200)),
                ('profile', models.OneToOneField(related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Badge',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('icon', models.ImageField(upload_to=b'Badges')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('badges', models.OneToOneField(to='main.Badge')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phoneNumber', models.CharField(max_length=30)),
                ('picture', models.ImageField(upload_to=b'users')),
                ('badges', models.ManyToManyField(to='main.Badge')),
                ('interests', models.ManyToManyField(related_name='interests', to='main.Category')),
                ('profile_user', models.OneToOneField(related_name='profile_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='activity',
            name='agent',
            field=models.OneToOneField(to='main.Agent'),
        ),
        migrations.AddField(
            model_name='activity',
            name='category',
            field=models.ForeignKey(to='main.Category'),
        ),
        migrations.AddField(
            model_name='activity',
            name='users',
            field=models.ManyToManyField(to='main.Profile'),
        ),
    ]
