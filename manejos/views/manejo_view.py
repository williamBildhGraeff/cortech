from ..models import Manejo
from ..serializers import ManejoSerializer
from rest_framework import viewsets
class ManejoViewSet(viewsets.ModelViewSet):
 queryset = Manejo.objects.all()
 serializer_class = ManejoSerializer