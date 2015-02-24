# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RegisteredUser',
            fields=[
                ('username', models.CharField(max_length=30, serialize=False, primary_key=True)),
                ('full_name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('approved', models.BooleanField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='URL',
            fields=[
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('target', models.URLField(max_length=1000)),
                ('short', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('clicks', models.IntegerField(default=0)),
                ('expires', models.DateTimeField(null=True, blank=True)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['short'],
            },
            bases=(models.Model,),
        ),
    ]
