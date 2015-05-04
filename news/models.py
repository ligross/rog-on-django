# -*- coding: utf-8 -*-
from django.db import models


class News(models.Model):
    news_title = models.CharField('Заголовок новости', max_length=200)
    news_text = models.TextField('Текст новости')
    link_to_original = models.CharField('Ссылка на оригинал', max_length=200)
    preview_image = models.ImageField('Картинка превью', upload_to='news', default=None, blank=True, null=True)
    pub_date = models.DateTimeField('Дата публикации')

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return unicode(self.news_title)

    def __unicode__(self):
        return '%s' % self.news_title


class NewsImage(models.Model):
    news = models.ForeignKey(News, related_name='images')
    image = models.ImageField('Изображение')


