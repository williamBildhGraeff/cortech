from django.shortcuts import get_object_or_404

from produtor.interfaces.produtor_interface import ProdutorInterface
from produtor.models import Produtor


class ProdutorService(ProdutorInterface):
    def get(self, produtor_id:int | None = None):
        if produtor_id:
            return get_object_or_404(Produtor, id=produtor_id)
        return Produtor.objects.all()

    def post(self, produtor:dict):
        produtor = Produtor.objects.create(**produtor)
        return produtor

    def put(self, produtor_id:int, produtor:dict):
        produtorOrigin = self.get(produtor_id)
        for key, value in produtor.items():
            setattr(produtorOrigin, key, value)
        produtorOrigin.save()
        return produtorOrigin

    def delete(self, produtor_id:int):
        produtor = self.get(produtor_id)
        produtor.delete()
