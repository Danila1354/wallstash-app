from .models import Wallpaper
from rest_framework import viewsets, generics
from .serializers import WallpaperSerializer


class WallpaperViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Wallpaper.objects.all().order_by("-uploaded_at")
    serializer_class = WallpaperSerializer
    lookup_field = "slug"
