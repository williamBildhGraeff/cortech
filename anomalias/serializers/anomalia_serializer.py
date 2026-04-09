from rest_framework import serializers
from anomalias.models import Anomalia

class AnomaliaSerializer(serializers.ModelSerializer):
 class Meta:
  model = Anomalia
  fields = '__all__'
  read_only_fields = ['id']