from django.contrib import admin

# local
from .models import *

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    search_fields = ['title', 'description', 'creator']
    list_display = ['title', 'creator', 'show_image']
    list_filter = ['category']
    ordering = ['-created_at']
    exclude = ['likes', 'hit_count_generic', 'like_count', 'favorites']
    prepopulated_fields = {'slug': ('title',)}



