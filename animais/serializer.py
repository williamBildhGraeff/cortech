from rest_framework import serializers
from .models import Animal
class AnimalSerializer(serializers.ModelSerializer):
 class Meta:
  model = Animal
  fields = '__all__'
  read_only = ['id', 'updated_at', 'created_at', 'ganho_acumulado', 'score_rendimento']