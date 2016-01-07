# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('go', '0002_auto_20140911_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='short',
            field=models.SlugField(max_length=20, serialize=False, primary_key=True),
        ),
    ]
