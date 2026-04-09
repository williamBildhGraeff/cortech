from anomalias.interfaces.anomalia_interface import AnomaliaInterface
from anomalias.models import Anomalia
from django.shortcuts import get_object_or_404
from animais.models import Animal
from anomalias.models import TipoAnomalia

class AnomaliaService(AnomaliaInterface):
    def get(self, id=None):
        if id:
            return get_object_or_404(Anomalia, id=id)
        return Anomalia.objects.all()

    def post(self, data):
        anomalia = Anomalia.objects.create(**data)
        return anomalia

    def put(self, id, data):
        anomalia = self.get(id=id)
        for key, value in data.items():
            setattr(anomalia, key, value)
        anomalia.save()
        return anomalia

    def delete(self, id):
        anomalia = self.get(id=id)
        anomalia.delete()
