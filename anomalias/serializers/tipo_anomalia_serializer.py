from rest_framework import serializers
from anomalias.models import TipoAnomalia

class TipoAnomaliaSerializer(serializers.ModelSerializer):
 class Meta:
  model = TipoAnomalia
  fields = '__all__'
  read_only_fields = ['id'] 