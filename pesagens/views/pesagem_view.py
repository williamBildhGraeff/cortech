from rest_framework import viewsets
from ..models import Pesagem
from ..serializer import PesagemSerializer

class PesagemViewSet(viewsets.ModelViewSet):
 queryset = Pesagem.objects.all()
 serializer_class = PesagemSerializer