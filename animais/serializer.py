from rest_framework import serializers
from .models import Animal
class AnimalSerializer(serializers.ModelSerializer):
 class Meta:
  model = Animal
  exclude = ['updated_at', 'created_at']
  read_only = ['id', 'ganho_acumulado', 'score_rendimento']