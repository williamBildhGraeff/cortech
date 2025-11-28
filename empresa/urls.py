from rest_framework.routers import DefaultRouter
from empresa.views import EnderecoViewSet,EmpresaViewSet

router = DefaultRouter()
router.register(r'empresas', EmpresaViewSet, basename = 'empresas')
router.register(r'enderecos', EnderecoViewSet, basename = 'enderecos')

urlpatterns = router.urls