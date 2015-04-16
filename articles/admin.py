from django.contrib import admin

from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('article_title', 'pub_date')

admin.site.register(Article)

