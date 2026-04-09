from anomalias.interfaces.tipo_anomalia_interface import TipoAnomaliaInterface
from anomalias.models import TipoAnomalia
from django.shortcuts import get_object_or_404

class TipoAnomaliaService(TipoAnomaliaInterface):
    def get(self, id=None):
        if id:
            return get_object_or_404(TipoAnomalia, id=id)
        return TipoAnomalia.objects.all()

    def post(self, data):
        tipo_anomalia = TipoAnomalia.objects.create(**data)
        return tipo_anomalia

    def put(self, id, data):
        tipo_anomalia = self.get(id)
        for key, value in data.items():
            setattr(tipo_anomalia, key, value)
        tipo_anomalia.save()
        return tipo_anomalia

    def delete(self, id):
        tipo_anomalia = self.get(id=id)
        tipo_anomalia.delete()