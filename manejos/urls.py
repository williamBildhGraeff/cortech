from rest_framework.routers import DefaultRouter
from .views import ManejoViewSet,TipoManejoViewSet

router = DefaultRouter()
router.register(r'manejos', ManejoViewSet, basename = 'manejos')
router.register(r'tipos-manejos', TipoManejoViewSet, basename = 'tipos-manejos')

urlpatterns = router.urls