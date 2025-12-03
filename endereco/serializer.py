from rest_framework import serializers
from empresa.models import Empresa,Endereco
from empresa.utils.validators import validar_cep

# O serializers.py é onde você controla o que entra e o que sai da sua API.
# Ele é o DTO (Data Transfer Object) do Django REST Framework.

# Ele faz 2 coisas importantes:
# 1️⃣ Converte objetos do banco → JSON (para enviar ao front-end ou API externa)
# 2️⃣ Converte JSON recebido → objetos validados → salvos no banco
#
# Por isso ele é onde você:
# - define quais campos serão expostos
# - adiciona validações
# - cria regras de leitura/escrita (read_only, write_only)
# - manipula dados antes de salvar (create/update)
class EnderecoSerializer(serializers.ModelSerializer):
 def validate_cep(self, value):
  return validar_cep(value)
 # Este serializer representa apenas o Endereco.
 # Ele é "simples" porque será usado como nested serializer dentro de Empresa.

 # A classe Meta controla como o ModelSerializer funciona
 class Meta:
  # Qual model ele representa?
  model = Endereco
 # Quais campos serão expostos na API?
  fields = '__all__' 
  # read_only_fields evita que o front sobrescreva
  # valores que não devem ser alterados diretamente.
  read_only_fields = ['id']


