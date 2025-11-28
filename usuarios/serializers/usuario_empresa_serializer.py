from rest_framework import serializers
from usuarios.models import UsuarioEmpresa

class UsuarioEmpresaSerializer(serializers.ModelSerializer):
 class Meta: 
  model = UsuarioEmpresa
  fields = [
   'id',
   'usuario',
   'empresa',
   'role'
  ]

  read_only_fields = ['id']
