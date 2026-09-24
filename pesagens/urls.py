from rest_framework.routers import DefaultRouter
from .views import PesagemViewSet
from .services import ImportarPesagensCSV
from .views.export_view import ExportarCsvPesagem
from django.urls import path

urlpatterns = [
 path('lotes/<int:lote_id>/importar-pesagens', ImportarPesagensCSV.as_view(), name = 'importar-pesagens'),
 path('exportar-pesagens/', ExportarCsvPesagem.as_view(), name = 'exportar-pesagens'),
 path('lote/<int:lote_id>/pesagens', PesagemViewSet.as_view(), name = 'pesagens'),
 path('<int:animal_id>/pesagens', PesagemViewSet.as_view(), name = 'pesagens'),
 path('pesagens/<int:pesagem_id>', PesagemViewSet.as_view(), name = 'pesagens'),
]
