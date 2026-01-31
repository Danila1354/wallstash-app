from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import WallpaperViewSet, ProfileWallpaperViewSet

router = DefaultRouter()
router.register(r'wallpapers', WallpaperViewSet, basename='wallpaper')

urlpatterns = [
    path('', include(router.urls)),
    path(
    'profile/<int:user_id>/wallpapers/',
    ProfileWallpaperViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }),
        name='profile-wallpapers'
    ),
    path(
        'profile/<int:user_id>/wallpapers/<slug:slug>/',
        ProfileWallpaperViewSet.as_view({
            'get': 'retrieve',
            'put': 'update',
            'patch': 'partial_update',
            'delete': 'destroy'
        }),
        name='profile-wallpaper-detail'
        )
]