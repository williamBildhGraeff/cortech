from rest_framework import viewsets
from empresa.models import Endereco
from empresa.serializers import EnderecoSerializer

# O views.py é o controlador — ele define como as requisições HTTP são tratadas.
# É aqui que você recebe os dados do request, chama o serializer, acessa o model, e devolve a response.
# Você coloca aqui:
# Lógica da API (listar, criar, atualizar, deletar)
# Regras de acesso (quem pode o quê)
# Uso de querysets, filters, permissions, etc.

class EnderecoViewSet(viewsets.ModelViewSet):
  queryset = Endereco.objects.all()
  serializer_class = EnderecoSerializer

    # ViewSet do Endereco fornece automaticamente:
    # - GET /enderecos/
    # - GET /enderecos/<id>/
    # - POST /enderecos/
    # - PUT/PATCH /enderecos/<id>/
    # - DELETE /enderecos/<id>/
  