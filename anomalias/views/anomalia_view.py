from rest_framework.views import APIView
from anomalias.serializers import AnomaliaSerializer
from anomalias.models import Anomalia
from anomalias.factories import get_anomalia_service
from anomalias.interfaces.anomalia_interface import AnomaliaInterface
from rest_framework import status
from rest_framework.response import Response

class AnomaliaViewSet(APIView):
    def __init__(self, service: AnomaliaInterface = None, **kwargs):
        super().__init__(**kwargs)
        self.service = service or get_anomalia_service()

    def get(self, request, id=None):
        anomalia = self.service.get(id)
        if id:
            serializer = AnomaliaSerializer(anomalia)
        else: 
            serializer = AnomaliaSerializer(anomalia, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
      
    
    def post(self, request):
        serializer = AnomaliaSerializer(data=request.data)
        if serializer.is_valid():
            anomalia = self.service.post(serializer.validated_data)
            return Response(AnomaliaSerializer(anomalia).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        anomalia = self.service.get(id)
        serializer = AnomaliaSerializer(anomalia, data=request.data)
        if serializer.is_valid():
            anomalia = self.service.put(id,serializer.validated_data)
            return Response(AnomaliaSerializer(anomalia).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        anomalia = self.service.delete(id)
        return Response(status=status.HTTP_204_NO_CONTENT)


        