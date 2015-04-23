# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_remove_article_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_author',
            field=models.CharField(default='admin', max_length=100),
            preserve_default=False,
        ),
    ]
