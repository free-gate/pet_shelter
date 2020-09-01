from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'api', views.PetViewSet)
urlpatterns = router.urls
