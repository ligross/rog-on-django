# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('news_title', models.CharField(max_length=200)),
                ('news_text', models.TextField()),
                ('link_to_original', models.CharField(max_length=200)),
                ('preview_image', models.ImageField(default=None, null=True, upload_to=b'news', blank=True)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
            ],
        ),
        migrations.CreateModel(
            name='NewsImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'')),
                ('news', models.ForeignKey(related_name='images', to='news.News')),
            ],
        ),
    ]
