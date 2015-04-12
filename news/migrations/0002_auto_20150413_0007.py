# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tagging.fields


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='publ_date',
            new_name='pub_date',
        ),
        migrations.AddField(
            model_name='news',
            name='tags',
            field=tagging.fields.TagField(max_length=255, blank=True),
            preserve_default=True,
        ),
    ]
