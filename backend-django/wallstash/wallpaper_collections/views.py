from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import action
from wallpapers.permissions import IsOwnerOrReadOnly
from wallpapers.models import Wallpaper
from wallpapers.serializers import (
    AddWallpaperSerializer,
    UploadWallpaperSerializer,
)
from rest_framework import status
from rest_framework.response import Response

from .models import Collection
from .serializers import CollectionSerializer


class UserCollectionViewSet(viewsets.ModelViewSet):
    serializer_class = CollectionSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        user_id = self.kwargs.get("user_pk")
        return (
            Collection.objects.filter(user_id=user_id)
            .order_by("-created_at")
            .prefetch_related("wallpapers")
        )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(
        detail=True,
        methods=["post"],
        permission_classes=[IsOwnerOrReadOnly],
        serializer_class=AddWallpaperSerializer,
    )
    def add_wallpaper(self, request, user_pk=None, pk=None):
        collection = self.get_object()

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        wallpaper_id = serializer.validated_data["wallpaper_id"]

        wallpaper = get_object_or_404(Wallpaper, id=wallpaper_id, user=request.user)

        collection.wallpapers.add(wallpaper)

        return Response(
            {"success": True, "message": "Wallpaper added successfully"},
            status=status.HTTP_200_OK,
        )

    @action(
        detail=True,
        methods=["post"],
        permission_classes=[IsOwnerOrReadOnly],
        serializer_class=UploadWallpaperSerializer,
    )
    def upload_wallpaper(self, request, user_pk=None, pk=None):
        collection = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        wallpaper = serializer.save(user=request.user)
        collection.wallpapers.add(wallpaper)

        return Response(
            {
                "success": True,
                "message": "Wallpaper uploaded and added to collection",
                "wallpaper_id": wallpaper.id,
            },
            status=status.HTTP_201_CREATED,
        )
