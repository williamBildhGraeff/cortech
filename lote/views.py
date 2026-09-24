from django.shortcuts import render
from .models import Lote
from .serializer import LoteSerializer
from rest_framework.views import APIView
from lote.interfaces.lote_interface import LoteInterface
from .factories import get_lote_service
from rest_framework.response import Response
from rest_framework import status

class LoteViewSet(APIView):
    
    def __init__(self, service: LoteInterface = None, **kwargs):
        super().__init__(**kwargs)
        self.service = service or get_lote_service()

    def get(self, request, id = None, fazenda_id = None):
        lote = self.service.get(id, fazenda_id)
        if id:
            serializer = LoteSerializer(lote)
        else: 
            serializer = LoteSerializer(lote, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, fazenda_id = None):
        serializer = LoteSerializer(data=request.data)
        if serializer.is_valid():
            lote = self.service.post(serializer.validated_data)
            return Response(LoteSerializer(lote).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id, fazenda_id = None):
        lote = self.service.get(id)
        serializer = LoteSerializer(lote, data=request.data)
        if serializer.is_valid():
            lote = self.service.put(id, serializer.validated_data)
            return Response(LoteSerializer(lote).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, fazenda_id = None):
        self.service.delete(id=id)
        return Response(status=status.HTTP_204_NO_CONTENT)
       
