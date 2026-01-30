from django.contrib import admin

from .models import Wallpaper

@admin.register(Wallpaper)
class WallpaperAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'uploaded_at', 'likes', 'downloads')
    search_fields = ('title', 'user__username', 'tags__name')
    list_filter = ('uploaded_at', 'tags')
    readonly_fields = ('likes', 'downloads', 'uploaded_at', 'updated_at', 'width', 'height', 'file_size')
    exclude = ('slug', 'width', 'height', 'file_size')
