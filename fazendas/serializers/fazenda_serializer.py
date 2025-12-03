from rest_framework import serializers
from ..models import Fazenda
class FazendaSerializer(serializers.ModelSerializer):
 class Meta:
  model = Fazenda
  fields = '_all__'
  read_only_fields = ['id', 'update_at', 'create_at']