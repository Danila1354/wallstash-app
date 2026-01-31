from django.urls import path
from wallpapers.views import ProfileWallpaperViewSet
from .views import UserProfileView

urlpatterns = [
    path(
        '<int:user_id>/',
        UserProfileView.as_view({
            'get': 'retrieve',
            'put': 'update',
            'patch': 'partial_update',
            'delete': 'destroy'
        }),
        name='user-profile'
    ),

    path(
        '<int:user_id>/wallpapers/',
        ProfileWallpaperViewSet.as_view({
            'get': 'list',
            'post': 'create'
        }),
        name='user-wallpapers'
    ),
    path(
        '<int:user_id>/wallpapers/<slug:slug>/',
        ProfileWallpaperViewSet.as_view({
            'get': 'retrieve',
            'put': 'update',
            'patch': 'partial_update',
            'delete': 'destroy'
        }),
        name='user-wallpaper-detail'
    ),
]