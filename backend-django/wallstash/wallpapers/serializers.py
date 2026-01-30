from rest_framework import serializers
from taggit.serializers import TagListSerializerField, TaggitSerializer
from django.template.defaultfilters import filesizeformat

from .models import Wallpaper


class WallpaperSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()
    file_size_human = serializers.SerializerMethodField()

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
            "file_size_human",
            "orientation",
        ]

    def get_file_size_human(self, obj):
        return filesizeformat(obj.file_size)
