from rest_framework.generics import get_object_or_404
from manejos.interfaces.tipo_manejo_interface import TipoManejoInterface
from manejos.models import TipoManejo

class TipoManejoService(TipoManejoInterface):
    def get(self, tipomanejoid:int | None = None):
        if tipomanejoid:
            return get_object_or_404(TipoManejo, id=tipomanejoid)
        return TipoManejo.objects.all()

    def post(self, data):
        return TipoManejo.objects.create(**data)

    def put(self, tipomanejoid:int, data):
        tipomanejo = self.get(tipomanejoid)
        for key, items in data.items():
            setattr(tipomanejo, key, items)
        tipomanejo.save()
        return tipomanejo

    def delete(self, tipomanejoid:int):
        tipomanejo = self.get(tipomanejoid)
        tipomanejo.delete()

