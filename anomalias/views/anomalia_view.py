from rest_framework import viewsets
from anomalias.serializers import AnomaliaSerializer
from anomalias.models import Anomalia

class AnomaliaViewSet(viewsets.ModelViewSet):
 queryset = Anomalia.objects.all()
 serializer_class = AnomaliaSerializer