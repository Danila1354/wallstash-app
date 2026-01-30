from rest_framework.routers import DefaultRouter

from .views import WallpaperViewSet

router = DefaultRouter()
router.register(r'wallpapers', WallpaperViewSet, basename='wallpaper')
urlpatterns = router.urls
