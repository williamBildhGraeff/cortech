from rest_framework import serializers
from ..models import TipoManejo

class TipoManejoSerializer(serializers.ModelSerializer):
 class Meta:
  model = TipoManejo
  fields = '__all__'
  read_only_fields = ['id']