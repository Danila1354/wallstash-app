from rest_framework import serializers

from .models import Collection
from wallpapers.serializers import WallpaperSerializer


class CollectionSerializer(serializers.ModelSerializer):
    wallpapers = serializers.SerializerMethodField()

    class Meta:
        model = Collection
        fields = ["id", "title", "wallpapers", "created_at"]

    def get_wallpapers(self, obj):
        view = self.context.get("view")
        qs = obj.wallpapers.all().order_by("-uploaded_at")
        if view and view.action == "list":
            qs = qs[:5]
        serializer = WallpaperSerializer(qs, many=True, context=self.context)
        return serializer.data

