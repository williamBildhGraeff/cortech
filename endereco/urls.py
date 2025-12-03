from rest_framework.routers import DefaultRouter
from endereco.views import EnderecoViewSet

router = DefaultRouter()
router.register(r'enderecos', EnderecoViewSet, basename = 'enderecos')

urlpatterns = router.urls