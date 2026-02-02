from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .permissions import IsSelfOrReadOnly
from .serializers import UserProfileSerializer
from .models import UserFollow
from wallpapers.models import Wallpaper
from wallpapers.serializers import WallpaperSerializer

User = get_user_model()


class UserProfileView(viewsets.ModelViewSet):
    
    queryset = User.objects.prefetch_related("followers", "following")
    permission_classes = [IsSelfOrReadOnly]
    serializer_class = UserProfileSerializer

    @action(
        methods=["get"],
        detail=True,
    )
    def followers(self, request, pk=None):
        """Возвращает список пользователей, подписанных на данного пользователя."""
        user = self.get_object()
        followers = user.followers.all()
        serializer = UserProfileSerializer(followers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(
        methods=["get"],
        detail=True,
    )
    def following(self, request, pk=None):
        """Возвращает список пользователей, на которых подписан данный пользователь."""
        user = self.get_object()
        following = user.following.all()
        serializer = UserProfileSerializer(following, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=["post"], detail=True, permission_classes=[IsAuthenticated])
    def follow(self, request, pk=None):
        """Подписаться на пользователя"""
        target = self.get_object()
        user = request.user
        if user == target:
            return Response(
                {"success": False, "message": "You cannot follow yourself."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        follow, created = UserFollow.objects.get_or_create(
            from_user=user, to_user=target
        )
        if not created:
            return Response(
                {
                    "success": True,
                    "message": "You are already following this user.",
                    "is_following": True,
                    "followers_count": target.followers.count(),
                },
                status=status.HTTP_200_OK,
            )

        return Response(
            {
                "success": True,
                "message": "You are now following this user.",
                "is_following": True,
                "followers_count": target.followers.count(),
            },
            status=status.HTTP_201_CREATED,
        )

    @action(methods=["post"], detail=True, permission_classes=[IsAuthenticated])
    def unfollow(self, request, pk=None):
        """Отписаться от пользователя"""
        target = self.get_object()
        user = request.user
        deleted, _ = UserFollow.objects.filter(from_user=user, to_user=target).delete()

        if deleted == 0:
            return Response(
                {
                    "success": False,
                    "message": "You are not following this user.",
                    "is_following": False,
                    "followers_count": target.followers.count(),
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(
            {
                "success": True,
                "message": "You have unfollowed this user.",
                "is_following": False,
                "followers_count": target.followers.count(),
            },
            status=status.HTTP_200_OK,
        )

    @action(detail=False, permission_classes=[IsAuthenticated])
    def me(self, request):
        """Данные текущего пользователя"""
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)

    @action(detail=False, permission_classes=[IsAuthenticated], url_path='me/followers')
    def my_followers(self, request):
        """Список подписчиков текущего пользователя"""
        followers = request.user.followers.all()
        serializer = UserProfileSerializer(followers, many=True)
        return Response(serializer.data)

    @action(detail=False, permission_classes=[IsAuthenticated], url_path='me/following')
    def my_following(self, request):
        """Список пользователей, на которых подписан текущий пользователь."""
        following = request.user.following.all()
        serializer = UserProfileSerializer(following, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=["get"])
    def wallpapers(self, request, pk=None):
        """Список обоев пользователя"""
        user = self.get_object()
        wallpapers = Wallpaper.objects.filter(user=user).order_by("-uploaded_at")
        serializer = WallpaperSerializer(wallpapers, many=True, context={"request": request})
        return Response(serializer.data)
