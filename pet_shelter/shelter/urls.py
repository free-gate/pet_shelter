from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register(r'api', views.PetApiViewSet, basename="pet")

urlpatterns = router.urls
