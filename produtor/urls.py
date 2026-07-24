from produtor.views import ProdutorViewSet
from django.urls import path
urlpatterns = [
    path('<int:empresa_id>/produtor/', ProdutorViewSet.as_view(), name='produtor'),
    path('<int:empresa_id>/produtor/<int:produtor_id>/', ProdutorViewSet.as_view(), name='produtor'),
]