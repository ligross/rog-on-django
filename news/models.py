from django.db import models
from tagging.fields import TagField
from tagging.models import Tag


class News(models.Model):
    news_title = models.CharField(max_length=200)
    news_text = models.TextField()
    pub_date = models.DateTimeField('date published')
    tags = TagField()

    def get_tags(self):
        return Tag.objects.get_for_object(self)



