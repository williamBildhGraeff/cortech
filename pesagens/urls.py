from rest_framework.routers import DefaultRouter
from .views import PesagemViewSet
from .services import ImportarPesagensCSV
from .views.export_view import ExportarCsvPesagem
from django.urls import path

urlpatterns = [
 path('lotes/<int:lote_id>/importar-pesagem', ImportarPesagensCSV.as_view(), name = 'importar-pesagens'),
 path('exportar-pesagem/', ExportarCsvPesagem.as_view(), name = 'exportar-pesagens'),
 path('pesagens', PesagemViewSet.as_view(), name = 'pesagens'),
 path('pesagens/<int:pesagem_id>', PesagemViewSet.as_view(), name = 'pesagens'),
]
