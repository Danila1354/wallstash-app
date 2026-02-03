from .views import UserProfileView
from rest_framework_nested import routers
from wallpaper_collections.views import UserCollectionViewSet

router = routers.DefaultRouter()
router.register("profile", UserProfileView, basename="profile")

profile_router = routers.NestedDefaultRouter(router, "profile", lookup="user")

profile_router.register(
    "collections", UserCollectionViewSet, basename="user-collections"
)

urlpatterns = router.urls + profile_router.urls
