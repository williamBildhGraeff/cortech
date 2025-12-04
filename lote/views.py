from django.shortcuts import render
from .models import Lote
from .serializer import LoteSerializer
from rest_framework import viewsets

class LoteViewSet(viewsets.ModelViewSet):
 queryset = Lote.objects.all()
 serializer_class = LoteSerializer