from rest_framework.routers import DefaultRouter
from empresa.views import EmpresaViewSet
from django.urls import path

urlpatterns = [
    path('empresas/', EmpresaViewSet.as_view(), name='empresas'),
    path('empresas/<int:id>/', EmpresaViewSet.as_view(), name='empresas')
]