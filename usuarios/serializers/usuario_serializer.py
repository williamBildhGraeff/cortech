from rest_framework import serializers
from usuarios.models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
 class Meta: 
  model = Usuario
  exclude = ['senha_hash']
  read_only_fields = ['id'] 
