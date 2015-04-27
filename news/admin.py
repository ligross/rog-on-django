from django.contrib import admin
from django.db import models

from suit_ckeditor.widgets import CKEditorWidget

from .models import News, NewsImage


class NewsImageInLine(admin.TabularInline):
    model = NewsImage
    extra = 1


class NewsAdmin(admin.ModelAdmin):
    inlines = [NewsImageInLine, ]
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget},
    }

admin.site.register(News, NewsAdmin)

