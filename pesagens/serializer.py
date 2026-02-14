from rest_framework import serializers
from .models import Pesagem

class PesagemSerializer(serializers.ModelSerializer):
 class Meta:
  model = Pesagem
  fields = '__all__'
  read_only_fields = ['id', 'gmd_calculado_automatico']