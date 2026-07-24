from django.db.models import Count
from django.shortcuts import get_object_or_404
from fazendas.interface.fazenda_interface import FazendaInterface
from fazendas.models import Fazenda
from endereco.models import Endereco

class FazendaService(FazendaInterface):
    def post(self, data, produtor_id:int | None = None):
        endereco_pop = data.pop('endereco')
        endereco = Endereco.objects.create(**endereco_pop)
        fazenda = Fazenda.objects.create(**data, endereco=endereco)
        return fazenda

    def get(self, id, produtor_id:int | None = None):
        queryset = Fazenda.objects.annotate(
            quantidade_lotes=Count("lotes"),
            quantidade_animais=Count("lotes__animais")
        )
        if id:
            fazenda = get_object_or_404(Fazenda, id=id)
            return fazenda
        return queryset.filter(produtor_id=produtor_id)

    def put(self, id, data, produtor_id:int | None = None):
        fazenda = self.get(id=id)
        endereco_pop = data.pop('endereco')
        endereco = Endereco.objects.filter(id=fazenda.endereco.id).update(**endereco_pop)
        for key, value in data.items():
            setattr(fazenda, key, value)
        fazenda.save()
        return fazenda

    def delete(self, id, produtor_id:int | None = None):
        fazenda = self.get(id=id)
        fazenda.delete()
        return fazenda