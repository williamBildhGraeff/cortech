from rest_framework.routers import DefaultRouter
from .views import AnomaliaViewSet, TipoAnomaliaViewSet

router = DefaultRouter()
router.register(r'anomalias', AnomaliaViewSet, basename = 'anomalias')
router.register(r'tipos-anomalias', TipoAnomaliaViewSet, basename = 'tipos-anomalias')

urlpatterns = router.urls