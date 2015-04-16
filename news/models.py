from django.db import models


class News(models.Model):
    news_title = models.CharField(max_length=200)
    news_text = models.TextField()
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.news_title




