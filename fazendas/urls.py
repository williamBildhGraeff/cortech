from django.urls import path
from .views import FazendaViewSet

urlpatterns = [
    path('fazendas/', FazendaViewSet.as_view(), name='fazendas'),
    path('fazendas/<int:id>/', FazendaViewSet.as_view(), name='fazenda'),
]