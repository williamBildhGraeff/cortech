from rest_framework.routers import DefaultRouter
from .views import AnimalViewSet

router = DefaultRouter()
router.register(r'animais', AnimalViewSet, basename = 'animais')
urlpatterns = router.urls