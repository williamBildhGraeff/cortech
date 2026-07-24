from django.urls import path
from .views import FazendaViewSet

urlpatterns = [
    path('<int:produtor_id>/fazendas', FazendaViewSet.as_view(), name='fazendas'),
    path('<int:produtor_id>/fazendas/<int:id>/', FazendaViewSet.as_view(), name='fazenda'),
]