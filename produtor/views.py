# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ProdutorSerializer
class ProdutorViewSet(viewsets.ModelViewSet):
 serialize_class = ProdutorSerializer

 def get_queryset(self):
  return Produtor.objects.filter(usuario = self.request.usuario)

 def perform_create(self, serializer):
  serializer.save(usuario=self.request.usuario)