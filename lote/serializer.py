from rest_framework import serializers
from lote.models import Lote
class LoteSerializer(serializers.ModelSerializer):
 class Meta:
  model = Lote
  fields = '__all__'
  read_only_fields = ['id', 'updated_at', 'created_at']