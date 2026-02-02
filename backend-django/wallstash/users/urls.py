from wallpapers.views import ProfileWallpaperViewSet
from .views import UserProfileView
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register("profile", UserProfileView, basename="profile")

profile_router = routers.NestedDefaultRouter(router, "profile", lookup="user")

profile_router.register(
    "wallpapers", ProfileWallpaperViewSet, basename="user-wallpapers"
)

urlpatterns = router.urls + profile_router.urls
