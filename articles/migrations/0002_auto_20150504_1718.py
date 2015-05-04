# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_author',
            field=models.CharField(max_length=100, verbose_name=b'\xd0\x90\xd0\xb2\xd1\x82\xd0\xbe\xd1\x80 \xd1\x81\xd1\x82\xd0\xb0\xd1\x82\xd1\x8c\xd0\xb8 \xd0\xb8\xd0\xbb\xd0\xb8 \xd0\xbf\xd0\xb5\xd1\x80\xd0\xb5\xd0\xb2\xd0\xbe\xd0\xb4\xd0\xb0'),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_text',
            field=models.TextField(verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xba\xd1\x81\xd1\x82 \xd1\x81\xd1\x82\xd0\xb0\xd1\x82\xd1\x8c\xd0\xb8'),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_title',
            field=models.CharField(max_length=200, verbose_name=b'\xd0\x97\xd0\xb0\xd0\xb3\xd0\xbe\xd0\xbb\xd0\xbe\xd0\xb2\xd0\xbe\xd0\xba \xd1\x81\xd1\x82\xd0\xb0\xd1\x82\xd1\x8c\xd0\xb8'),
        ),
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateTimeField(verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xbf\xd1\x83\xd0\xb1\xd0\xbb\xd0\xb8\xd0\xba\xd0\xb0\xd1\x86\xd0\xb8\xd0\xb8'),
        ),
        migrations.AlterField(
            model_name='articleimage',
            name='image',
            field=models.ImageField(upload_to=b'', verbose_name=b'\xd0\x98\xd0\xb7\xd0\xbe\xd0\xb1\xd1\x80\xd0\xb0\xd0\xb6\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5'),
        ),
    ]
