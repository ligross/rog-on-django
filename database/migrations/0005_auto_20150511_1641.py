# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0004_auto_20150506_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pageimage',
            name='image',
            field=models.ImageField(default=None, upload_to=b'database', null=True, verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435', blank=True),
        ),
    ]
