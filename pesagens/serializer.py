from rest_framework import serializers
from .models import Pesagem

class PesagemSerializer(serializers.ModelSerializer):
 brinco = serializers.CharField(source='animal.brinco', read_only=True)
 class Meta:
  model = Pesagem
  fields = '__all__'
  read_only_fields = ['id', 'gmd_calculado_automatico']


class PesagemIndicadoresSerializer(serializers.Serializer):
 primeira_pesagem = serializers.DecimalField(
  max_digits=6,
  decimal_places=2,
  allow_null=True
 )
 ultima_pesagem = serializers.DecimalField(
  max_digits=6,
  decimal_places=2,
  allow_null=True
 )
 ganho_total = serializers.DecimalField(
  max_digits=6,
  decimal_places=2,
  allow_null=True
 )
 gmd_medio = serializers.DecimalField(
  max_digits=6,
  decimal_places=2,
  allow_null=True
 )
 gmd_atual = serializers.DecimalField(
  max_digits=6,
  decimal_places=2,
  allow_null=True
 )