from rest_framework.routers import DefaultRouter
from .views import AnomaliaViewSet, TipoAnomaliaViewSet
from django.urls import path

urlpatterns = [
    path('tipos-anomalias/', TipoAnomaliaViewSet.as_view(), name='tipos-anomalias'),
    path('tipos-anomalias/<int:id>/', TipoAnomaliaViewSet.as_view(), name='tipos-anomalias'),
     path('anomalias/', AnomaliaViewSet.as_view(), name='anomalias'),
    path('anomalias/<int:id>/', AnomaliaViewSet.as_view(), name='anomalias')
]