from django.contrib import admin
from django.db import models


from .models import ResourceNode, Resource


class ResourceInline(admin.StackedInline):
    model = Resource
    extra = 3

class ResourceNodeAdmin(admin.ModelAdmin):
    inlines = [ResourceInline]

admin.site.register(ResourceNode, ResourceNodeAdmin)