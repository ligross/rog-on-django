# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('resource_image', models.ImageField(upload_to=b'')),
                ('resource_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ResourceNode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('node_name', models.CharField(max_length=200)),
                ('node_image', models.ImageField(default=None, null=True, upload_to=b'database', blank=True)),
                ('node_yield', models.FloatField()),
                ('node_respawn_time', models.IntegerField()),
                ('node_location', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='resource',
            name='resource_node',
            field=models.ForeignKey(related_name='resource', to='database.ResourceNode'),
        ),
    ]
