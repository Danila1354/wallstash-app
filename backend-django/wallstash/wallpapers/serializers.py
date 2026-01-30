from rest_framework import serializers
from taggit.serializers import TagListSerializerField, TaggitSerializer
from .models import Wallpaper


class WallpaperSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()
    class Meta:
        model = Wallpaper
        fields = [
            "id",
            "user",
            "title",
            "slug",
            "image",
            "tags",
            "uploaded_at",
            "updated_at",
            "likes",
            "downloads",
            "width",
            "height",
            "file_size",
            "orientation",
        ]
