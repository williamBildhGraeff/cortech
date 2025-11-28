from rest_framework import viewsets
from usuarios.models import UsuarioEmpresa
from usuarios.serializers import UsuarioEmpresaSerializer

class UsuarioEmpresaViewSet(viewsets.ModelViewSet):
 queryset = UsuarioEmpresa.objects.all()
 serializer_class = UsuarioEmpresaSerializer