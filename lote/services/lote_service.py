from lote.interfaces.lote_interface import LoteInterface
from django.shortcuts import get_object_or_404
from lote.models import Lote

class LoteService(LoteInterface):
    def get(self, id = None):
        if id:
            return get_object_or_404(Lote, id=id)
        return Lote.objects.all()

    def post(self, data):
        lote = Lote.objects.create(**data)
        return lote
    
    def put(self, id, data):
        lote = self.get(id=id)
        for key, value in data.items():
            setattr(lote, key, value)
        lote.save()
        return lote

    def delete(self, id):
        lote = self.get(id=id)
        lote.delete()