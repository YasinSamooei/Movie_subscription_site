from django.contrib import admin

from .models import *


@admin.register(Tag)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ["title"]
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    search_fields = ["title", "description", "author"]
    list_display = ["title", "author", "show_image"]
    list_filter = ["tag"]
    ordering = ["-created_at"]
    exclude = ["hit_count_generic"]
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Comment)
