from rest_framework import viewsets
from ..models import TipoManejo
from ..serializers import TipoManejoSerializer

class TipoManejoViewSet(viewsets.ModelViewSet):
 queryset = TipoManejo.objects.all()
 serializer_class = TipoManejoSerializer 