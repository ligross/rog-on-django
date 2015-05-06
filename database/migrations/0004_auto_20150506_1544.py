# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0003_auto_20150504_1742'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('page_title', models.CharField(max_length=200, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b')),
                ('page_text', models.TextField(verbose_name='\u0422\u0435\u043a\u0441\u0442')),
                ('pub_date', models.DateTimeField(verbose_name='\u0414\u0430\u0442\u0430 \u043f\u0443\u0431\u043b\u0438\u043a\u0430\u0446\u0438\u0438')),
                ('last_update', models.DateTimeField(verbose_name='\u0414\u0430\u0442\u0430 \u043e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u044f')),
            ],
            options={
                'verbose_name': '\u0421\u0442\u0440\u0430\u043d\u0438\u0446\u0430 \u0411\u0430\u0437\u044b \u0417\u043d\u0430\u043d\u0438\u0439',
                'verbose_name_plural': '\u0421\u0442\u0440\u0430\u043d\u0438\u0446\u044b \u0411\u0430\u0437\u044b \u0417\u043d\u0430\u043d\u0438\u0439',
            },
        ),
        migrations.CreateModel(
            name='PageImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'', verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435')),
                ('page', models.ForeignKey(related_name='images', to='database.Page')),
            ],
        ),
        migrations.AlterField(
            model_name='resource',
            name='resource_image',
            field=models.ImageField(upload_to=b'', verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u0440\u0435\u0441\u0443\u0440\u0441\u0430'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='resource_name',
            field=models.CharField(max_length=200, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0440\u0435\u0441\u0443\u0440\u0441\u0430'),
        ),
        migrations.AlterField(
            model_name='resourcenode',
            name='node_image',
            field=models.ImageField(default=None, upload_to=b'database', null=True, verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u0438\u0441\u0442\u043e\u0447\u043d\u0438\u043a\u0430', blank=True),
        ),
        migrations.AlterField(
            model_name='resourcenode',
            name='node_location',
            field=models.TextField(verbose_name='\u041c\u0435\u0441\u0442\u043e\u043d\u0430\u0445\u043e\u0436\u0434\u0435\u043d\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='resourcenode',
            name='node_name',
            field=models.CharField(max_length=200, verbose_name='\u0418\u0441\u0442\u043e\u0447\u043d\u0438\u043a \u0440\u0435\u0441\u0443\u0440\u0441\u0430'),
        ),
        migrations.AlterField(
            model_name='resourcenode',
            name='node_respawn_time',
            field=models.IntegerField(verbose_name='\u0412\u0440\u0435\u043c\u044f \u0440\u0435\u0441\u043f\u0430\u0443\u043d\u0430'),
        ),
        migrations.AlterField(
            model_name='resourcenode',
            name='node_yield',
            field=models.FloatField(verbose_name='\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e'),
        ),
    ]
