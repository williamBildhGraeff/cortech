from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, UsuarioEmpresaViewSet

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet, basename = 'usuarios')
router.register(r'usuarios-empresas', UsuarioEmpresaViewSet, basename = 'usuarios-empresas')

urlpatterns = router.urls