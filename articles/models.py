# -*- coding: utf-8 -*-
from django.db import models


class Article(models.Model):
    article_title = models.CharField('Заголовок статьи', max_length=200)
    article_text = models.TextField('Текст статьи')
    article_author = models.CharField('Автор статьи или перевода', max_length=100)
    pub_date = models.DateTimeField('Дата публикации')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return unicode(self.article_title)

    def __unicode__(self):
        return '%s' % self.article_title



class ArticleImage(models.Model):
    article = models.ForeignKey(Article, related_name='images')
    image = models.ImageField('Изображение')