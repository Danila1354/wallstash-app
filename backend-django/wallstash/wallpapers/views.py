from rest_framework import viewsets
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import mixins
from django.shortcuts import get_object_or_404
from django.db.models import F
from django.http import FileResponse

from .serializers import CommentSerializer, WallpaperSerializer
from .models import WallpaperLike, Wallpaper, Comment
from .permissions import IsOwnerOrReadOnly


class WallpaperViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Wallpaper.objects.all().select_related("user").order_by("-uploaded_at")
    serializer_class = WallpaperSerializer
    lookup_field = "slug"

    def get_serializer_context(self):
        context = super().get_serializer_context()
        user = self.request.user
        if user.is_authenticated:
            liked_ids = set(
                WallpaperLike.objects.filter(user=user).values_list(
                    "wallpaper_id", flat=True
                )
            )
            context["user_likes"] = liked_ids
        else:
            context["user_likes"] = set()
        return context

    @action(detail=True, methods=["post"], permission_classes=[IsAuthenticated])
    def like(self, request, slug=None):
        """Поставить лайк обою."""
        wallpaper = self.get_object()
        user = request.user
        like, created = WallpaperLike.objects.get_or_create(
            wallpaper=wallpaper, user=user
        )
        if created:
            wallpaper.likes_count = WallpaperLike.objects.filter(
                wallpaper=wallpaper
            ).count()
            wallpaper.save(update_fields=["likes_count"])
            return Response(
                {
                    "success": True,
                    "message": "Wallpaper liked.",
                    "likes_count": wallpaper.likes_count,
                    "liked_by_user": True,
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(
            {
                "success": True,
                "message": "You have already liked this wallpaper.",
                "likes_count": wallpaper.likes_count,
                "liked_by_user": True,
            },
            status=status.HTTP_200_OK,
        )

    @action(detail=True, methods=["post"], permission_classes=[IsAuthenticated])
    def unlike(self, request, slug=None):
        """Убрать лайк с обоя."""
        wallpaper = self.get_object()
        user = request.user
        try:
            like = WallpaperLike.objects.get(wallpaper=wallpaper, user=user)
            like.delete()
            wallpaper.likes_count = WallpaperLike.objects.filter(
                wallpaper=wallpaper
            ).count()
            wallpaper.save(update_fields=["likes_count"])
            return Response(
                {
                    "success": True,
                    "message": "Wallpaper unliked.",
                    "likes_count": wallpaper.likes_count,
                    "liked_by_user": False,
                },
                status=status.HTTP_200_OK,
            )
        except WallpaperLike.DoesNotExist:
            return Response(
                {
                    "success": False,
                    "message": "You have not liked this wallpaper.",
                    "likes_count": wallpaper.likes_count,
                    "liked_by_user": False,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

    @action(detail=True, methods=["get"], permission_classes=[IsAuthenticated])
    def download(self, request, slug=None):
        wallpaper = self.get_object()
        Wallpaper.objects.filter(slug=wallpaper.slug).update(
            downloads_count=F("downloads_count") + 1
        )
        return FileResponse(
            wallpaper.image.open("rb"),
            as_attachment=True,
            filename=wallpaper.image.name.split("/")[-1],
        )


class ProfileWallpaperViewSet(viewsets.ModelViewSet):
    serializer_class = WallpaperSerializer
    permission_classes = [IsOwnerOrReadOnly]
    lookup_field = "slug"
    http_method_names = ["get", "post", "patch", "delete"]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        user_id = self.kwargs.get("user_pk")
        return Wallpaper.objects.filter(user_id=user_id).order_by("-uploaded_at")


class CommentViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_queryset(self):
        return (
            Comment.objects.filter(wallpaper__slug=self.kwargs["wallpaper_slug"])
            .select_related("user")
            .order_by("created_at")
        )

    def perform_create(self, serializer):
        wallpaper = get_object_or_404(Wallpaper, slug=self.kwargs["wallpaper_slug"])
        serializer.save(user=self.request.user, wallpaper=wallpaper)
