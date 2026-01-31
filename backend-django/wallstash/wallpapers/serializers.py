from rest_framework import serializers
from taggit.serializers import TagListSerializerField, TaggitSerializer
from django.template.defaultfilters import filesizeformat

from .models import Wallpaper


class WallpaperSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()
    file_size_human = serializers.SerializerMethodField()
    liked_by_user = serializers.SerializerMethodField()

    class Meta:
        model = Wallpaper
        fields = [
            "id",
            "user",
            "title",
            "slug",
            "image",
            "category",
            "tags",
            "uploaded_at",
            "updated_at",
            "likes_count",
            "downloads_count",
            "width",
            "height",
            "file_size_human",
            "orientation",
            "liked_by_user",
        ]
    
    def get_liked_by_user(self, obj):
        user_likes = self.context.get('user_likes', set())
        return obj.id in user_likes

    def get_file_size_human(self, obj):
        return filesizeformat(obj.file_size)
