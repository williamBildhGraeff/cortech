from django.db.models import Count

from lote.interfaces.lote_interface import LoteInterface
from django.shortcuts import get_object_or_404
from lote.models import Lote

class LoteService(LoteInterface):
    def get(self, id = None, fazenda_id = None):
        queryset = Lote.objects.annotate(
            quantidade_animais=Count("animais")
        )
        if id:
            return get_object_or_404(Lote, id=id)
        return queryset.filter(fazenda_id=fazenda_id)

    def post(self, data, fazenda_id = None):
        lote = Lote.objects.create(**data)
        return lote
    
    def put(self, id, data, fazenda_id = None):
        lote = self.get(id=id)
        for key, value in data.items():
            setattr(lote, key, value)
        lote.save()
        return lote

    def delete(self, id, fazenda_id = None):
        lote = self.get(id=id)
        lote.delete()