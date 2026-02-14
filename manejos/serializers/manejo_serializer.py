from rest_framework import serializers
from ..models import Manejo

class ManejoSerializer(serializers.ModelSerializer):
    class Meta:
        ordering = ['-data']
        model = Manejo
        fields = '__all__'
        read_only_fields = ['id']