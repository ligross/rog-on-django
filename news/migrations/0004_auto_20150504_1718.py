# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20150427_1538'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': '\u041d\u043e\u0432\u043e\u0441\u0442\u044c', 'verbose_name_plural': '\u041d\u043e\u0432\u043e\u0441\u0442\u0438'},
        ),
        migrations.AlterField(
            model_name='news',
            name='link_to_original',
            field=models.CharField(max_length=200, verbose_name=b'\xd0\xa1\xd1\x81\xd1\x8b\xd0\xbb\xd0\xba\xd0\xb0 \xd0\xbd\xd0\xb0 \xd0\xbe\xd1\x80\xd0\xb8\xd0\xb3\xd0\xb8\xd0\xbd\xd0\xb0\xd0\xbb'),
        ),
        migrations.AlterField(
            model_name='news',
            name='news_text',
            field=models.TextField(verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xba\xd1\x81\xd1\x82 \xd0\xbd\xd0\xbe\xd0\xb2\xd0\xbe\xd1\x81\xd1\x82\xd0\xb8'),
        ),
        migrations.AlterField(
            model_name='news',
            name='news_title',
            field=models.CharField(max_length=200, verbose_name=b'\xd0\x97\xd0\xb0\xd0\xb3\xd0\xbe\xd0\xbb\xd0\xbe\xd0\xb2\xd0\xbe\xd0\xba \xd0\xbd\xd0\xbe\xd0\xb2\xd0\xbe\xd1\x81\xd1\x82\xd0\xb8'),
        ),
        migrations.AlterField(
            model_name='news',
            name='preview_image',
            field=models.ImageField(default=None, upload_to=b'news', null=True, verbose_name=b'\xd0\x9a\xd0\xb0\xd1\x80\xd1\x82\xd0\xb8\xd0\xbd\xd0\xba\xd0\xb0 \xd0\xbf\xd1\x80\xd0\xb5\xd0\xb2\xd1\x8c\xd1\x8e', blank=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='pub_date',
            field=models.DateTimeField(verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xbf\xd1\x83\xd0\xb1\xd0\xbb\xd0\xb8\xd0\xba\xd0\xb0\xd1\x86\xd0\xb8\xd0\xb8'),
        ),
        migrations.AlterField(
            model_name='newsimage',
            name='image',
            field=models.ImageField(upload_to=b'', verbose_name=b'\xd0\x98\xd0\xb7\xd0\xbe\xd0\xb1\xd1\x80\xd0\xb0\xd0\xb6\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5'),
        ),
    ]
