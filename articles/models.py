from django.db import models


class Article(models.Model):
    article_title = models.CharField(max_length=200)
    article_text = models.TextField()
    article_author = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.article_title
