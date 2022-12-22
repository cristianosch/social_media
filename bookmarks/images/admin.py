from django.contrib import admin
from .models import Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'created']
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ['created']
