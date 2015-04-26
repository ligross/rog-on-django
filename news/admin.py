from django.contrib import admin

from .models import News, NewsImage


class NewsAdmin(admin.ModelAdmin):
    list_display = ('news_title', 'pub_date')


class NewsImageInLine(admin.TabularInline):
    model = NewsImage
    extra = 1


class NewsAdmin(admin.ModelAdmin):
    inlines = [NewsImageInLine, ]

admin.site.register(News, NewsAdmin)

