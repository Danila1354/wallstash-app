from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from wallpapers.permissions import IsOwnerOrReadOnly
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

    @action(detail=True, methods=['post'], permission_classes=[IsOwnerOrReadOnly])
    def add_wallpaper():
        pass
