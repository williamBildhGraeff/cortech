from rest_framework import serializers
class LoteSerializer(serializers.ModelSerializer):
 class Meta:
  model = "lote.Lote"
  fields = '__all__'
  read_only_fields = ['id', 'updated_at', 'created_at']