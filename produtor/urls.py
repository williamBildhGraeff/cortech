from produtor.views import ProdutorViewSet
from django.urls import path
urlpatterns = [
    path('produtor/', ProdutorViewSet.as_view(), name='produtor'),
    path('produtor/<int:produtor_id>/', ProdutorViewSet.as_view(), name='produtor'),
]