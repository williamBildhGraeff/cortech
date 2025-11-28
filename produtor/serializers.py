from rest_framework import serializers
from .models import Produtor

class ProdutorSerializer(serializers.ModelSerializer):
 class Meta:
  model = Produtor
  fields = '__all__'
  read_only_fields = ['id']