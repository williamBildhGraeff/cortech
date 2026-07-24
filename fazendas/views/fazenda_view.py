
from ..serializers import FazendaSerializer
from ..factories import get_fazenda_service
from ..interface.fazenda_interface import FazendaInterface
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

class FazendaViewSet(APIView):
    def __init__(self, service: FazendaInterface = None, **kwargs):
        super().__init__(**kwargs)
        self.service = service or get_fazenda_service()

    def get(self, request, id=None, produtor_id=None):
        fazenda = self.service.get(id, produtor_id)
        if id:
            serializer = FazendaSerializer(fazenda)
        else: 
            serializer = FazendaSerializer(fazenda, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, produtor_id=None):
        serializer = FazendaSerializer(data=request.data)
        if serializer.is_valid():
            fazenda = self.service.post(serializer.validated_data)
            return Response(FazendaSerializer(fazenda).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id, produtor_id=None):
        fazenda = self.service.get(id)
        serializer = FazendaSerializer(fazenda, data=request.data)
        if serializer.is_valid():
            fazenda = self.service.put(id,serializer.validated_data)
            return Response(FazendaSerializer(fazenda).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id, produtor_id=None):
        self.service.delete(id)
        return Response(status=status.HTTP_204_NO_CONTENT)