
from .views import ManejoViewSet,TipoManejoViewSet
from django.urls import path

urlpatterns = [
    path('tipo-manejo', TipoManejoViewSet.as_view(), name='tipo-manejo'),
    path('tipo-manejo/<int:tipomanejoid>', TipoManejoViewSet.as_view(), name='tipo-manejo'),
    path('manejo', ManejoViewSet.as_view(), name='manejo'),
    path('manejo/<int:manejoid>', ManejoViewSet.as_view(), name='manejo'),
]