from django.contrib import admin

# local
from .models import *

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Actors)
class ActorsAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    search_fields = ['title', 'description', 'creator']
    list_display = ['title', 'creator', 'show_image']
    list_filter = ['category']
    ordering = ['-created_at']
    exclude = ['likes', 'hit_count_generic', 'favorites']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user','all_user', 'created_at')


# @admin.register(Serial)
# class SerialAdmin(admin.ModelAdmin):
#     search_fields = ['name']
#     list_display = ['name', 'show_image','year']
#     ordering = ['-created_at']
#     prepopulated_fields = {'slug': ('name',)}