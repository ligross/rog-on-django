# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='resource_image',
            field=models.ImageField(upload_to=b'', verbose_name=b'\xd0\x98\xd0\xb7\xd0\xbe\xd0\xb1\xd1\x80\xd0\xb0\xd0\xb6\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5 \xd1\x80\xd0\xb5\xd1\x81\xd1\x83\xd1\x80\xd1\x81\xd0\xb0'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='resource_name',
            field=models.CharField(max_length=200, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd1\x80\xd0\xb5\xd1\x81\xd1\x83\xd1\x80\xd1\x81\xd0\xb0'),
        ),
        migrations.AlterField(
            model_name='resourcenode',
            name='node_image',
            field=models.ImageField(default=None, upload_to=b'database', null=True, verbose_name=b'\xd0\x98\xd0\xb7\xd0\xbe\xd0\xb1\xd1\x80\xd0\xb0\xd0\xb6\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xb8\xd1\x81\xd1\x82\xd0\xbe\xd1\x87\xd0\xbd\xd0\xb8\xd0\xba\xd0\xb0', blank=True),
        ),
        migrations.AlterField(
            model_name='resourcenode',
            name='node_location',
            field=models.TextField(verbose_name=b'\xd0\x9c\xd0\xb5\xd1\x81\xd1\x82\xd0\xbe\xd0\xbd\xd0\xb0\xd1\x85\xd0\xbe\xd0\xb6\xd0\xb4\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5'),
        ),
        migrations.AlterField(
            model_name='resourcenode',
            name='node_name',
            field=models.CharField(max_length=200, verbose_name=b'\xd0\x98\xd1\x81\xd1\x82\xd0\xbe\xd1\x87\xd0\xbd\xd0\xb8\xd0\xba \xd1\x80\xd0\xb5\xd1\x81\xd1\x83\xd1\x80\xd1\x81\xd0\xb0'),
        ),
        migrations.AlterField(
            model_name='resourcenode',
            name='node_respawn_time',
            field=models.IntegerField(verbose_name=b'\xd0\x92\xd1\x80\xd0\xb5\xd0\xbc\xd1\x8f \xd1\x80\xd0\xb5\xd1\x81\xd0\xbf\xd0\xb0\xd1\x83\xd0\xbd\xd0\xb0'),
        ),
        migrations.AlterField(
            model_name='resourcenode',
            name='node_yield',
            field=models.FloatField(verbose_name=b'\xd0\x9a\xd0\xbe\xd0\xbb\xd0\xb8\xd1\x87\xd0\xb5\xd1\x81\xd1\x82\xd0\xb2\xd0\xbe'),
        ),
    ]
