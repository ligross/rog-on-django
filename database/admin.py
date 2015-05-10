from django.contrib import admin
from django.db import models

from suit_ckeditor.widgets import CKEditorWidget

from .models import Page, PageImage


class PageImageInLine(admin.TabularInline):
    model = PageImage
    extra = 3


class PageAdmin(admin.ModelAdmin):
    inlines = [PageImageInLine, ]
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget},
    }



admin.site.register(Page, PageAdmin)
