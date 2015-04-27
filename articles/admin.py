from django.contrib import admin
from django.db import models

from suit_ckeditor.widgets import CKEditorWidget

from .models import Article, ArticleImage


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('article_title', 'pub_date')


class ArticleImageInLine(admin.TabularInline):
    model = ArticleImage
    extra = 3


class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleImageInLine, ]
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget},
    }


admin.site.register(Article, ArticleAdmin)

