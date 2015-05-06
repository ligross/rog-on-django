# -*- coding: utf-8 -*-
from django.db import models


class Page(models.Model):
    page_title = models.CharField(u'Название страницы', max_length=200)
    page_text = models.TextField(u'Текст')
    pub_date = models.DateTimeField(u'Дата публикации')
    last_update = models.DateTimeField(u'Дата обновления')

    class Meta:
        verbose_name = u'Страница Базы Знаний'
        verbose_name_plural = u'Страницы Базы Знаний'

    def __str__(self):
        return unicode(self.page_title)

    def __unicode__(self):
        return '%s' % self.page_title


class PageImage(models.Model):
    page = models.ForeignKey(Page, related_name='images')
    image = models.ImageField(u'Изображение')


class ResourceNode(models.Model):
    node_name = models.CharField(u'Источник ресурса', max_length=200)
    node_image = models.ImageField(u'Изображение источника', upload_to='database', default=None, blank=True, null=True)
    node_yield = models.FloatField(u'Количество')
    node_respawn_time = models.IntegerField(u'Время респауна')
    node_location = models.TextField(u'Местонахождение')

    def __str__(self):
        return unicode(self.node_name)

    def __unicode__(self):
        return '%s' % self.node_name

    class Meta:
        verbose_name = u'Источник ресурса'
        verbose_name_plural = u'Источники ресурсов'


class Resource(models.Model):
    resource_node = models.ForeignKey(ResourceNode, related_name='resource')
    resource_image = models.ImageField(u'Изображение ресурса')
    resource_name = models.CharField(u'Название ресурса', max_length=200)

    def __str__(self):
        return unicode(self.resource_name)

    def __unicode__(self):
        return '%s' % self.resource_name


