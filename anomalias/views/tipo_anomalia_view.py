from rest_framework.views import APIView
from anomalias.serializers import TipoAnomaliaSerializer
from anomalias.models import TipoAnomalia
from anomalias.factories import get_tipo_anomalia_service
from anomalias.interfaces.tipo_anomalia_interface import TipoAnomaliaInterface
from rest_framework import status
from rest_framework.response import Response

class TipoAnomaliaViewSet(APIView):
    def __init__(self, service: TipoAnomaliaInterface = None, **kwargs):
        super().__init__(**kwargs)
        self.service = service or get_tipo_anomalia_service()

    def get(self, request, id=None):
        tipo_anomalia = self.service.get(id)
        if id:
            serializer = TipoAnomaliaSerializer(tipo_anomalia)
        else: 
            serializer = TipoAnomaliaSerializer(tipo_anomalia, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = TipoAnomaliaSerializer(data=request.data)
        if serializer.is_valid():
            tipo_anomalia = self.service.post(serializer.validated_data)
            return Response(TipoAnomaliaSerializer(tipo_anomalia).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        tipo_anomalia = self.service.get(id)
        serializer = TipoAnomaliaSerializer(tipo_anomalia, data=request.data)
        if serializer.is_valid():
            tipo_anomalia = self.service.put(id,serializer.validated_data)
            return Response(TipoAnomaliaSerializer(tipo_anomalia).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        tipo_anomalia = self.service.delete(id)
        return Response(status=status.HTTP_204_NO_CONTENT)