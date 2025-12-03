from rest_framework import viewsets
from .models import Empresa
from .serializer import EmpresaSerializer

class EmpresaViewSet(viewsets.ModelViewSet):
 queryset = Empresa.objects.all()
 serializer_class = EmpresaSerializer
 
# 
#  ViewSet da Empresa controla todas as operações CRUD da tabela.
#  - Utiliza o EmpresaSerializer para validar dados
#  - Retorna JSON para o front-end
# 
 