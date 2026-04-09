from empresa.interface.interface_empresa import EmpresaInterface
from django.shortcuts import get_object_or_404
from empresa.models import Empresa
from endereco.models import Endereco

class EmpresaService(EmpresaInterface):

    def get(self, id=None):
        if id:
            return get_object_or_404(Empresa, id=id)
        return Empresa.objects.all()

    def post(self, data):
        endereco_pop = data.pop('endereco')
        endereco = Endereco.objects.create(**endereco_pop)
        empresa = Empresa.objects.create(**data, endereco=endereco)
        return empresa

    def put(self, id, data):
        empresa = self.get(id=id)
        endereco_pop = data.pop('endereco')
        endereco = Endereco.objects.filter(id=empresa.endereco.id).update(**endereco_pop)
        for key, value in data.items():
            setattr(empresa, key, value)
        empresa.save()
        return empresa

    def delete(self, id):
        empresa = self.get(id=id)
        empresa.delete()