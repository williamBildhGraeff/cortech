from rest_framework import serializers
from ..models import Fazenda
from endereco.models import Endereco
from endereco.serializer import EnderecoSerializer

class FazendaSerializer(serializers.ModelSerializer):
    endereco = EnderecoSerializer()

    class Meta:
        model = Fazenda
        fields = '__all__'
        read_only_fields = ['id', 'update_at', 'create_at']

    def create(self, validated_data):
        endereco_data = validated_data.pop("endereco")
        endereco = Endereco.objects.create(**endereco_data)

        fazenda = Fazenda.objects.create(
            endereco=endereco,
            **validated_data
        )

        return fazenda