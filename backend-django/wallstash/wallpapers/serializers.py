from rest_framework.reverse import reverse
from rest_framework import serializers
from taggit.serializers import TagListSerializerField, TaggitSerializer
from django.template.defaultfilters import filesizeformat

from .models import Wallpaper, Comment


class WallpaperSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()
    file_size_human = serializers.SerializerMethodField(read_only=True)
    liked_by_user = serializers.SerializerMethodField(read_only=True)
    username = serializers.SerializerMethodField(read_only=True)
    image_preview = serializers.ImageField(read_only=True)
    detail_link = serializers.SerializerMethodField(read_only=True)
    download_link = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Wallpaper
        fields = [
            "id",
            "title",
            "slug",
            "user",
            "username",
            "image",
            "image_preview",
            "detail_link",
            "download_link",
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
        read_only_fields = [
            "id",
            "user",
            "slug",
            "uploaded_at",
            "updated_at",
            "likes_count",
            "downloads_count",
            "width",
            "height",
            "orientation",
        ]

    def get_liked_by_user(self, obj):
        user_likes = self.context.get("user_likes", set())
        return obj.id in user_likes

    def get_file_size_human(self, obj):
        return filesizeformat(obj.file_size)

    def get_username(self, obj):
        return obj.user.username

    def get_detail_link(self, obj):
        request = self.context.get("request")
        if request:
            return request.build_absolute_uri(obj.get_absolute_url())
        return obj.get_absolute_url()

    def get_download_link(self, obj):
        request = self.context.get("request")
        return reverse("wallpaper-download", kwargs={"slug": obj.slug}, request=request)


class CommentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)
    first_name = serializers.CharField(source="user.first_name", read_only=True)
    last_name = serializers.CharField(source="user.last_name", read_only=True)

    class Meta:
        model = Comment
        fields = ["id", "username", "first_name", "last_name", "text", "created_at"]
        read_only_fields = ["created_at", "id"]
