from rest_framework.routers import DefaultRouter
from produtor.views import ProdutorViewSet

router = DefaultRouter()

router.register(r'produtores', ProdutorViewSet, basename = 'produtores')

urlpatterns = router.urls