from django.contrib import admin

from .models import Article, ArticleImage


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('article_title', 'pub_date')


class ArticleImageInLine(admin.TabularInline):
    model = ArticleImage
    extra = 3


class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleImageInLine, ]


admin.site.register(Article, ArticleAdmin)

