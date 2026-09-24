from rest_framework.routers import DefaultRouter
from .views import LoteViewSet
from django.urls import path

urlpatterns = [
    path('<int:fazenda_id>/lotes/', LoteViewSet.as_view(), name='lotes'),
    path('<int:fazenda_id>/lotes/<int:id>/', LoteViewSet.as_view(), name='lotes')
]