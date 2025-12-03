from rest_framework.routers import DefaultRouter
from .views import FazendaViewSet

router = DefaultRouter()
router.register(r'fazendas', FazendaViewSet, basename = 'fazendas')

urlpatterns = router.urls