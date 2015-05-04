# -*- coding: utf-8 -*-
from django.db import models


class ResourceNode(models.Model):
    node_name = models.CharField('Источник ресурса', max_length=200)
    node_image = models.ImageField('Изображение источника', upload_to='database', default=None, blank=True, null=True)
    node_yield = models.FloatField('Количество')
    node_respawn_time = models.IntegerField('Время респауна')
    node_location = models.TextField('Местонахождение')

    class Meta:
        verbose_name = 'Источник ресурса'
        verbose_name_plural = 'Источники ресурсов'

    def __str__(self):
        return unicode(self.node_name)


class Resource(models.Model):
    resource_node = models.ForeignKey(ResourceNode, related_name='resource')
    resource_image = models.ImageField('Изображение ресурса')
    resource_name = models.CharField('Название ресурса', max_length=200)

    def __str__(self):
        return unicode(self.resource_name)


