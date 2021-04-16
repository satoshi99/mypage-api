from django.contrib import admin
from . import models

class ContentImageInline(admin.TabularInline):
    model = models.ContentImage

class PostAdmin(admin.ModelAdmin):
    inlines = [
        ContentImageInline,
    ]

# Register your models here.
admin.site.register(models.Tag)
admin.site.register(models.Post, PostAdmin)

