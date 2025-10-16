from rest_framework.routers import DefaultRouter
from .views import OwnerViewSet, PropertyViewSet

router = DefaultRouter()
router.register(r"owners", OwnerViewSet, basename="owner")
router.register(r"properties", PropertyViewSet, basename="property")

urlpatterns = router.urls
