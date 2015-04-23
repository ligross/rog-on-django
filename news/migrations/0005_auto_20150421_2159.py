# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_news_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='image',
            new_name='preview_image',
        ),
    ]
