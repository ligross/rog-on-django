# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20150413_0007'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='link_to_original',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
