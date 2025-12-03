from rest_framework import viewsets
from endereco.models import Endereco
from endereco.serializer import EnderecoSerializer

# Create your views here.
class EnderecoViewSet(viewsets.ModelViewSet):
  queryset = Endereco.objects.all()
  serializer_class = EnderecoSerialize