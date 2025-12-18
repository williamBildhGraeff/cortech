from rest_framework import viewsets
from anomalias.serializers import TipoAnomaliaSerializer
from anomalias.models import TipoAnomalia

class TipoAnomaliaViewSet(viewsets.ModelViewSet):
 queryset = TipoAnomalia.objects.all()
 serializer_class = TipoAnomaliaSerializer