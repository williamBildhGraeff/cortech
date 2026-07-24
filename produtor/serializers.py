from rest_framework import serializers
from .models import Produtor

class ProdutorSerializer(serializers.ModelSerializer):
 quantidade_animais = serializers.IntegerField(read_only=True)
 quantidade_lotes = serializers.IntegerField(read_only=True)
 class Meta:
  model = Produtor
  fields = '__all__'
  read_only_fields = ['id']