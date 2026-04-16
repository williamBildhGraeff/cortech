from rest_framework.routers import DefaultRouter
from .views import LoteViewSet
from django.urls import path

urlpatterns = [
    path('lotes/', LoteViewSet.as_view(), name='lotes'),
    path('lotes/<int:id>/', LoteViewSet.as_view(), name='lotes')
]