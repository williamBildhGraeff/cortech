from .endereco_interface import EnderecoInterface
from .models import Endereco
from django.shortcuts import get_object_or_404

class EnderecoService(EnderecoInterface):
    def get(self, id=None):
        if id:
            return get_object_or_404(Endereco, id=id)
        return Endereco.objects.all()
    
    def post(self, data):
        endereco = Endereco.objects.create(**data)
        return endereco
    
    def put(self, id, data):
        endereco = self.get(id=id)
        for key, value in data.items():
            setattr(endereco, key, value)
        endereco.save()
        return endereco

    def delete(self, id):
        endereco = self.get(id=id)
        endereco.delete()
    