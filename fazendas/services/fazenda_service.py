from django.shortcuts import get_object_or_404
from fazendas.interface.fazenda_interface import FazendaInterface
from fazendas.models import Fazenda
from endereco.models import Endereco

class FazendaService(FazendaInterface):
    def post(self, data):
        endereco_pop = data.pop('endereco')
        endereco = Endereco.objects.create(**endereco_pop)
        fazenda = Fazenda.objects.create(**data, endereco=endereco)
        return fazenda

    def get(self, id):
        if id:
            fazenda = get_object_or_404(Fazenda, id=id)
            return fazenda
        fazenda = Fazenda.objects.all()
        return fazenda

    def put(self, id, data):
        fazenda = self.get(id=id)
        endereco_pop = data.pop('endereco')
        endereco = Endereco.objects.filter(id=fazenda.endereco.id).update(**endereco_pop)
        for key, value in data.items():
            setattr(fazenda, key, value)
        fazenda.save()
        return fazenda

    def delete(self, id):
        fazenda = self.get(id=id)
        fazenda.delete()
        return fazenda