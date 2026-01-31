from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import WallpaperViewSet, ProfileWallpaperViewSet

router = DefaultRouter()
router.register(r'wallpapers', WallpaperViewSet, basename='wallpaper')

urlpatterns = [
    path('', include(router.urls)),
]