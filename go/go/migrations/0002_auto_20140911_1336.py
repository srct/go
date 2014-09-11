# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('go', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='qrclicks',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='url',
            name='socialclicks',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
