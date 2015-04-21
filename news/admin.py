from django.contrib import admin

from .models import News, Image


class NewsAdmin(admin.ModelAdmin):
    list_display = ('news_title', 'pub_date')

admin.site.register(News)

