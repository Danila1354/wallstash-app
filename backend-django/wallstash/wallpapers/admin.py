from django.contrib import admin
from django.template.defaultfilters import filesizeformat
from django.utils.html import format_html

from .models import Wallpaper, Category


@admin.register(Wallpaper)
class WallpaperAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "preview",
        "user",
        "category",
        "uploaded_at",
        "likes_count",
        "downloads_count",
        "resolution",
        "file_size_human",
    )

    search_fields = ("title", "user__username", "category__name", "tags__name")
    list_filter = ("uploaded_at", "category", "tags")
    exclude = ("width", "height", "file_size")
    readonly_fields = (
        "likes_count",
        "downloads_count",
        "slug",
        "uploaded_at",
        "updated_at",
        "resolution",
        "file_size_human",
        "image_preview",
    )
    fieldsets = (
        (
            "Basic information",
            {
                "fields": (
                    "title",
                    "slug",
                    "user",
                    "category",
                    "image_preview",
                    "image",
                    "tags",
                )
            },
        ),
        (
            "Statistics",
            {
                "fields": (
                    "likes_count",
                    "downloads_count",
                )
            },
        ),
        (
            "Image metadata",
            {
                "fields": (
                    "resolution",
                    "file_size_human",
                )
            },
        ),
        (
            "Timestamps",
            {
                "fields": (
                    "uploaded_at",
                    "updated_at",
                )
            },
        ),
    )

    @admin.display(description="Preview")
    def preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height: 50px; max-width: 50px;" />',
                obj.image.url,
            )
        return "-"

    @admin.display(description="Resolution")
    def resolution(self, obj):
        if not obj.width or not obj.height:
            return "-"
        return f"{obj.width} × {obj.height} px"

    @admin.display(description="File size")
    def file_size_human(self, obj):
        if not obj.file_size:
            return "-"
        return filesizeformat(obj.file_size)

    @admin.display(description="Preview")
    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height: 400px; max-width: 400px;" />',
                obj.image.url,
            )
        return "-"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    search_fields = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}
