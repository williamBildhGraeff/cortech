from rest_framework import serializers
from empresa.models import Empresa
from endereco.models import Endereco
from endereco.serializer import EnderecoSerializer
from empresa.utils.validators import validar_cnpj

# Este serializer é avançado:
# - inclui nested serializer
# - validações customizadas
# - create/update sobrescritos
# - campos somente leitura
class EmpresaSerializer(serializers.ModelSerializer):
 def validate_cnpj(self, value):
  return validar_cnpj(value)
  
 # 👇 Inclui os dados completos do endereço dentro da empresa
 # Isso é chamado de "nested serializer"
 endereco = EnderecoSerializer()
 class Meta: 
  model = "empresa.Empresa"
  fields = '__all__'
  read_only_fields = ['id', 'updated_at']
 
 
  # =====================================================================
  # 🧠 CREATE (POST)
  # =====================================================================
  # Por padrão o ModelSerializer não sabe criar objetos filhos
  # quando usamos nested serializer.
  # Então precisamos sobrescrever o create.
 def create(self, validated_data):
   # Extrai os dados do nested serializer (endereco)
   endereco_data = validated_data.pop('endereco')
   # Cria primeiro o endereço
   endereco = Endereco.objects.create(**endereco_data)
   # Depois cria a empresa ligada ao endereço criado
   empresa = Empresa.objects.create(endereco=endereco, **validated_data)
   return empresa

  # =====================================================================
  # 🧠 UPDATE (PUT/PATCH)
  # =====================================================================
 def update(self, instance, validated_data):
   # Atualização separada do endereço
   endereco_data = validated_data.pop('endereco', None)
   if endereco_data:
    # Atualiza manualmente campo a campo do endereço existente
    for field, value in endereco_data.items():
     setattr(instance.endereco, field, value)
    instance.endereco.save()
    # Atualiza os campos normais da Empresa
   for field, value in validated_data.items():
    setattr(instance, field, value)
   instance.save()
   return instance