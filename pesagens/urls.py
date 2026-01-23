from rest_framework.routers import DefaultRouter
from .views import PesagemViewSet
from .views import ImportarPesagensCSV
from .views import ExportarCsvPesagem
from django.urls import path

router = DefaultRouter()
router.register(r'pesagens', PesagemViewSet, basename = 'pesagens')

urlpatterns = [
 path('lotes/<int:lote_id>/importar-pesagem', ImportarPesagensCSV.as_view(), name = 'importar-pesagens'),
 path('exportar-pesagem/', ExportarCsvPesagem.as_view(), name = 'exportar-pesagens')
]

urlpatterns += router.urls