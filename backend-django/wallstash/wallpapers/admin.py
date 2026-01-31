from django.contrib import admin
from django.template.defaultfilters import filesizeformat
from .models import Wallpaper, Category


@admin.register(Wallpaper)
class WallpaperAdmin(admin.ModelAdmin):
    list_display = (
        "title",
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


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    search_fields = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}
