from rest_framework_nested import routers

from .views import WallpaperViewSet, CommentViewSet

router = routers.DefaultRouter()
router.register(r'wallpapers', WallpaperViewSet, basename='wallpaper')
wallpaper_router = routers.NestedDefaultRouter(router, 'wallpapers',lookup='wallpaper')

wallpaper_router.register('comments',CommentViewSet,basename='wallpaper-comment')


urlpatterns = router.urls + wallpaper_router.urls